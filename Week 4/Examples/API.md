# API manual

In this manual you will learn to use the API to get the data from the AI on the raspberry pi. we created a library with all of the functions, so you can just import the library and use the functions.

## Installing the library

the library can be installed like this

```powershell
pip install libraryVanThomasEnCody
```

## Using the library

Now you can use the functions in the library, there are a lot of different functions so you will always have what you need.

### Coordinates

```python
library.getCoords()
```

This functions return the coord from the API. The api gets this data directly from the drone camera and the AI

### functienaam

```python
library.getFrame()
```
This function returns the frame from the video stream. It returns it as a picture, with this picture you can do what you want.
