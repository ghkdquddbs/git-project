# try:
#     raise ArithmeticError
# except TypeError:
#     print("TypeError occurred!")
# except ArithmeticError:
#     raise ArithmeticError('Weird error')
#     print("ArithmeticError occurred!")
# finally:
#     print("Finished")
try:
    raise ArithmeticError
except TypeError:
    print("TypeError occurred!")
except ArithmeticError:
    raise Exception('Weird Error')
    print("ArithmeticError occurred!")
finally:
    print('Finished')
    