def add(firNum, secNum):
  return firNum + secNum
def multiply(firNum, secNum):
  return firNum * secNum
def division(firNum, secNum):
  if secNum != 0:
        return firNum / secNum
  else:
        return "Error: Division by zero my friend"
def sub(firNum, secNum):
  return firNum - secNum

firNum = float(input("First Number: "))
secNum = float(input("Second Number: "))
op = input("Select operator: ")

def calculate():
  if op == '+':
    print(add (firNum, secNum))
  elif op == '*':
    print(multiply (firNum, secNum))
  elif op == '-':
    print(sub (firNum, secNum))
  elif op == '/':
    print(division (firNum, secNum))
  else:
    print("WTF")
    
if __name__ == "__main__":
    calculate()