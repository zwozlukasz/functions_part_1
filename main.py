# functions

def func_1():
  print("Call function_1")
  return func_2()

def func_2():
  print("Call function_2")

# we have to define func_2() before we decide invoke func_1
func_1()