import _def
import time
import subprocess
import platform

try:
    from input import *
    print("Input file compiled successfully... assembling!")
except:
    print("Input file has errors... halting!")
    quit()

fileIO = open("input.py", "rb")
dataIn = fileIO.read()
fileIO.close()

p = time.time()

functionCount = dataIn.count(b'def ')
functionsString = dataIn[0:]
linesOut = []
libs = []
for function in range(functionCount):
    first = functionsString.index(b'def')
    try:
        last = functionsString.find(b'\n\n')
        chop = 2
    except:
        last = functionsString.rindex(b'\n')
        chop = 1
    block = functionsString[first:last]
    output = _def.generate(block, "input")
    linesOut.extend(output[0])
    for c in range(0, len(output[1])):
        for l in range(0, len(output[1][c])):
            if output[1][c][l] not in libs:
                libs.append(output[1][c][l])
    functionsString = functionsString[(chop + last):]

print(time.time() - p)

finalOutput = b''
for libNum in range(0, len(libs)):
    finalOutput += b'#include ' + libs[libNum] + b'\n'
finalOutput += b'\n'
for global_var in range(0, len(_def.global_vars)):
    finalOutput += _def.global_vars[global_var] + b'\n'
finalOutput += b'\n'
for lineOutNum in range(0, len(linesOut)):
    finalOutput += linesOut[lineOutNum] + b'\n'
fileIO = open("output.cpp", "wb")
fileIO.write(finalOutput[:len(finalOutput) - 1])
fileIO.close()

OS = platform.system()
if OS == 'Linux':
    try:
        output = subprocess.check_output(['g++', 'output.cpp', '-o', 'output'])
        print("C++ code compiled successfully!")
    except Exception as compileError:
        print("One or more errors occured when compiling")
