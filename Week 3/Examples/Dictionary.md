# Dictionary example
In the example below we are trying to go right 40, left 20, forward 25 then right again 15. 
The problem that arises here is that you can only use a key once.
If used more, then the last used time will just simple overwrite the other uses.

Example List:

```python
ExampleListOverwrite = {
    'right': 40,
    'left': 20,
    'forward': 25,
    'right': 15
}
```

So what happens here is that the drone will perform this:

```
15 to the right
20 to the left
25 forward
```

 This happens because the value of the last command use of 'right' has overwritten the first value.



The dictionary we are going to use for the exercises is a multidimensional list. It is a list with multiple lists within itself. We use this specific sort of list, because normally a list overwrites keys of the same name. This makes it so we cant do a command multiple times. Using this system of nested lists, we are bypassing this problem.

Every list is composed of a key and an value. This makes it so we can access the values through the keys from each list.

Example dictionary:

```python
ExampleDictionary = {
    1: {'right': 80 }
    2: {'right': 40, 'left': 15 }
    3: {'left': 20 }
}
```

In the dictionary we are defining the key as the command we want the drone to perform. So "right" can be used a key for example.  We can link a value to the key in the list, so like 80 in the example. 

As you can see in this dictionary, we have created multiple lists within our list. Doing this, allows us to use the same key name multiple times.  

The drone will perform the outcome of the example:

```
80 to the right
40 to the right
15 to the left
20 to the left
```

