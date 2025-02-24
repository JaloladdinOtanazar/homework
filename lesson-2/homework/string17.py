string = input("Enter a string: ")
symbol = input("Enter a symbol")
vowels = "aeiouAEIOU"
for vowel in vowels:
    string = string.replace(vowel, symbol)

# Print the result
print("the new string:", string)