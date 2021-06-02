# Executing Code

In this manual we will describe how you can execute your code on the drone.

Because actually establishing the connection with the drone is already quite advanced programming, we have simplified the work for you. 

### Import the Library

The first step you'll have to take, is importing the predefined python library file that is made ready for you.  This is done through the following command:

```python
import tello_code_execution.py
```

### Using the Library content

Now that the library is imported and setup, you'll have access to its functions. You'll now be able to send commands to the drone. This is done with the following command out the library.

```python
send_command("actual command")
```

Lets say you want to issue the command that will make the drone fly for 100 cm to the left. You can do this with the following command then.

```python
send_command("left 100")
```

Now you can implement this in your code and push your projects to the GitHub. The drone should be able to understand and execute your code. 

