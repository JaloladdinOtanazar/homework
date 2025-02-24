txt = "abcabcdabcdeabcdefabcdefg"
wowels = "aieuo"
new_one = ""

for i in range(len(txt)):
    new_one += txt[i]
    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        if txt[i] in wowels or txt[i-1] == '_':
            new_one += txt[i+1] + '_'
        else:
            new_one += '_'

print(new_one)
