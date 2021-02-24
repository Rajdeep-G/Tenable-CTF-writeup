import string
DRX = []
def xorStr(a, b):
    f = []
    if len(a)>len(b):
        a, b = b, a
    for i in range(len(a)):
        f.append(a[i]^b[i])

    for i in range(len(a), len(b)):
        f.append(b[i])

    return f

def move(a):
    return [ord(x) for x in a]

# def moveTRX(a):
#     TRX = [ord(x) for x in a]

def printB(a):
    for i in a:
        if chr(i) in string.printable:
            print(chr(i), end="")
        else:
            print(hex(i), end="")
    print()

def printHex(a):
    print(*[hex(i) for i in a])


def getVal(s):
    return [ord(i) for i in s]

# printB(xorStr(getVal("dogs"), getVal("shadows")))

TRX = (getVal("GED\x03hG\x15&Ka =;\x0c\x1a31o*5M"))
# TRX = (getVal("UL\x03d\x1c'G\x0b'l0kmm_"))

for line in range(85):

    inp = input().split()
    print(line, inp)
    v2=""
    cmd = inp[0]
    v1 = inp[1]
    if len(inp)==3:
        v2 = inp[2]

    print(v1, v2)
    if cmd == "MOV":
        if v1 == "DRX" and v2 =="TRX":
            DRX = TRX[::]
        elif v1 == "TRX" and v2=="DRX":
            TRX = DRX[::]
        elif v1 == "DRX":
            print(v1, v2[1:-1])
            DRX = move(v2[1:-1])
        elif v1 == "TRX":
            TRX = move(v2[1:-1])
    elif cmd == "REVERSE":
        if v1 == "DRX":
            DRX = DRX[::-1]
        elif v1 == "TRX":
            TRX = TRX[::-1]
    else:
        if v1 == "TRX":
            if v2 == "DRX":
                TRX = xorStr(TRX, DRX)
            elif v2 == "TRX":
                TRX = xorStr(TRX, TRX)
        elif v1 == "DRX":
            if v2 == "DRX":
                DRX = xorStr(DRX, DRX)
            elif v2 == "TRX":
                DRX = xorStr(TRX, DRX)

    print("DRX: ", end="")
    printB(DRX)
    print("TRX: ", end="")
    printB(TRX)
    print('--------------------------')