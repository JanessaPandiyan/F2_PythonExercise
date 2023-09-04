
print("Question 1: ")

celsius = float(input("Celsius: "))
fahrenheit = celsius * 1.8 + 32.00
print(f"Fahrenheit: {fahrenheit:.2f}")

print("\nQuestion 2: ")

int_1 = int(input("Integer 1: "))
int_2 = int(input("Integer 2: "))
int_3 = int(input("Integer 3: "))

max = int_1
if max < int_2:
    max = int_2
if max < int_3:
    max = int_3

print("Max Integer: ", + max)

print("\nQuestion 3: ")

number = input("Number: ")
i = 0
max_digit = -1
min_digit = 10

for num in number:
    n = int(num)
    if n > max_digit:
        max_digit = n
    if n < min_digit:
        min_digit = n
    i += 1

print("Number of digits in the given number is:", i)
print("Smallest number is:", min_digit)
print("Highest number is:", max_digit)

print("\nQuestion 4: ")

givenum = int(input("Number: "))
sum = 0

for i in range(0, givenum+1):
    sum+=i

print("Sum:", + sum)

print('\nQuestion 5: ')

def decToBinary(dec):
    if dec == 0:
        return "0"
    binary = ""
    while dec > 0:
        binary = str(dec % 2) + binary
        dec = dec // 2
    return binary


def binaryToN(bin, type):
    dec = 0
    for digit in bin:
        dec = dec * 2 + int(digit)

    if type == "dec":
        return dec
    elif type == "oct":
        return decToOctal(dec)
    elif type == "hex":
        return decToHex(dec)
    else:
        return "Type not valid"


def decToOctal(dec):
    if dec == 0:
        return "0"
    octal = ""
    while dec > 0:
        octal = str(dec % 8) + octal
        dec = dec // 8
    return octal


def decToHex(dec):
    if dec == 0:
        return "0"
    hex_value = ""
    hex_chars = "0123456789ABCDEF"
    while dec > 0:
        hex_value = hex_chars[dec % 16] + hex_value
        dec = dec // 16
    return hex_value


def main():
    decimal = int(input("Decimal number: "))
    print("Binary:", decToBinary(decimal))
    print("Octal:", decToOctal(decimal))
    print("Hex:", decToHex(decimal))

    binary = input("Binary number: ")
    print("Decimal:", binaryToN(binary, "dec"))
    print("Octal:", binaryToN(binary, "oct"))
    print("Hex:", binaryToN(binary, "hex"))


main()




