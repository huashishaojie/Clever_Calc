import re
from math import sin, cos, tan, log, sqrt, factorial, asin, acos, atan, radians, pi, factorial, e

arc = re.compile(r'arc[a-z]{3}')
radian = re.compile(r'\d+\.?\d*°|\(.*\)°')
word3 = re.compile(r'[a-z^e]{3}\d+\.?\d*°?π?|[a-z^e]{3}[πe]')
word4 = re.compile(r'[a-z^e]{4}\d+\.?\d*°?π?|[a-z^e]{4}[πe]')
ispi = re.compile(r'\dπ')
fac = re.compile(r'\d+\.?\d*!')
sqr = re.compile(r'√\d+\.?\d*')

def calc(s):
    w = arc.findall(s)
    for i in w:
        s = s.replace(i, "a" + i[3:])
    w = word3.findall(s)
    for i in w:
        s = s.replace(i, i[0:3]+"("+i[3:]+")")
    w = word4.findall(s)
    for i in w:
        s = s.replace(i, i[0:4]+"("+i[4:]+")")
    w = sqr.findall(s)
    for i in w:
        s = s.replace(i, "sqrt("+i[1:]+")")
    s = s.replace("√", "sqrt")
    w = radian.findall(s)
    for i in w:
        s = s.replace(i, "radians("+i[:-1]+")")
    w = ispi.findall(s)
    for i in w:
        s = s.replace(i, i[0] + "*pi")
    s = s.replace("π", "pi")
    w = fac.findall(s)
    for i in w:
        s = s.replace(i, "factorial(" + i[:-1] + ")" )
    s = s.replace("^", "**")
    #print(s)
    result = check_eval(s)
    if(result != "INPUT ERROR"):
        result = round(result, 4)
    return result

def check_eval(s):
    try:
        s = eval(s)
    except:
        return "INPUT ERROR"
    return s
