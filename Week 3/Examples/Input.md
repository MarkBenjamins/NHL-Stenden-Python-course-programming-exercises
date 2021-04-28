 # Input

Python has several ways to have user input, it even has its own function to retrieve input from the console. 

Sometimes when you work with input, you have to continuously check if the user is doing something. If you have something that continuously checks something, you have to loop it. This is done with a while loop, like this;

```python
while True:
    # Your code that continuously checks something, like key presses.
```

## Input()

As mentioned before, Python has a function to retrieve the input on the console. The function is called the input function;

```python
input()
```

This essentially stops the program until the user provides input. Now we can use the input in a lot of ways, but as a simple example we will use it to provide a customized greeting message, as seen below:

```python
print('What is your name?')
name = input()
print('Hello, ' + name)
```

This is of course a simple example and you can do a lot more with the input function.

## Keyboard input

We can also detect keyboard input with Python. The function is not predefined in Python, so we have to import a library called keyboard. You can import a library for your project by opening the console in PyCharm, which is located at the bottom left of the screen. then we have to execute the following command:

```shell
pip3 install keyboard
```

This will install the library, now we have to import it in our code like this:

```python
import keyboard
```

Now we can use the functions that the library offers, for the input we will need the keyboard.is_pressed() function. This function requires the key you want to check as input and it will return true or false depending if the key is pressed. The following example prints 'You pressed q!' when you press the q key:

```python
import keyboard
while True:
    if keyboard.is_pressed('q'):
        print('You pressed q!')
```

The keyboard library has a lot of functions we don't need, but can be very useful. You can see al of the possibilities [here](https://github.com/boppreh/keyboard)