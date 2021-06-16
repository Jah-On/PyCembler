import _def

try:
    from input import *
    print("Input file compiled successfully... assembling!")
except:
    print("Input file has errors... halting!")
    quit()

fileIO = open("input.py", "rb")
dataIn = fileIO.read()
fileIO.close()

functionCount = dataIn.count(b'def ')
functionsString = dataIn[0:]
linesOut = []
for function in range(functionCount):
    first = functionsString.index(b'def')
    try:
        last = functionsString.find(b'\n\n')
        chop = 2
    except:
        last = functionsString.rindex(b'\n')
        chop = 1
    block = functionsString[first:last]
    linesOut.extend(_def.generate(block, "input"))
    functionsString = functionsString[(chop + last):]

finalOutput = b''
for lineOutNum in range(0, len(linesOut)):
    finalOutput += linesOut[lineOutNum] + b'\n'
fileIO = open("output.c", "wb")
fileIO.write(finalOutput)
fileIO.close()
