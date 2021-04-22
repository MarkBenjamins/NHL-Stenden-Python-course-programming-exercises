# :repeat: Loops

Just like any other languages, Python has a way to loop certain code. Here are some detailed examples that shows how the code works.

### For (each) loop

In Python a For loop is used to "create" a foreach loop, this can be achieved by using the "in" keyword as shown below.

```python
# An array in Python that contains 3 elements.
countries = ["Netherlands", "England", "Germany", "Denmark"]
# This is the loop, in this case its a foreach loop.
# It loops through all of the countries.
for x in countries:
    # It uses x as the variable to store the country.
    # This means we can use x in the loop.
    print(x)  # this prints the country that is currently assigned to x.
    # We can also use it in al kinds of different functions
    if x == "Netherlands":
        print("Nederland")  # This prints "Nederland" if the country is the netherlands.
# This is the end of the for loop.
```

As you can see we loop through all of the elements in the array, shown here.

```python
countries = ["Netherlands", "England", "Germany", "Denmark"]
for x in countries:
```

Inside of the loop we can do whatever we want, and x is the current iteration in the loop, so we can use the x variable to preform calculations or other manipulations as show below.

```python
 print(x)
 if x == "Netherlands":
 	print("Nederland")
```

In Python this is marked by indentations, so its extra important that you keep you code clean.

### For loop

The for loop can also be used a numerous amount of times with the range function, here are some examples;

```python
# This is a for loop.
for x in range(8):
    print(x)
# It prints 0 to 7.

# This is also a for loop.
for x in range(3, 9):
    print(x)
# It prints 3 to 8.

# This is also a for loop.
for x in range(4, 21, 2):
    print(x)
# It prints 4 8 12 16 an 20. So it prints 4 to 20, with steps of 4.
```

### While loop

The last loop in python is the while loop, it looks like this;

```python
# This is a simple while loop.
x = 4
while x > 10:
    print(x)
    x += x
# It prints 4 to 9.
```

