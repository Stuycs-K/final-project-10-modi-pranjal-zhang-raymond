def splitIntoBlocks(paddedStr){
    int numBlocks
    if len(paddedStr) % 1024 == 0:
        numBlocks = len(paddedStr) / 1024
    else:
        numBlocks = len(paddedStr) / 1024 + 1
    listBlocks = []
    for x in range(0, len(paddedStr), 1024):
        listBlocks.append(paddedStr[x:x+1024])
    return listBlocks
}

def processBlocks(listBlocks){
    int A,B,C,D,E,F,G,H = None
    for x in listBlocks:
        s = hash(x) # what does it mean traverse 80 times & how do i get the hex variables to be 64 bit (nvm i have to import libraries)

    AA = hex(A)
    BB = hex(B)
    CC = hex(C)
    DD = hex(D)
    EE = hex(E)
    FF = hex(F)
    GG = hex(G)
    HH = hex(H)
    finalStr = str(AA) + str(BB) + str(CC) + str(DD) + str(EE) + str(FF) + str(GG) + str(HH)
    return finalStr
}