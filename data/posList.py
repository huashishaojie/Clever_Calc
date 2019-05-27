import cv2
import copy
import itertools
import numpy as np
class posList(list):
        
    def __init__(self):
        self = []
    
    def divide_pos(self, image):
        self.clear()
        self.image = image
        #cv2.imshow("line", image)
        show = np.zeros(self.image.shape[:])
        self.extend(self.vertical_cut([0, 0, image.shape[1], image.shape[0]]))
        for i in self:
            if(isinstance(i, list)):
                cv2.rectangle(show, (i[0], i[1]), (i[2], i[3]), 200, -1)
               # cv2.rectangle(show, (i[0], i[1]), (i[2], i[3]), 255, 1)
        #cv2.imshow("divide", show)
        #print(self)
        
    def vertical_cut(self, pos):
        v = []
        for x in range(pos[0], pos[2]):
            a = 0
            for y in range(pos[1], pos[3]):
                if(self.image[y, x] != 0):
                    a = a + 1
            v.append(a)
        
        tmplist = dict()
        left = right = 0
        
        i = 0
        while(i < len(v)):
            while(i < len(v) and v[i] == 0):
                i += 1
            left = i
            while(i < len(v) and v[i] != 0):
                i += 1
            right = i - 1
            if (left < right):
                q = tuple([left, right])
                num = max(v[left:right])
                tmplist[q] = num
        if(len(tmplist) <= 1 and list(tmplist.values())[0] > 4):
            result = self.horizontal_cut(pos)
        else:
            result=[]
            for key, value in tmplist.items():
                posi = [key[0] + pos[0], pos[1], key[1] + pos[0], pos[3]]
                if (isinstance(posi, list) and tmplist[(key[0], key[1])] > 4):
                    posi = self.horizontal_cut(posi)
                    result.extend(posi)
                else:
                    result.append(posi)
            if(len(result) > 1 or max(list(tmplist.values())) >= 4):
                result.insert(0, "(")
                result.extend(")")
        return result
                
    def horizontal_cut(self, pos):
        v = []
        for y in range(pos[1], pos[3]):
            a = 0
            for x in range(pos[0], pos[2]):
                if(self.image[y, x] != 0):
                    a = a + 1
            v.append(a)
        
        count = [key for key, value in enumerate(v) if value > 0]
        if(len(count) < 6):
            y1, y2 = [key + pos[1] for key in [count[0], count[-1]]]
            result = [[pos[0], y1, pos[2], y2]]
        else:
            if(len(count) == 6):
                y1, y2 = count[1], count[4]
            else:
                y1, y2 = [key for key, value in enumerate(v) if value == max(v)]
            y1, y2 = [key + pos[1] for key in [y1, y2]]
            tmpre = []
            tmpre.append([pos[0], pos[1], pos[2], y1-1])
            tmpre.extend([{"position":[(pos[2] + pos[0]) // 2, ((y2 + y1) // 2)], "char":"/", "size":(pos[3] - pos[1], pos[2] - pos[0])}])
            tmpre.append([pos[0], y2+1, pos[2], pos[3]])
            result = []
            for i in tmpre:
                if(isinstance(i, list)):
                    result.extend(self.vertical_cut(i))
                else:
                    result.append(i)
        return result    
                    
        
