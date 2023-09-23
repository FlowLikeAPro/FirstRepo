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

def operator():
  operator = input("Select operator: ")
  if operator == '+':
    print(add (firNum, secNum))
  elif operator == '*':
    print(multiply (firNum, secNum))
  elif operator == '-':
    print(sub (firNum, secNum))
  elif operator == '/':
    print(division (firNum, secNum))
  else:
    print("WTF")
    
if __name__ == "__main__":
    operator()