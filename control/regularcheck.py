import re
divide = re.compile(r'[n0°\.]/[n0°\.]')
cos = re.compile(r'c0.|.0s|c.s')
sin = re.compile(r'si.|.in|s.n')
tan = re.compile(r'\+a.|.an|\+.n')
log = re.compile(r'1[0o°]g')
arc = re.compile(r'.4c|a4.|a.c')
angle = re.compile(r'[0-9\)]\.[^0-9]')
def re_check(list):
    ls = ''.join([x for x in list])
    ls = re.sub('°', '.', ls)
    ls = re.sub(divide, "/", ls)
    ls = re.sub('l', "1", ls)
    ls = re.sub("t", "+", ls)
    ls = re.sub("o", "0", ls)
    ls = re.sub("r", "4", ls)
    ls = re.sub(cos, "cos", ls)
    ls = re.sub(sin, "sin", ls)
    ls = re.sub(tan, "tan", ls)
    ls = re.sub(log, "log", ls)
    ls = re.sub(arc, "arc", ls)
    w = angle.findall(ls)
    for i in w:
        ls = ls.replace(i, i[0] + "°" + i[2])
    #print(ls)
    return ls
    
'''while(1):
    a = input()
    l = re_check(a)
    print(l)
'''
