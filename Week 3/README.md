# :pencil: Week 3 exercises 
This week we will use our experience with the simulation to fly with the real drone. 
We will preform some simple actions with the drone like flying, landing, flipping, and maneuvering in the air. 
Doing thinks like this will make us comfortable with flying the drone.

## :gear: Drone connection setup

## Exercise 3.1 Directory Drone Flight

The first exercise is to process the following command, this command is structured in a dictionary so we see all of the options at once. For more information on dictionaries, you can consult the example. You can see a command in the dictionary here, every key can have a value. You can only use a key once, if you use that key again, it will overwrite the original key's value.

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

You can expand the dictionary with other commands, like this;

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

## Exercise 3.2 Error prevention 

In this exercise we will expand our code from the last assignment. 
You will perform some error prevention so the drone does not crash into the ground. 
You should also stop the code from running if the value is 0 or less.

So make sure the following requirements are met:
- Code commands with a value of 0 or less can't be executed.
- Validate if the down command is possible with the current height of the drone.
