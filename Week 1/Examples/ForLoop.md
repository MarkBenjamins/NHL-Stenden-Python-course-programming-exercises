# Loops

Just like any other languages, Python has a way to loop certain code. Here is a detailed example that shows how the code works;

```python
# An array in python that contains 3 elements
countries = ["Netherlands", "England", "Germany", "Denmark"]
# This is the loop, in this case its a foreach loop.
# it loops through all of the countries.
for x in countries:
    # it uses x as the variable to store the country.
    # this means we can use x in the loop
    print(x)  # this prints the country that is currently assigned to x.
    # we can also use it in al kinds of different functions
    if x == "Netherlands":
        print("Nederland")  # this prints "Nederland" if the country is the netherlands
# this is the end of the for loop,
```

as you can see we loop through all of the elements in the array, shown here

```python
countries = ["Netherlands", "England", "Germany", "Denmark"]
for x in countries:
```

inside of the loop we can do whatever we want, and x is the current iteration in the loop, so we can use that to process as show below

```python
 print(x)
 if x == "Netherlands":
 	print("Nederland")
```

in Python this is marked by indentations, so its extra important that you keep you code clean.