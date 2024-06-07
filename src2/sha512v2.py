import tools, constants

initList = [tools.intToList(0x6a09e667f3bcc908), tools.intToList(0xbb67ae8584caa73b), tools.intToList(0x3c6ef372fe94f82b), tools.intToList(0xa54ff53a5f1d36f1), tools.intToList(0x510e527fade682d1), tools.intToList(0x9b05688c2b3e6c1f), tools.intToList(0x1f83d9abfb41bd6b), tools.intToList(0x5be0cd19137e2179)]

def sha512(msg):
    padded = tools.padMsg(msg)
    list_blocks = tools.splitIntoBlocks(padded, 1024)
    for chunk in list_blocks:
        fullWords = tools.genWords(chunk)
        A = initList[0]
        B = initList[1]
        C = initList[2]
        D = initList[3]
        E = initList[4]
        F = initList[5]
        G = initList[6]
        H = initList[7]
        for j in range(80):
            valOne = tools.add(H, tools.add(tools.ch(E, F, G), tools.add(tools.largeSigOne(E), tools.add(fullWords[j], tools.intToList(constants.list_constants[j])))))
            valTwo = tools.add(tools.largeSigZero(A), tools.maj(A, B, C))         
            H = G
            G = F
            F = E
            E = tools.add(D, valOne)
            D = C
            C = B
            B = A
            A = tools.add(valOne, valTwo)
            # print(tools.unsignedToSigned(int("".join(tools.intListToStr(A)), 2)))
        initList[0] = tools.add(initList[0], A)
        initList[1] = tools.add(initList[1], B)
        initList[2] = tools.add(initList[2], C)
        initList[3] = tools.add(initList[3], D)
        initList[4] = tools.add(initList[4], E)
        initList[5] = tools.add(initList[5], F)
        initList[6] = tools.add(initList[6], G)
        initList[7] = tools.add(initList[7], H)
    output = ""
    for i in initList:
        bitstring = "".join(tools.intListToStr(i))
        hexes = ""
        for i in range(0, len(bitstring), 4):
            toConv = bitstring[i:i + 4]
            hexes += hex(int(toConv, 2))[2:]
        output += hexes
    return output

print(sha512("hi"))
# print(len("46741x4x85x4x33x36x61x2x4x530x462x4x4x35x501x8x24x6x341333x12x2x60x2x1x71x50x2x1x2x4x44x156x72272x2x83x4x2x62x63x702x8x473437403x7x54x8x6x2020462x8730754173x8706x70x5x6x1x5411x74x7x3x36"))