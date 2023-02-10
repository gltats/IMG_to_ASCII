from PIL import Image

ASCII_CHARS = "_++++++++++_"

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str

def main():
    path = input("Enter the path to the image fiel : \n")
    try:
        image = Image.open(path)
    except:
        print(path, "Unable to find image ")
    #resize image
    image = image.resize((70, 70))
    #convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    #save the string to a file
    with open("image.txt", "w") as f:
        f.write(ascii_img)
main()