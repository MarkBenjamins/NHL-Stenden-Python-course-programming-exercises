# :pencil: Week 2 exercises 
This week we will learn to use a simulation that simulates the DJI Tello drone, using this simulation we will simulate some simple movements with the drone. 

## :gear: Simulation setup
To use the simulation, you'll need to download an library.

You will accomplice this through the command lines within PyCharm.

1. Open the terminal within your PyCharm Application.

Next you will need to clone the git directory from the simulation.

2. Run the command  `git clone https://github.com/Fireline-Science/tello_sim`

Lastly you will to locate the file directory and install it.

3. Run the command `cd tello_sim`
4. Run the command `pip install .`

For more information go to [the tello_sim GitHub](https://github.com/Fireline-Science/tello_sim)

## Exercise 2.1 Square
In the first exercise we fly a simple square in our simulation. 
You are expected to get the following output as result.

<img src="/Media/Exercise%202.1%20Week%202.png" width="300"/>

## Exercise 2.2 Shape
In this exercise we will use the simulation to draw shapes, your job it to replicate the following shapes for the Horizontal movement.

<img src="/Media/horGraph.png" width="300"/>

You also have to replicate the following vertical shape, edit you code so it does both at the same time.

<img src="/Media/verGraph.png" width="300"/>

## Exercise 2.3 Circle
In this exercise we will use a for loop to create circles. Try to recreate the following shape with a nested for loop.

<img src="/Media/LoopShape.png" width="300"/>

Use the following turns with degrees.

<img src="/Media/angle's.png" width="300"/>

## Exercise 2.4 Maze

In this exercise your goal is to get through the maze and reach the end goal. This maze is designed so it will simulate a real life environment.

The blue marker will be your starting point. 

You need to simulate the drone so it will reach the green marker (the end goal) without touching any black walls. Envision all the black parts as walls in real life. 
You wouldn't want to fly the drone against those walls.

You will also notice there are some red and purple markers on the map. 
Red will be the indicator that the drone needs to reach a certain higher altitude. 
Purple on the other hand, will indicate that the drone needs to reach a lower altitude. 
These requirements need to be met, before its allowed to continue.

By the red markers the drone should have reached an altitude of 120 cm.

By the purple marker the drone should have dropped to an altitude of 60 cm.

The size of one square on the map is 50 cm long by 40 cm wide.

<img src="/Media/MazeExercise.png" width="300"/>