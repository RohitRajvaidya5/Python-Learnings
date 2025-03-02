# Error Handling In Python
---

## What is error handling ?

Error handling is a process that ensures the smooth execution of a program even when an error occurs. As the name suggests, error handling manages errors and provides appropriate error messages, which help in understanding the error and aid in debugging.

<br>

```python
number = input("Enter the number : ")
for i in range(1, 11):
    print(f"{number} x {i} = {int(number) * i}")
```

<br>

The above code prints the multiplication table of a number provided by the user. However, if the user enters letters or words instead of a number, the code will not execute and will result in an error.

<br>

**Error :**

<br>

```python
Enter the number : rohit
Traceback (most recent call last):
     print(f"{number} x {i} = {int(number) * i}")
                               ^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'rohit'
```

### try - except
<br>

To prevent this error, you should use exception handling with try-except, like this:

<br>


```python
try:
    number = input("Enter the number : ")
    for i in range(1, 11):
        print(f"{number} x {i} = {int(number) * i}")

# Gives errors by the system

except Exception as e:
    print(e)

# Error : output : invalid literal for int() with base 10: 'rohit'

```

### Custom Error Message

```python
try:
    number = input("Enter the number : ")
    for i in range(1, 11):
        print(f"{number} x {i} = {int(number) * i}")

# The line below displays a custom message when an error occurs.
# A ValueError exception occurs when the data type is correct, 
# but the value itself is inappropriate.

except ValueError:
    print("Error Occurred (Custom Error Handling Message)")
```

<br>


### Finally
---

`finally` is a keyword that always executes, regardless of whether the code inside the try block runs successfully or encounters an error.

```python
try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index : "))
    print(l[i])
except:
    print("Some error occurred")
finally:
    print("I am always executed")
```



