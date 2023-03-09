# PSEUDOCODE

# START
# DISPLAY 'Palindrome Checker'
# DISPLAY 'Please String:'
# x is equal to INPUT
# y is equal to REVERSE of x
# IF x is equal to y 
#     DISPLAY 'The input is Palindrome'
# ELSE 
#     DISPLAY 'The input isn't a Palindrome'
# END


# SOURCE CODE
print('\n')
print("Palindrome Checker")
x = str(input("Enter String: "))

# compares the x to the reversed x
# [::-1] returns string in reverse
if x == x[::-1]:
    print(f"'{x}' is a palindrome")
else:
    print(f"'{x}' isn't a palindrome")