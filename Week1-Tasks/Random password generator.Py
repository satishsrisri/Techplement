import random
import string
def password_generator(length, complexity):
    char_sets = {
        1: string.ascii_lowercase + string.ascii_uppercase,
        2: string.ascii_lowercase + string.ascii_uppercase + string.digits,
        3: string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation}
    characters = char_sets[complexity]
    while True:
        pwd = ''.join(random.choice(characters)
        for i in range(length))
        yield pwd
def main():
    while True:
        opt = input("Press 0 to generate Password (or) OFF to switch off generator: ")
        if opt == 'OFF':
            break
        elif opt == "0":
            try:
                length = int(input("Enter the password length: "))
                complexity = int(input("Enter the complexity (1-3): "))
                if complexity not in range(1, 4):
                    print("** Enter valid complexity value (1-3) **")
                    continue
                p = password_generator(length, complexity)
                pwd = next(p)
                print("Generated Password: ", pwd)
            except ValueError:
                print("** Enter valid integer values for length and complexity **")
        else:
            print("*** Enter valid inputs ***")
main()
