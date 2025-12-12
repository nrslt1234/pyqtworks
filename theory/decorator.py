import time

def testTime(fn):
   def wrapper(*args):
       st = time.time()
       a = fn(*args)
       dt = time.time() - st
       print(f"Время работы: {dt} сек")
       return a

   return wrapper


@testTime
def getNOD(a, b):
   while a != b:
       if a > b:
           a-= b
       else:
           b -= a
   return a

print(getNOD(100000,2))