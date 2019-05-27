import cv2
import copy
import numpy as np
from data.posList import posList
class imageList(list):
    
    def __init__(self):
        self = []
            
    def deivde_image(self, image):
        self.clear()
        _, self.image = cv2.threshold(image, 122, 255, cv2.THRESH_BINARY_INV)
        self.lineimage = np.zeros(self.image.shape)
        #cv2.imshow("image", self.image)
        _, contours, _ = cv2.findContours(self.image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0, len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            position = [x + w // 2, y + h // 2]
            img = copy.copy(self.image[y:y+h, x:x+w])
            _, cont, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if(len(cont) > 1):
                for j in range(0, len(cont)):
                    lx, ly, lw, lh = cv2.boundingRect(cont[j])
                    if(lw < w or lh < h):
                        img[ly:ly+lh, lx:lx+lw] = 0
            self.append({"image":img, "position":position})
            cv2.rectangle(self.image, (x, y), (x+w-1, y+h-1), 255, 1)
            cv2.line(self.lineimage, (x, y+1), (x+w, y+1), 255, 1)
            cv2.line(self.lineimage, (x, y+h-1), (x+w, y+h-1), 255, 1)
        print(self)
        #cv2.imshow("findContours", self.image)
        if (self):
            return True
        else:
            return False
        #cv2.imshow("Contours", self.lineimage)
        
    def resize_image(self, img):
        height, width = img.shape[:]
        line = abs(height-width) // 2
        if(height > width):
            img = cv2.copyMakeBorder(img, 0, 0, line, line, cv2.BORDER_CONSTANT, 0)
            size = height
        else:
            img = cv2.copyMakeBorder(img, line, line, 0, 0, cv2.BORDER_CONSTANT, 0)
            size = width
        if(size > 200):
            ksize = size // 28
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize))
            img = cv2.dilate(img,  kernel)
        img = cv2.resize(img,(28, 28), interpolation=cv2.INTER_AREA)
        img = cv2.copyMakeBorder(img, 2, 2, 2, 2, cv2.BORDER_CONSTANT, 0)
        return img
    
    def get_lineimage(self):
       return self.lineimage
    
    def set_position(self, pos):
        poslist = pos.copy()
        for item in self:
            pos = item["position"]
            for i in range(len(poslist)):
                if(isinstance(poslist[i], list) and self.isin(pos, poslist[i])):
                    poslist.insert(i + 1, item)
                    if(self.isindex(pos, poslist[i])):
                        item['index'] = True
                    break
        i = 0 
        while(i < len(poslist)):
            if(isinstance(poslist[i], list)):
                n = 1
                while(i + n < len(poslist) and isinstance(poslist[i+n], dict) and "image" in poslist[i+n]):
                    n += 1
                poslist.remove(poslist[i])
                if(n > 2):
                    imgs = poslist[i:i+n-1]
                    newimgs = self.split_and_merge(imgs)
                    poslist[i:i+n-1] = newimgs
            i += 1
        for i in poslist:
            if(isinstance(i, dict) and "image" in i):
                img = i.get("image", False)
                i["size"] = img.shape[:]
                newimg = self.resize_image(img)
                i["image"] = newimg
        return poslist
                    
    
    def isin(self, point, rect):
        if(point[0] > rect[0] and point[0] < rect[2] and point[1] > rect[1] and point[1] < rect[3]):
            return True
        return False
        
    def isindex(self, point, rect):
        if(point[1] <= rect[1] + (rect[3] - rect[1]) / 3):
            return True
        return False
        
    def split_and_merge(self, l):
        l.sort(key= lambda k:k["position"])
        i = 0
        while(i < len(l) - 1):
            pos = l[i]["position"]
            nextpos = l[i+1]["position"]
            dy = nextpos[1] - pos[1]
            dx = nextpos[0] - pos[0]
            if(dx != 0):
                d = dy / dx
                if(d >= 2 or d <= -2):
                    l[i:i+2] = self.merge_img(l[i], l[i+1])
                    i -= 1
            i += 1
        return l
       
    def merge_img(self, now, next):
        pos = now["position"]
        img = now["image"]
        nextpos = next["position"]
        nextimg = next["image"]
        
        ltx = min(pos[0] - img.shape[1] // 2, nextpos[0] - nextimg.shape[1] // 2)
        lty = min(pos[1] - img.shape[0] // 2, nextpos[1] - nextimg.shape[0] // 2)
        rbx = max(pos[0] + img.shape[1] // 2, nextpos[0] + nextimg.shape[1] // 2)
        rby = max(pos[1] + img.shape[0] // 2, nextpos[1] + nextimg.shape[0] // 2)
        
        imgrect = [pos[0] - img.shape[1] // 2 - ltx, pos[1] - img.shape[0] // 2 - lty]
        nextimgrect = [nextpos[0] - nextimg.shape[1] // 2 - ltx, nextpos[1] - nextimg.shape[0] // 2 - lty]
        
        height, width = int(rbx - ltx), int(rby - lty)
        newimg = np.zeros([width+1, height+1], dtype = "uint8")
        newimg[imgrect[1]:imgrect[1] + img.shape[0], imgrect[0]:imgrect[0] + img.shape[1]] = img
        newimg[nextimgrect[1]:nextimgrect[1] + nextimg.shape[0], nextimgrect[0]:nextimgrect[0] + nextimg.shape[1]] = nextimg
        
        newpos = [ltx + newimg.shape[1] // 2, lty + newimg.shape[0] // 2]

        return [{"position":newpos, "image":newimg}]

