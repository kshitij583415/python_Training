# Sum of Digits

n=int(input("Enter a number: "))
sum=0

while (n > 0):
    last_digit = n % 10
    sum += last_digit
    n = n // 10
print("Sum of digits:", sum)

# output
# Enter a number: 564
# Sum of digits: 15