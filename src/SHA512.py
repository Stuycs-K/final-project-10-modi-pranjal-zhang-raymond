import byteFunc

list_constants = [int("428a2f98d728ae22", 16), int("7137449123ef65cd", 16), int("b5c0fbcfec4d3b2f", 16),
        int("e9b5dba58189dbbc", 16), int("3956c25bf348b538", 16), int("59f111f1b605d019", 16),
        int("923f82a4af194f9b", 16), int("ab1c5ed5da6d8118", 16), int("d807aa98a3030242", 16),
        int("12835b0145706fbe", 16), int("243185be4ee4b28c", 16), int("550c7dc3d5ffb4e2", 16),
        int("72be5d74f27b896f", 16), int("80deb1fe3b1696b1", 16), int("9bdc06a725c71235", 16),
        int("c19bf174cf692694", 16), int("e49b69c19ef14ad2", 16), int("efbe4786384f25e3", 16),
        int("0fc19dc68b8cd5b5", 16), int("240ca1cc77ac9c65", 16), int("2de92c6f592b0275", 16),
        int("4a7484aa6ea6e483", 16), int("5cb0a9dcbd41fb44", 16), int("76f988da831153b5", 16),
        int("983e5152ee66dfab", 16), int("a831c66d2db43210", 16), int("b00327c898fb213f", 16),
        int("bf597fc7beef0ee4", 16), int("c6e00bf33da88fc2", 16), int("d5a79147930aa725", 16),
        int("06ca6351e003826f", 16), int("142929670a0e6e70", 16), int("27b70a8546d22ffc", 16),
        int("2e1b21385c26c926", 16), int("4d2c6dfc5ac42aed", 16), int("53380d139d95b3df", 16),
        int("650a73548baf63de", 16), int("766a0abb3c77b2a8", 16), int("81c2c92e47edaee6", 16),
        int("92722c851482353b", 16), int("a2bfe8a14cf10364", 16), int("a81a664bbc423001", 16),
        int("c24b8b70d0f89791", 16), int("c76c51a30654be30", 16), int("d192e819d6ef5218", 16),
        int("d69906245565a910", 16), int("f40e35855771202a", 16), int("106aa07032bbd1b8", 16),
        int("19a4c116b8d2d0c8", 16), int("1e376c085141ab53", 16), int("2748774cdf8eeb99", 16),
        int("34b0bcb5e19b48a8", 16), int("391c0cb3c5c95a63", 16), int("4ed8aa4ae3418acb", 16),
        int("5b9cca4f7763e373", 16), int("682e6ff3d6b2b8a3", 16), int("748f82ee5defb2fc", 16),
        int("78a5636f43172f60", 16), int("84c87814a1f0ab72", 16), int("8cc702081a6439ec", 16),
        int("90befffa23631e28", 16), int("a4506cebde82bde9", 16), int("bef9a3f7b2c67915", 16),
        int("c67178f2e372532b", 16), int("ca273eceea26619c", 16), int("d186b8c721c0c207", 16),
        int("eada7dd6cde0eb1e", 16), int("f57d4f7fee6ed178", 16), int("06f067aa72176fba", 16),
        int("0a637dc5a2c898a6", 16), int("113f9804bef90dae", 16), int("1b710b35131c471b", 16),
        int("28db77f523047d84", 16), int("32caab7b40c72493", 16), int("3c9ebe0a15c9bebc", 16),
        int("431d67c49c100d4c", 16), int("4cc5d4becb3e42b6", 16), int("597f299cfc657e2a", 16),
        int("5fcb6fab3ad6faec", 16), int("6c44198c4a475817", 16)]

a = 0x6a09e667f3bcc908
b = 0xbb67ae8584caa73b
c = 0x3c6ef372fe94f82b
d = 0xa54ff53a5f1d36f1
e = 0x510e527fade682d1
f = 0x9b05688c2b3e6c1f
g = 0x1f83d9abfb41bd6b
h = 0x5be0cd19137e2179

def processFunc(constantList, count, curList):
    valOne = constantList[7] + byteFunc.ch(constantList[4], constantList[5], constantList[6]) + byteFunc.largeSigma1((bin(constantList[4])[2:])) + int(curList[count], 2) + list_constants[count]
    valTwo = byteFunc.largeSigma0((bin(constantList[0])[2:])) + byteFunc.maj(constantList[0], constantList[1], constantList[2])
    constantList[3] = constantList[3] + valOne
    constantList[7] = valOne + valTwo

def sha512(message):
    global a, b, c, d, e, f, g, h
    formatted = byteFunc.padMsg(message)
    # print(len(formatted))
    blockNum = round(len(formatted) / 1024)
    chunks = byteFunc.splitIntoBlocks(formatted)
    # print(chunks)
    fullComponentList = []
    for i in chunks:
        chunk = byteFunc.chunkSplit(i, chunkLength = 64)
        # print(chunk)
        for i in range(64):
            chunk.append("")
        fullComponentList.append(chunk)
    
    for i in fullComponentList:
        for subchunkInd in range(16, 80):
            wordOne = byteFunc.smallSigma1(i[subchunkInd - 2])
            wordTwo = int(i[subchunkInd - 7], 2)
            wordThree = byteFunc.smallSigma0(i[subchunkInd - 15])
            wordFour = int(i[subchunkInd - 16], 2)
            sumWords = wordOne + wordTwo + wordThree + wordFour
            # sumWords = byteFunc.binAdd(byteFunc.intToBitstring(wordOne, 64), byteFunc.binAdd(byteFunc.intToBitstring(wordTwo, 64), byteFunc.binAdd(byteFunc.intToBitstring(wordThree, 64), byteFunc.intToBitstring(wordFour, 64))))
            # print((bin(sumWords)[2:]).zfill(64))
            i[subchunkInd] = (bin(sumWords)[2:]).zfill(64)
            # print(sumWords)
            # i[subchunkInd] = sumWords
    # print(fullComponentList)
    for i in fullComponentList:
        for j in i:
            A = a
            B = b
            C = c
            D = d
            E = e
            F = f
            G = g
            H = h
            constList = [B, C, D, E, F, G, H, A]
            counter = 0
            for h in range(10):
                constList = byteFunc.rotateRight(constList, 1)
                # print(constList)
                for k in range(8):
                    constList = byteFunc.rotateRight(constList, k)
                    # print(constList)
                    processFunc(constList, counter, i)
                    counter += 1
            a += constList[7]
            b += constList[0]
            c += constList[1]
            d += constList[2]
            e += constList[3]
            f += constList[4]
            g += constList[5]
            h += constList[6]
    return str(hex(a + b + c + d + e + f + g + h))

print(sha512("hi"))




             



# int A, B, C, D, E, F, G, H
# list_64bit = [A,B,C,D,E,F,G,H]