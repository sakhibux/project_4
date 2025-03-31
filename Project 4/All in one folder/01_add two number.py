
def main():
  try:
    num1 = (input("Enter the 1st Number "))
    num1 = int(num1)
    num2 = (input("Enter the 2nd Number "))
    num2 = int(num2)
    total = num1 + num2
    print(f" {num1} + {num2} = {total} ")
  except ValueError:
    print("Invalid input! please Enter number only.")
    
main()
    
   