# :pencil: Week 3 exercises 
This week we will use our experience with the simulation to fly with the real drone. 
We will perform some simple actions with the drone like flying, landing, flipping, and maneuvering in the air. 
Doing things like this will make us comfortable with flying the drone.
We will also learn how to fly the drone through the use of input commands. This will be done within the simulation environment.

## :closed_book: Exercise 3.1 Dictionary drone flight

The first exercise is to process the command below. This command is structured in a dictionary so we can see all of the options at once. For more information on dictionaries, you can consult the example. As shown by the commands in the dictionary below, every key can have a value. You can only use a key once. If you choose to use the same key again, it will overwrite the original key's value.

```python
command = {
    1: {
        'right': 0,
        'up': 0,
        'down': 0,
        'left': 0,
        'forward': 0,
        'back': 0,
        'flip': '', # direction to flip
        'cw': 0,
        'ccw': 0
    }
}
```

Your code should loop through the dictionary and execute according to the key and value pair. If the key is 'forward' and the value is 80, the drone should go forward by 80.

You can expand the dictionary with other commands, like this:

```python
commandsDict = {
    1: {'right': 80},
    2: {'up': 10},
    3: {'down': 100},
    4: {'left': 80},
    5: {'forward': 80},
    6: {'back': 80},
    7: {'flip': 'r'},
    8: {'cw': 80},
    9: {'ccw': 80}
}
```

Your code should preform the commands in this dictionary. 

## :no_entry_sign: Exercise 3.2 Error prevention 

In this exercise we will expand our code from the last assignment. 
You will perform some error prevention so the drone does not crash into the ground or ceiling. 
You should also stop the code from running if the value is 0 or less.

So make sure the following requirements are met:
- Code commands with a value of 0 or less cannot be executed.
- The drone is not allowed to go higher than 200 cm.
- The done cannot go further than 200 cm at once.
- Validate if the down command is possible with the current height of the drone.
- Validate if the up command is possible with the current height of the drone.

## :cl: Exercise 3.3 Commands through input

In this exercise we will be sending commands to the simulation through the use of real-time inputs. 
For further explanation, observe the [example](/Week%203/Examples/Input.md) provided in the examples folder. 
This exercise will consist of two parts.

### Part One:

For the first part of the exercise, you will need to create a program that allows commands to be written within the command line. 

- You should be capable of moving the drone through the simulation while the application is running. 

### Part Two:

For the second part of the exercise, you will need to remodel the program so that the commands will be send by use of keyboard inputs. 

- You should be capable of moving the drone with only your keyboard through the simulation while the application is running.

## :helicopter: Exercise 3.4 The real drone

In this exercise we are going to upload our code to the real drone, this is done through the Jenkins pipeline. For an explanation on how this is done, please visit [this](/Week%203/Examples/DroneConnection.md) example. 

>**Important** *When working with the real drone, contrary to the simulation, the drone does not preform the operations very precise. This is because of a lot of external factors like battery power, wind, air pressure, etc. The drone is very fragile, so it is important that it does not crash. With all of the previously mentioned external factors, you should **always** be careful when flying the drone or when you are making it fly with your code.*

We are going to edit our code from the first two exercises so it works with the real drone. This is fairly easy, as the structure of the code does not have to change. We have prepared predefined functions you can import and use, this way the very complicated stuff is already done. You can look at the library with the predefined functions [here](), and there is an explanation on how to use them in [this]() manual.

The drone should fly according to the dictionary, just like in the first exercise. It should also implement the error prevention from the second exercise.