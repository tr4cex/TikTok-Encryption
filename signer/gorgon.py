from copy import deepcopy
from hashlib import md5

def hex_string(num):
    tmp_string = hex(num)[2:]
    if len(tmp_string) < 2:
        tmp_string = "0" + tmp_string
    return tmp_string

def reverse(num):
    tmp_string = hex(num)[2:]
    if len(tmp_string) < 2:
        tmp_string = "0" + tmp_string
    return int(tmp_string[1:] + tmp_string[:1], 16)

def RBIT(num):
    result = ""
    tmp_string = bin(num)[2:]
    while len(tmp_string) < 8:
        tmp_string = "0" + tmp_string
    for i in range(0, 8):
        result = result + tmp_string[7 - i]
    return int(result, 2)

class XG:
    def __init__(self, debug):
        self.length = 0x14
        self.debug = debug
        a1 = 228
        a2 = 208
        self.hex_510 = [0x1E, 0x00, 0xE0, a1, 0x93, 0x45, 0x01, a2]

    def addr_920(self):
        tmp = ""
        hex_920 = []
        for i in range(0x0, 0x100):
            hex_920.append(i)
        for i in range(0, 0x100):
            if i == 0:
                A = 0
            elif tmp:
                A = tmp
            else:
                A = hex_920[i - 1]
            B = self.hex_510[i % 0x8]
            if A == 0x55:
                if i != 1:
                    if tmp != 0x55:
                        A = 0
            C = A + i + B
            while C >= 0x100:
                C = C - 0x100
            if C < i:
                tmp = C
            else:
                tmp = ""
            D = hex_920[C]
            hex_920[i] = D
        return hex_920

    def initial(self, debug, hex_920):
        tmp_add = []
        tmp_hex = deepcopy(hex_920)
        for i in range(self.length):
            A = debug[i]
            if not tmp_add:
                B = 0
            else:
                B = tmp_add[-1]
            C = hex_920[i + 1] + B
            while C >= 0x100:
                C = C - 0x100
            tmp_add.append(C)
            D = tmp_hex[C]
            tmp_hex[i + 1] = D
            E = D + D
            while E >= 0x100:
                E = E - 0x100
            F = tmp_hex[E]
            G = A ^ F
            debug[i] = G
        return debug

    def calculate(self, debug):
        for i in range(self.length):
            A = debug[i]
            B = reverse(A)
            C = debug[(i + 1) % self.length]
            D = B ^ C
            E = RBIT(D)
            F = E ^ self.length
            G = ~F
            while G < 0:
                G += 0x100000000
            H = int(hex(G)[-2:], 16)
            debug[i] = H
        return debug

    def main(self):
        result = ""
        for item in self.calculate(self.initial(self.debug, self.addr_920())):
            result = result + hex_string(item)
        return "0404{}{}0001{}".format(
            hex_string(self.hex_510[7]), hex_string(self.hex_510[3]), result
        )

def X_Gorgon(params, data, cookie, rticket, model="utf-8"):
    gorgon = []
    _rticket = str(int(rticket * 1000))
    Khronos = hex(int(rticket))[2:]
    url_md5 = md5(bytearray(params, "utf-8")).hexdigest()
    for i in range(0, 4):
        gorgon.append(int(url_md5[2 * i: 2 * i + 2], 16))
    if data:
        if model == "utf-8":
            data_md5 = md5(bytearray(data, "utf-8")).hexdigest()
            for i in range(0, 4):
                gorgon.append(int(data_md5[2 * i: 2 * i + 2], 16))
        elif model == "octet":
            data_md5 = md5(data).hexdigest()
            for i in range(0, 4):
                gorgon.append(int(data_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0x0)
    if cookie:
        cookie_md5 = md5(bytearray(cookie, "utf-8")).hexdigest()
        for i in range(0, 4):
            gorgon.append(int(cookie_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0x0)
    for i in range(0, 4):
        gorgon.append(0x0)
    for i in range(0, 4):
        gorgon.append(int(Khronos[2 * i: 2 * i + 2], 16))

    return XG(gorgon).main()

def get_xgorgon(params, ticket, data="", cookie=""):
    return X_Gorgon(params=params, data=data, cookie=cookie, rticket=ticket)
