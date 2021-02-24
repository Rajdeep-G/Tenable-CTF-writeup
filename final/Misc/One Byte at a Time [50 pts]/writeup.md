```py
from pwn import *
HOST = 'challenges.ctfd.io'
PORT = 30468
flag = 'flag{f0ll0w_th3_whit3_r@bbit'

def getChar(hexi):
    poss = []
    for i in range(0, 256):
        if i^int(hexi, 16) < 256:
                ch = chr(i^int(hexi, 16))
                if ch in string.printable:
                        poss.append(ch)

    return poss

def test(c):
    print('Trying', c)
    conn = remote(HOST, PORT)
    conn.recvuntil('[flag]>')
    conn.sendline(flag+str(c))
    conn.recvline()
    chk = conn.recvline().decode('ascii')
    # print(chk)
    return (not chk.startswith('Flag does not start with characters entered'))
    # data = conn.read().decode('ascii').strip()

while True:
    conn = remote(HOST, PORT)
    conn.recvuntil('[flag]>')
    print('Sending Flag', flag)
    conn.sendline(flag)
    conn.recvuntil('IPv4 address I have...')
    data = conn.read().decode('ascii').strip()
    print(data)
    chSet = getChar(data)
    for ch in chSet:
        if test(ch):
            flag += str(ch)
            print(flag)
```