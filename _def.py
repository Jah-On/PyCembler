methods = []
return_dict = {}
library_dict = {}
exec(b'from module_wrappers._builtins import *')
for method in __all__:
    if (method != '__all__') & (method != '_return_dict') & (method != '_library_dict'):
        methods.append(bytes(method, "utf8")[1:])
return_dict.update(_return_dict)
del _return_dict
library_dict.update(_library_dict)
del _library_dict

def embedded_call_constructor(call):
    # print(b'Call: ' + call)
    call_count = 0
    index = 0
    # print(call)
    # Identifier ▭
    try:
        imt(call)
        return call
    except:
        pass
    while b'++' in call:
        call = call.replace(b'++', b'+')
    while b'--' in call:
        call = call.replace(b'--', b'-')
    open_parenthesis = call.find(b'(')
    close_parenthesis = call.find(b')')
    if (close_parenthesis < call[open_parenthesis + 1:].find(b'(')):
        ops = []
        for slice in range(0, len(call)):
            if ((call[slice:slice + 1] == b'+') or (call[slice:slice + 1] == b'-') or (call[slice:slice + 1] == b'*') or (call[slice:slice + 1] == b'/') or (call[slice:slice + 1] == b'%')) and not (call[slice -1:slice] == b'('):
                ops.append(call[slice:slice + 1])
        # print("Ops")
        # print(len(ops))
        # print(ops)
        begin = 0
        end = 1
        split_calls = []
        for op in range(0, len(ops)):
            while not (call[end:end + 1] in [b'+', b'-', b'*', b'/', b'%']):
                if (call[end:end + 1] == b'('):
                    end += 2
                else:
                    end += 1
            split_calls.append(call[begin:end])
            begin = end + 1
            end += 1
        split_calls.append(call[end:len(call)])
        constructed = b''
        for sub_call in range(0,len(split_calls)):
            split_calls[sub_call] = embedded_call_constructor(split_calls[sub_call])
            constructed += split_calls[sub_call]
            if (len(ops) != sub_call):
                constructed += ops[sub_call]
        return constructed
    # elif
    while True:
        mIndex = len(call[index:])
        mIndexLen = 0
        found_in_pass = False
        for m in methods:
            if m in call[index:]:
                foundPos = call[index:].find(m)
                if (foundPos < mIndex):
                    mIndex = foundPos
                    mIndexLen = len(m)
                found_in_pass = True
        if not found_in_pass:
            break
        else:
            # print(eval(b'_' + call[mIndex:mIndexLen + 1] + embedded_call_constructor(call[mIndex + mIndexLen + 1:len(call) - 1]) + b')'))
            call_count += 1
            constructed = eval(b'_' + call[mIndex:mIndexLen + 1] + b'\"' + embedded_call_constructor(call[mIndex + mIndexLen + 1:call.rfind(b')')]) + b'\"' + b')') + call[call.rindex(b')') + 1:]
            return constructed
            index += mIndexLen + 1
    if call_count == 0:
        return call

    # spots = 0
    # call_tree = []
    # tree_spot = []
    # for index in range(0, len(call)):
    #     if call[index] == b'(':
    #         last_
    # for embedded_call in range(0, spots):
    #     pass
    # if (call_count == 0):
    #     return call

def generate(block,file):
    from builtins import type
    exec("from "  + file + " import *")
    lines = block.split(b'\n')
    # print(block)
    libraries_used = []
    blockOut = []
    name = lines[0][4:lines[0].index(b'(')]

    pointers = {}
    pointerType = {}
    if (lines[0].index(b'(') - lines[0].index(b')')) == -1:
        returnType = bytes(str(type(eval(name + b'()'))), "utf8")
        returnType = returnType[8:returnType.rindex(b'\'')]
        if returnType == b'NoneType':
            returnType = b'void'
        blockOut.append(returnType + b' ' + name + b'(){')

    for lineNum in range(1, len(lines)):
        line = lines[lineNum]
        indentations = 1
        indents = (indentations * b'\t')
        line = line.replace(b'\t', b' ')
        try:
            if b'=' in line:
                nonTab = 0
                while (line[nonTab] == b' '):
                    nonTab += 1
                cleanLine = line[nonTab:]
                cleanLine = cleanLine.replace(b' ', b'')
                if (cleanLine[cleanLine.find(b'=') + 1] != b'=') and (cleanLine[0:(cleanLine.find(b'='))] not in pointers):
                    pointer = cleanLine[0:(cleanLine.find(b'='))]
                    pointers[pointer] = 0
                    method_calls = []
                    # print(cleanLine[cleanLine.find(b'=') + 1:])
                    varType = bytes(str(type(eval(cleanLine[cleanLine.find(b'=') + 1:]))), "utf8")
                    varType = varType[8:varType.rindex(b'\'')]
                    pointerType[pointer] = varType
                    cleanLine = cleanLine.replace(b'True', b'true')
                    cleanLine = cleanLine.replace(b'False', b'false')
                    generated = embedded_call_constructor(cleanLine[cleanLine.find(b'=') + 1:len(cleanLine)])
                    # print(generated)
                    blockOut.append(indents + varType + b' ' + pointer + b' =' + generated + b';')
                    continue
        except Exception as e:
            print(e)
            # print(e)
        try:
            # Add case for not a pointer
            returnStringIndex = line.find(b'return ')
            returning = line[returnStringIndex + 7:]
            if returning in pointers:
                blockOut.append(indents + b'return ' + list(pointers)[list(pointers).index(returning)] + b';')
                continue
        except Exception as LordOdin:
            pass
        try:
            line = embedded_call_constructor(line.replace(b' ', b''))
            line = line.replace(b'True', b'true')
            line = line.replace(b'False', b'false')
            blockOut.append(indents + line + b';')
        except Exception as bug:
            pass

    methods.append(name)
    return_dict.update({name:returnType})
    blockOut.append(b'}\n')
    return [blockOut, libraries_used]
