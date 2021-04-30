# :pencil: Week 1 exercises 
This week we will learn very basic Python functions and write simple programs. 
We will learn to write to the console, use variables and use simple loops. 
We will also install Python and set up the development environment.

## :gear: Developer setup
- Run the installer and follow the on-screen instructions [installing Python](https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe)
- Create a student account by filling in the [form](https://www.jetbrains.com/shop/eform/students?_st=phGZYaLDwIFGzailE1uoJf-YSAMxYl0W9cCb_fmXojmwSBZwGwGLnwzHtxOrCGvc)
- After this, select PyCharm out of the options and click on [download](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows)

## :wave: Exercise 1.1 Hello World
For the exercise we will start with setting up the environment. 
You will start by creating a new project  within PyCharm. 
Next you create a new Python file in which you'll write your code. 
When you are done with your code, you'll run it to see if it works. 
For additional explanation, consult the gif below.

For more information go to [this website](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html) 

![Gif](/Media/Python_gif_1.gif)

As stated in the title, this exercise revolves around the words "Hello World". 
The objective of this exercise is to be print out the "Hello World" text within your editor. 
To clear the exercise, a few checkpoints have to be reached.

- A new project has to be made, named "Exercises Week 1".
- A new Python file has to be made, named "Hello World".
- Once run, "Hello World" should be printed out.

## :package: Exercise 1.2 Variables
In this exercise we will start using variables. You should already have some experience with variables. 
In the [examples folder](/Week%201/Examples) you will find useful information that should aid you through this exercise.

The first exercise is to assign something to the variable and print out the following phrase:

```python
filler_text =

print("The Ducks follow", filler_text, "across the road.")

expected output: The Ducks follow their mother across the road
```

The second exercise is get the defined output by means of adding and subtracting the variables together:

```python
x = 7
y = 8
z = 5

expected output: 6
```

The third exercise is to get the defined outputs through using different operations:

```python
# Calculate the square value.
a = 5

expected output: 25

# Calculate the rest value.
c = 10
d = 3

expected output = 1

# Calculate the root value.
e = 36

expected output = 6
```

The last exercise is to convert the variable number from Celsius to Fahrenheit. 
You are expected to handle the errors through the use of an if-else statement:  

```python
temperature_number = 20

expected output if success: 68

expected output if failed: The conversion was preformed incorrectly.
```



## :repeat: Exercise 1.3 Loops

In this exercise we will use some loops in Python. 
You already learned how loops work with the PHP Lessons, so this should not be too hard. 
In Python loops are very similar, the main difference is that they are declared differently. 
In the [examples folder](/Week%201/Examples) you will find some useful examples on how the [loops](/Week%201/Examples/Loops.md) in Python work.

The first assignment is to print this with a while loop:

```python
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
```

Just like in PHP, you can also use loops in loops.

The next assignment is to print this with a for loop:

```python
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

You can also loop through lists, an list is a variable that contains multiple other variables.

The last assignment is to loop through the given list with a for(each) loop:

```python
countries = ['Netherlands', 'Denmark', 'Germany', 'Belgium', 'France', 'Sweden']
```

First try to print every country in this list in order, from left to right. The output will be:

```
Netherlands 
Denmark 
Germany 
Belgium 
France 
Sweden 
```

Now try to print every country in reverse order, from right to left. You can use a loop of your choice. The output will be:

```
Sweden 
France 
Belgium 
Germany 
Denmark 
Netherlands
```
