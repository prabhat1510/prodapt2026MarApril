#       012345       
fruit1='Orange'
#       0123
fruit2="Kiwi"
print(fruit1,fruit2)
print(type(fruit1))
print(type(fruit2))
print(dir(fruit1))
print(fruit2[2])
#fruit2[2]="J" #TypeError: 'str' object does not support item assignment
#print(fruit2)
print(fruit1.upper())
print(fruit2.lower())
print(fruit1)
print(fruit2)
print(fruit1.replace('r','R'))
print(fruit1)
#print(fruit1.translate())
print(fruit1.translate.__doc__)

print("************************")
# Create a translation table to replace 'a', 'e', 'i', 'o', 'u' with '1', '2', '3', '4', '5'
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

# Original string
text = "this is string example....wow!!!"

# Apply the translation table
translated_text = text.translate(trantab)

# Print the result
print(translated_text)
# Output: th3s 3s str3ng 2x1mpl2....w4w!!!