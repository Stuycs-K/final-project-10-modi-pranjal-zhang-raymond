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

def rotateRight(bitString, num):
    part1 = bitString[-num:]
    part2 = bitString[:-num]
    return part1 + part2

def rotateLeft(bitString, num):
    part1 = bitString[num:]
    part2 = bitString[:num]
    return part1 + part2

def binAdd(bString1, bString2):
    # Assume len(bString1) = len(bString2)
    bStrLen = len(bString1)
    totString = ""
    curPos = bStrLen - 1
    carryIn = 0
    while curPos >= 0:
        b1Int = int(bString1[curPos])
        b2Int = int(bString2[curPos])
        totString = str(((b1Int ^ b2Int) ^ carryIn)) + totString
        if (b1Int + b2Int + carryIn) >= 2:
            carryIn = 1
        else:
            carryIn = 0
        curPos -= 1
    return totString

