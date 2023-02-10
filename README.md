# IMG_to_ASCII
A program that converts an image to ASCII art.

## Requirements
- Python 3.x
- Pillow library (pip install pillow)  
```python3 -m pip install --upgrade pip```   
```python3 -m pip install --upgrade Pillow```  

## Usage
- Run the program using ```python <filename>.py```
- Enter the path to the image file you want to convert.
- The ASCII art will be saved in a file named image.txt.

## How it works
- The program takes the path to an image file as input.
- It opens the image file using the Image module from the PIL library.
- The image is resized to 70x70 pixels.  
    It's possible to change, find line 22 ```image = image.resize((70, 70))```
    and remplace 70, 70 with the desired values. 1st value stands for width, and 2nd for height.  
- The image is then converted to greyscale using the to_greyscale function.
- The greyscale image is then converted to ASCII art using the pixel_to_ascii function. This function maps each pixel to an ASCII character from the ASCII_CHARS string.   
  - You can experiment with different characters or custom sets of characters to see how they affect the final output (line 3).
- The ASCII art string is split into lines based on the width of the original image.
- The ASCII art string is then saved to a file named image.txt.
