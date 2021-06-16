# Executing Code

In this manual we will describe how you can execute your code on the drone.

Because actually establishing the connection with the drone is already quite advanced programming, we have simplified the work for you. 

## :closed_book:Import the Library

The first step you'll have to take, is importing the predefined python library file that is made ready for you.  This is done through the following command:

```python
import tello_code_execution as tello
```

## :open_file_folder:Using the Library content

Now that the library is imported and setup, you'll have access to its functions. In order to connect to the drone, first write the following method call:

```python
tello.connect()
```

You'll now be able to send commands to the drone. This is done with the following command from within the library:

```python
tello.send_command("actual command")
```

Lets say you want to issue the command that will make the drone fly for 100 cm to the left. You can do this with the following command:

```python
tello.send_command("left 100")
```
There are a lot of commands the drone is able to execute, so here is a list that contains all of them:

  - ```takeoff (this command must always be executed first)```
  - ```land (this command must always be executed last)```
  - ```flip { UP | DOWN | R | L }```
  - ```forward { units in CM }```
  - ```back { units in CM }```
  - ```left { units in CM }```
  - ```right { units in CM }```
  - ```up { units in CM }```
  - ```down { units in CM }```
  - ```cw { degrees to rotate }```
  - ```ccw { degrees to rotate }```
  - ```speed { ... }```
  - ```speed?```

When your code has been executed it's necessary to disconnect from the drone, simply writing the following method call will do the work:

```python
tello.disconnect()
```

Now you can implement this in your code and push your projects to the GitHub. The drone should be able to understand and execute your code. 

