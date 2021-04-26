# :pencil: Week 3 exercises 
This week we will use our experience with the simulation to fly with the real drone. 
We will preform some simple actions with the drone like flying, landing, flipping, and maneuvering in the air. 
Doing thinks like this will make us comfortable with flying the drone.

## :gear: Drone connection setup

## Exercise 3.1

The first exercise is to process the following command, this command is structured in a dictionary so we see all of the options at once. For more information on dictionaries, you can consult the example.

```python
command = {
    1: {
        'right': 80,
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

Your code should loop through the dictionary and execute according to the key and value. if the key is 'right' and the value is 80, the drone should go 80 to the right.

If your code implements all of the different commands, you can expand the dictionary with other commands, like this;

```python
commandsDict = {
    1: {'right': 80, 'up': 0, 'down': 0, 'left': 0, 'forward': 0, 'back': 0, 'flip': '', 'cw': 0, 'ccw': 0},
    2: {'right': 0, 'up': 80, 'down': 0, 'left': 0, 'forward': 0, 'back': 0, 'flip': '', 'cw': 0, 'ccw': 0},
    3: {'right': 0, 'up': 0, 'down': 80, 'left': 0, 'forward': 0, 'back': 0, 'flip': '', 'cw': 0, 'ccw': 0},
    4: {'right': 0, 'up': 0, 'down': 0, 'left': 80, 'forward': 0, 'back': 0, 'flip': '', 'cw': 0, 'ccw': 0},
    5: {'right': 0, 'up': 0, 'down': 0, 'left': 0, 'forward': 80, 'back': 0, 'flip': '', 'cw': 0, 'ccw': 0},
    6: {'right': 0, 'up': 0, 'down': 0, 'left': 0, 'forward': 0, 'back': 80, 'flip': '', 'cw': 0, 'ccw': 0},
    7: {'right': 0, 'up': 0, 'down': 0, 'left': 0, 'forward': 0, 'back': 0, 'flip': 'r', 'cw': 0, 'ccw': 0},
    8: {'right': 0, 'up': 0, 'down': 0, 'left': 0, 'forward': 0, 'back': 0, 'flip': '', 'cw': 80, 'ccw': 0},
    9: {'right': 0, 'up': 0, 'down': 0, 'left': 0, 'forward': 0, 'back': 0, 'flip': '', 'cw': 0, 'ccw': 80}
}
```

Your code should preform the commands in this dictionary. You should try to stop the command from running if it the value is 0.

## Exercise 3.2

In this exercise we will expand our code from the last assignment. We will preform some error handling so the drone does not crash into the ground.
