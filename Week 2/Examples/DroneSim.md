# How to use the simulator

***To use the simulator we first have to obtain it, how to do this is described in the [manual](/Week%202/Manual%20Simulation/README.md).***

## :earth_africa: Creation
First we have to create the drone, this is done by importing the required library and assigning a variable as shown below;

```python
from tello_sim import Simulator

drone = Simulator()
```

This will show the following output;

```
Hi! My name is TelloSim and I am your training drone.
I help you try out your flight plan before sending it to a real Tello.
I am now ready to take off. 🚁
I am running your "command" command.
```

## :rocket: Takeoff
As we can see the drone is ready to take off;

```python
drone.takeoff()
```

This will show the following output;

```
Get ready for takeoff!
I am running your "takeoff" command.
My estimated takeoff altitude is 81 centimeters
```

Now the drone is ready to fly and we can preform several commands.

## :airplane: Flying commands
There are several commands to fly in the air, we have separated them in four categories.

### :left_right_arrow: Horizontal flying
We can use the forward command to fly forward, the back command to fly backwards, the right command to fly to the right and the left command to fly to the left, all in centimeters.

```python
drone.forward(40)
drone.back(40)
drone.right(40)
drone.left(40)
```

### :arrow_up_down: Vertical flying
We can use the up and down commands to change the drone's altitude, in centimeters.

```python
drone.up(40)
drone.down(40)
```

The drone can also preform a flip operation so it makes a loop in the air, in the direction you choose.

```python
direction = "f"
# "f" to flip forward, "b" to flip backward, "r" to flip to the right and "l" to flip to the left.
drone.flip(direction)
```

### :arrows_counterclockwise: Turning
We can use the cw command to turn clockwise and the ccw command to turn counterclockwise, in amount of degrees.

```python
drone.cw(90)
drone.ccw(90)
```

### :floppy_disk: Data
We can also retrieve data like positions with the following commands;

```python
# Return the current altitude.
drone.altitude

# Return the current rotation.
drone.bearing

# Return the current location(X,Y).
drone.cur_loc

# Return all of the different altitudes.
drone.altitude_data

# Return all of the different locations.
drone.path_coors

# Return the locations where the drone flipped.
drone.flip_coors

# Return a list of all the commands executed.
drone.command_log
```

## :chart_with_upwards_trend: Graph
When you execute a movement command the drone simulator will create a graph where you can see the path the drone followed, here are some examples;

### vertical

<img src="/Media/verGraph.png" width="400"/>

### horizontal

<img src="/Media/horGraph.png" width="400"/>