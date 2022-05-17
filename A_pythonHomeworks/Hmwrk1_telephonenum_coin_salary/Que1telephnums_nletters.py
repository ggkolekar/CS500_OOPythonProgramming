
def telephone():

    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V"]
    numbers= [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8]

    print("Enter a single letter, and I will tell you what the corresponding digit is on the telephone.")

    alphabet = input("your input is = ")
    digit = -1;
    for i in range(len(letters)):
        if letters[i] == alphabet:
            digit = numbers[i];
            break;

    if digit != -1:
        print("The digit corresponds to the letter on the telephone " + str(numbers[i]))
    else:
        print("There is no digit on the telephone that corresponds to " + str(alphabet)+ ".")

if __name__ == '__main__':
    telephone()