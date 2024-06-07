import tools, constants

initList = [tools.intToList(0x6a09e667f3bcc908), tools.intToList(0xbb67ae8584caa73b), tools.intToList(0x3c6ef372fe94f82b), tools.intToList(0xa54ff53a5f1d36f1), tools.intToList(0x510e527fade682d1), tools.intToList(0x9b05688c2b3e6c1f), tools.intToList(0x1f83d9abfb41bd6b), tools.intToList(0x5be0cd19137e2179)]

def sha512(msg):
    padded = tools.padMsg(msg)
    list_blocks = tools.splitIntoBlocks(padded, 1024)
    for chunk in list_blocks:
        fullWords = tools.genWords(chunk)
        print(fullWords)
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
            toConv = "0b" + bitstring[i:i + 4]
            hexes += hex(int(toConv, 2))[2:]
        output += hexes
    return output

sha512("hi")
print(len("0c05560c4e26088f7ab436dcaa34c405f286417105b0e62ad00feb626ede6984383ed812bc2312bfc9a69030ebbef4fec5cd225c5788c3392691421f175bd24c"))
          #150a14ed5bea6cc731cf86c41566ac427a8db48ef1b9fd626664b3bfbb99071fa4c922f33dde38719b8c8354e2b7ab9d77e0e67fc12843920a712e73d558e197