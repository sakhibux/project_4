def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Please type an subject and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()