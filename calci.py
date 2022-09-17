#Calculator
from  art import logo
print(logo)
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}
def calci():
    num1 = float(input("What's the first number?: "))
    for charc in operations:
        print(charc)
    conti =  True
    while conti:
          operation_sym = input("choose a operation symbol from above: ")
          num2 = float(input("What's the next number?: "))  
          operate = operations[operation_sym]
          f_answer = operate(num1,num2)
          print(f"{num1} {operation_sym} {num2} = {f_answer}")
          repeat_opr = input("do you want to repeat the opration yes/no: ").lower()
          if repeat_opr=="y":
            num1=f_answer
          else:
            conti:False
            calci()

calci()
