#import sys import audioop


id =10
name = "surender"

def add():
    result = id +4
    print(result)

def add_and_return():
    result = id +4
    return result*2

def add_numbers(n1,n2):
    return n1+n2

def main():

   add()
   r = add_and_return()
   r1 = add_and_return()
   print(f"result of add_and_return {r}")
   print(f"result of add_and_return {r1}")

   n_result = add_numbers(2,4)
   print(f"result of add_and_return {n_result}")
   print(__name__)
"""
if __name__ == "__main__":
 main()
 """








