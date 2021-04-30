# If-Else 

In Python there is also an If Else statement to compare values, the given values are:

```python
x = 121
y = 29
```

Now we can use the if statement to compare the values of x and y:

```python
if x > y:
    print('x is greater than y')
```

We can expand this with the else statement:

```python
if x > y:
    print('x is greater than y')
else:
    print('y is greater than x')
```

If we want to add more comparisons, we can use the elif(else if) statement:

```python
if x > y:
    print('x is greater than y')
elif x == y:
    print('x and y are equal')
else:
    print('y is greater than x')
```

You can add as many elif statements as you like. If there are more then 5, most of the times there is a better solution.
