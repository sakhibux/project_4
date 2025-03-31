
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()

def main():
    fahrenheit = int(input("Enter temprature in Fahrenheit "))
    celsius = (fahrenheit - 32)* 5.8 / 9.0
    print(f"Temprature {fahrenheit}F = {celsius}C")
main()