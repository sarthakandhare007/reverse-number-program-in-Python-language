# Take input from the user
num = int(input("Enter a number: "))

reversed_num = 0

while num != 0:
    remainder = num % 10              # Get last digit
    reversed_num = reversed_num * 10 + remainder  # Append to reversed number
    num //= 10                         # Remove last digit

print("Reversed number:", reversed_num)
