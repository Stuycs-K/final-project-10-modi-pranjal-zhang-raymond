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
    lenMessageBits = surroundZeros(strToBitStr(str(len(message))), 64, "F")
    