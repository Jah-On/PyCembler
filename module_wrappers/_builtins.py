# MUST BE CODED FOR C++
# Arrange in alphabetical order
# Remove from "Not yet added" list once implemented and tested

# Not yet added [delattr, hash, memoryview, set, all, dict, help, min, setattr, any, dir, hex, next, sliceascii, divmod, id, object, sortedbin, enumerate, input, oct, staticmethod, bool, eval, int, open, strbreakpoint, exec, isinstance, ord, sumbytearray, filter, issubclass, pow, super, bytes, float, iter, tuplecallable, format, len, property, type, chr, frozenset, list, range, vars, classmethod, getattr, locals, repr, zip, compile, globals, map, reversed, __import__, complex, hasattr, max]

method_list = [b'abs', b'print', b'round']

def abs(number):
    return b'abs(' + bytes(str(number), "utf8") + ')'

def abs_lib():
    return [b'<cmath>']

# def all(pointer):
#     return b'for (auto &part : pointer)'

def round(number):
    return b'round(' + bytes(str(number), "utf8") + ')'

def round_lib():
    return [b'<cmath>']

def print(data):
    return b'cout << ' + data + b' << \"\\n\"'

def print_lib():
    return [b'<iostream>']
