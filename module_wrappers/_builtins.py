# MUST BE CODED FOR C++
# Arrange in alphabetical order
# Remove from "Not yet added" list once implemented and tested

# Not yet added [delattr, hash, memoryview, set, all, dict, help, min, setattr, any, dir, hex, next, sliceascii, divmod, id, object, sortedbin, enumerate, input, oct, staticmethod, bool, eval, int, open, strbreakpoint, exec, isinstance, ord, sumbytearray, filter, issubclass, pow, super, bytes, float, iter, tuplecallable, format, len, property, type, chr, frozenset, list, range, vars, classmethod, getattr, locals, repr, zip, compile, globals, map, reversed, __import__, complex, hasattr, max]

# __all__ is a key variable for Python's import system. It tells what variables (functions are a variable!) are included in the module
__all__ = ['_abs', '_print', '_round', '_return_dict', '_library_dict', '__all__']

# _return_dict allows the main runner code to grab trhe expected return type of a function

# ID: Indicates a return type that depends on the input type
# void: Indicates there is no return value

# As more types beyond the primative types are added, a list of types will be included
_return_dict = {b'_abs':b'ID', b'_print':b'void', b'_round':b'int'}

# _library_dict tells what libraries are required to use a specific function
_library_dict = {b'_abs':[b'<cmath>'], b'_print':[b'<iostream>'], b'_round':[b'<cmath>']}

# All functions have to start with a hyphen
# This is because it allows Python to distinguish between it's own functions and one's that are made in this module

# std is the namespace a function would typically fall under when using included C++ libs
# Always check what namespace a library falls under!!!

# I don't think it's a good idea to have "using namespace ..." inside an autogenerated system since it will likely lead to conflicts
# "More work now, way less work later" - Jah-On

# Do NOT add semi-colons to these. The main runner will do that automatically!

# Always convert input to bytes (as demonstrated below) and always use UTF-8 (also demonstrated below).

# You are taking C++ functions, adding input to it, and returning it.

def _abs(number):
    return b'std::abs(' + bytes(str(number), "utf8") + b')'

def _print(data=b'\n'):
    if len(data) == 0:
        return b'std::cout << \"\\n\"'
    return b'std::cout << ' + bytes(str(data), 'utf8') + b' << \"\\n\"'

def _round(number):
    return b'std::round(' + bytes(str(number), "utf8") + b')'
