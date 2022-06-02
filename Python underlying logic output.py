def func():
        a, b = b, a

import dis
dis.dis(func)

'''
  2           0 LOAD_FAST                0 (b)
              2 LOAD_FAST                1 (a)
              4 ROT_TWO
              6 STORE_FAST               1 (a)
              8 STORE_FAST               0 (b)
             10 LOAD_CONST               0 (None)
             12 RETURN_VALUE
'''
