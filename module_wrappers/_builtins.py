# MUST BE CODED FOR C++
# Arrange in alphabetical order
# Remove from "Not yet added" list once implemented and tested

# Not yet added [delattr, hash, memoryview, set, all, dict, help, min, setattr, any, dir, hex, next, sliceascii, divmod, id, object, sortedbin, enumerate, input, oct, staticmethod, bool, eval, int, open, strbreakpoint, exec, isinstance, ord, sumbytearray, filter, issubclass, pow, super, bytes, float, iter, tuplecallable, format, len, property, type, chr, frozenset, list, range, vars, classmethod, getattr, locals, repr, zip, compile, globals, map, reversed, __import__, complex, hasattr, max]

__all__ = ['_abs', '_print', '_round', '_return_dict', '_library_dict', '__all__']
_return_dict = {b'_abs':b'ID', b'_print':b'void', b'_round':b'int'}
_library_dict = {b'_abs':[b'<cmath>'], b'_print':[b'<iostream>'], b'_round':[b'<cmath>']}

def _abs(number):
    return b'std::abs(' + bytes(str(number), "utf8") + b')'

# def all(pointer):
#     return b'for (auto &part : pointer)'

def _print(data):
    return b'std::cout << ' + bytes(str(data), 'utf8') + b' << \"\\n\"'

def _round(number):
    return b'std::round(' + bytes(str(number), "utf8") + b')'
