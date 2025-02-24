c = float(input("Enter a temperature in degrees C: "))
def convert_cel_to_far():
    f = c * 9/5 + 32
    return f
print(f"{c} degrees C is", convert_cel_to_far(), "degrees F")
f = float(input("Enter a temperature in degrees F: "))
def convert_far_to_cel():
   c = (f - 32) * 5/9
   return c
print(f"{f} degrees F is", convert_far_to_cel(), "degrees C")
