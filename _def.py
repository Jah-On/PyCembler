def generate(block,file):
    from builtins import type
    exec("from "  + file + " import *")
    lines = block.split(b'\n')
    # print(block)
    blockOut = []
    name = lines[0][4:8]

    pointers = {}
    pointerType = {}
    if (lines[0].index(b'(') - lines[0].index(b')')) == -1:
        returnType = bytes(str(type(eval(name + b'()'))), "utf8")
        returnType = returnType[8:returnType.rindex(b'\'')]
        blockOut.append(returnType + b' ' + name + b'(){')

    for lineNum in range(1, len(lines)):
        line = lines[lineNum]
        indentations = 1
        indents = (indentations * b'\t')
        line = line.replace(b'\t', b' ')
        try:
            nonTab = 0
            while (line[nonTab] == b' '):
                nonTab += 1
            cleanLine = line[nonTab:]
            while b'  ' in cleanLine:
                cleanLine = cleanLine.replace(b'  ', ' ')
            if (cleanLine[cleanLine.find(b'=') + 1] != b'=') and (cleanLine[0:(cleanLine.find(b'='))] not in pointers):
                pointer = cleanLine[0:(cleanLine.find(b'='))].replace(b' ', b'')
                pointers[pointer] = 0
                type = bytes(str(type(eval(line[cleanLine.find(b'=') + 1 + nonTab:]))), "utf8")
                type = type[8:type.rindex(b'\'')]
                pointerType[pointer] = type
                blockOut.append(indents + type + b' ' + pointer + b' =' + cleanLine[cleanLine.find(b'=') + 1:] + b';')
        except Exception as e:
            pass
            # print(e)
        try:
            returnStringIndex = line.find(b'return ')
            returning = line[returnStringIndex + 7:]
            if returning in pointers:
                blockOut.append(indents + b'return ' + list(pointers)[list(pointers).index(returning)] + b';')
        except Exception as LordOdin:
            print(LordOdin)
            pass
    blockOut.append(b'}\n')
    return blockOut
