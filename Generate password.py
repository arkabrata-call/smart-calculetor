import string
import random

def generat_password(length=8):
    print("Generating a random password")
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(char) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length of password: "))
    generated_password = generat_password(password_length)
    print("The password is:", generated_password)
if __name__ == "__main__":
    main()