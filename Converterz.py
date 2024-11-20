hexacode = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
    }

def reverser(x):
    xy = list(reversed(x))
    xz = ''.join(xy)
    return xz

def stringer(x):
    xy = ''.join(x)
    return xy

def convertbinary(x,binary):
    remainder = x%2
    floor = x//2
    binary.append(str(remainder))
    if floor != 0:
        convertbinary(floor,binary)
    return binary


def convertoctal(x,octal):
    remainder = x%8
    floor = x//8
    octal.append(str(remainder))
    if floor != 0:
        convertoctal(floor,octal)
    return octal
     
def converthexa(x,hexa):
    remainder = x%16
    floor = x//16
    if remainder >= 10:
        hexa.append(str(hexacode[remainder]))
    else:
        hexa.append(str(remainder))
    if floor != 0:
        converthexa(floor,hexa)
    return hexa

def convertgray(x,binary,gray):
    r = int(0)
    binary = []
    convertbinary(x,binary)
    gray.append(str(binary[0]))
    while r < (len(binary)-1):
        if binary[r] == binary[r+1]:
            gray.append('0')
        else:
            gray.append('1')
        r+=1
    return gray

