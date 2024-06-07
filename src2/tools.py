# Initialization Functions

def strToBitStr(msg):
    bitstring = ""
    for i in msg:
        intRep = ord(i)
        bitstring += (bin(intRep)[2:]).zfill(8) # Removes built-in '0b' indicator from bitstring
    return bitstring

def intToBitstring(intRep, desiredLength = 64):
    posString = bin(intRep)
    if posString[0] == "-":
        posString = posString[0] + posString[3:]
    else:
        posString = posString[2:]
    return posString.zfill(desiredLength)

def strToList(message):
    list = []
    for i in message:
        list.append(int(i))
    return list

def padMsg(message):
    bitMsg = strToBitStr(message)
    bitMsgLen = len(bitMsg)
    extraMults = 0
    for i in range(1, 3):
        if (((bitMsgLen // 1024) + i) * 1024 - bitMsgLen) >= 128:
            extraMults = i
            break
    desiredLength = ((bitMsgLen // 1024) + extraMults) * 1024 - 128
    paddedStr = bitMsg
    if desiredLength != bitMsgLen:
        paddedStr = bitMsg + "1" + "0" * (desiredLength - bitMsgLen - 1)
    lenMessageBits = intToBitstring(bitMsgLen, 128)
    return strToList(paddedStr + lenMessageBits)

def splitIntoBlocks(paddedStr, desiredLength = 1024):
    listBlocks = []
    for x in range(0, len(paddedStr), desiredLength):
        listBlocks.append(paddedStr[x:x+desiredLength])
    return listBlocks

# Logic Functions

def and_(x, y):
    andList = []
    for i in range(len(x)):
        andList.append(x[i] & y[i])
    return andList

def or_(x, y):
    orList = []
    for i in range(len(x)):
        orList.append(x[i] | y[i])
    return orList

def xor_(x, y):
    xorList = []
    for i in range(len(x)):
        xorList.append(x[i] ^ y[i])
    return xorList

def not_(x):
    notList = []
    for i in range(len(x)):
        notList.append(~x[i])
    return notList

def xor_xor_(x, y, z):
    xorXorList = []
    for i in range(len(x)):
        xorXorList.append(x[i] ^ y[i] ^ z[i])
    return xorXorList

# Manipulation Functions

def rotateRight(msg, num):
    return msg[-num:] + msg[num:]

def shiftRight(msg, num):
    shiftList = []
    for i in range(num):
        shiftList.append(0)
    shiftList = shiftList + msg[:-num]
    return shiftList

def add(x, y):
    resultList = []
    for i in range(len(x)):
        resultList.append("")
    carry = 0
    for i in range(len(x) - 1, -1, -1):
        resultList[i] = x[i] ^ y[i] ^ carry
        if (x[i] + y[i] + carry) // 2 == 1:
            carry = 1
        else:
            carry = 0
    return resultList

# Misc. Functions

def zeroList(len):
    zerosList = []
    for i in range(len):
        zerosList.append(0)
    return zerosList

def intToList(constant):
    bitstring = bin(constant)[2:].zfill(64)
    list = strToList(bitstring)
    return list

def intListToStr(intList):
    strList = []
    for i in intList:
        strList.append(str(i))
    return strList

# Processing Functions

def genWords(chunk):
    wordList = splitIntoBlocks(chunk, desiredLength = 64)
    for i in range(64):
        wordList.append(zeroList(64))
    for i in range(16, 80):
        sigZero = xor_xor_(rotateRight(wordList[i - 15], 1), rotateRight(wordList[i - 15], 8), shiftRight(wordList[i - 15], 7))
        sigOne = xor_xor_(rotateRight(wordList[i - 2], 19), rotateRight(wordList[i - 2], 61), shiftRight(wordList[i - 2], 6))
        wordList[i] = add(sigOne, add(wordList[i - 7], add(sigZero, wordList[i - 16])))
    return wordList

def largeSigOne(l):
    return xor_xor_(rotateRight(l, 14), rotateRight(l, 18), rotateRight(l, 41))

def largeSigZero(l):
    return xor_xor_(rotateRight(l, 28), rotateRight(l, 34), rotateRight(l, 39))

def ch(x, y, z):
    return xor_(and_(x, y), and_(not_(x), z))

def maj(x, y, z):
    return xor_xor_(and_(x, y), and_(x, z), and_(y, z))