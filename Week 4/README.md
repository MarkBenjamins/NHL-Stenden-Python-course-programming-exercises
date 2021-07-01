# :pencil: Week 4 exercises 
This week we will learn the basics of artificial intelligence. We will try to connect to the drone through our library, to retrieve coordinates where the AI recognizes a traffic cone and to retrieve a frame from the camera. This week will prepare you for the end assignments. 

## Exercise 4

In this exercise you have to get a picture from the drone AI through the API. The API is used to get the data from the AI on the raspberry pi. We created a library with all of the functions, so you can just import the library and use the functions. Follow these step to use the API.

### Installing the library

First, you have to install the library from the commandline, like this:

```powershell
pip install connectionLibrary
```

### Using the library

Now you can use the functions in the library, we made two different functions. We made a function to retrieve the coordinates on the camera. We also made a second function to get the frame from the camera, as a picture.
first you have to import it, like this;
```python
import connectionLibrary
```

#### Coordinates

```python
library.getCoords()
```

This function returns the coordinates from the API. The API gets this data directly from the drone camera and the AI.

#### Frame

```python
library.getFrame()
```

This function returns the frame from the video stream. It returns it as a picture, with this picture you can do what you want.
