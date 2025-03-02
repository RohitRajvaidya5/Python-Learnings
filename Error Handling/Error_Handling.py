
number = input("Enter the number : ")
for i in range(1, 11):
    print(f"{number} x {i} = {int(number) * i}")


try:
    number = input("Enter the number : ")
    for i in range(1, 11):
        print(f"{number} x {i} = {int(number) * i}")

# Gives errors by the system
except Exception as e:
    print(e)

# output : invalid literal for int() with base 10: 'rohit'

except ValueError:
    print("Error Occurred (Custom Error Handling Message)")