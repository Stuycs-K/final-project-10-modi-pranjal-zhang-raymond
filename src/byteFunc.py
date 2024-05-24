def strToBitStr(msg):
    bitstring = ""
    for i in msg:
        intRep = ord(i)
        bitstring += (bin(intRep)[2:]).zfill(8) # Removes built-in '0b' indicator from bitstring
    return bitstring

def bitStrToHex(bitstring):
    halfByteList = []
    hexString = ""
    for i in range(round(len(bitstring) / 4)):
        halfByteList.append("0b" + bitstring[4 * i: 4 * i + 4]) # Have to add python byte indicator
    for i in halfByteList:
        hexString += hex(int(i, 2))[2:]
    return hexString

def surroundZeros(bitString, desiredLength, frontOrBack):
    if frontOrBack == "F":
        for i in range(len(bitString), desiredLength):
            bitString = "0" + bitString
    else:
        for i in range(len(bitString), desiredLength):
            bitString = bitString + "0"
    return bitString

def chunkSplit(bitstring, chunkLength = 512):
    chunks = []
    for i in range(0, len(bitstring), chunkLength):
        chunks.append(bitstring[i: i + chunkLength])
    return chunks

def padMsg(message):
    bitMsg = strToBitStr(message)
    bitMsgLen = len(bitMsg)
    extraMults = 0
    for i in range(1, 3):
        if (((bitMsgLen // 1028) + i) * 1028 - bitMsgLen) >= 128:
            extraMults = i
            break
    desiredLength = ((bitMsgLen // 1028) + extraMults) * 1028 - 128
    paddedStr = bitMsg
    if desiredLength != bitMsgLen:
        paddedStr = bitMsg + "1" + "0" * (desiredLength - bitMsgLen - 1)
    lenMessageBits = surroundZeros(strToBitStr(str(len(message))), 128, "F")
    return paddedStr + lenMessageBits
    
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

# def processBlocks(listBlocks){
#     int A,B,C,D,E,F,G,H = None
#     for x in listBlocks:
#         s = hash(x) # what does it mean traverse 80 times & how do i get the hex variables to be 64 bit (nvm i have to import libraries)

#     AA = hex(A)
#     BB = hex(B)
#     CC = hex(C)
#     DD = hex(D)
#     EE = hex(E)
#     FF = hex(F)
#     GG = hex(G)
#     HH = hex(H)
#     finalStr = str(AA) + str(BB) + str(CC) + str(DD) + str(EE) + str(FF) + str(GG) + str(HH)
#     return finalStr
# }
