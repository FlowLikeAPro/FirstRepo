def division(firNum, secNum):
  if secNum != 0:
        return firNum / secNum
  else:
        return "Error: Division by zero my friend"

opMap = {
  '+' : float.__add__,
  '*' : float.__mul__,
  '/' : division,
  '-' : float.__sub__
}

3.0 + 4.0

3.0.__add__(4.0)
float.__add__(3.0,4.0)

def calculate():
  firNum = float(input("First Number: "))
  secNum = float(input("Second Number: "))
  op = input("Select operator: ")
  try:
    print(opMap.get(op)(firNum, secNum))
  except:
    print("WTF")
    
if __name__ == "__main__":
  calculate()