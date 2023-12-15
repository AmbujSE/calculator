from art_calculator import logo
def add (n1, n2):
  return n1 + n2
def subtract (n1, n2):
  return n1 - n2
def multiply (n1, n2):
  return n1 * n2
def divide (n1, n2):
  return n1 / n2
calculator = {'+' : add, '-' : subtract, "*" : multiply, '/' : divide}
def re_run():
  print(logo)
  num1 = float(input("What's the First number: "))
  for sign in calculator:
    print(sign)  
  running = True
  while running:
    selected_symbol = input("Pick an Operation: ")
    num2 = float(input("What's the next number: "))
        
    answer = calculator[selected_symbol]
    final = answer(num1, num2)
          
    print(f"{num1} {selected_symbol} {num2} = {final}")
    
    if input(f"Type 'y' if you want continue calculating with {final} type 'n' to start with a new calculation ") == "y":
      num1 = final
    else:
      running = False
      re_run()
re_run()