
enter_string = input("Enter a string: ")
enter_string.lower()
vowels = "aeiou"
count_w = sum(1 for char in enter_string if char in vowels)
count_c = sum(1 for char in enter_string if char.isalpha() and char not in vowels)
print(f"Vowels: {count_w}, Consonants: {count_c}")