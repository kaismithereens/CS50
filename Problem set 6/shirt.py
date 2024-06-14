"""
In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input
after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit,
per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
using default values for method, bleed, and centering, overlay the shirt with Image.paste,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
"""

from PIL import Image, ImageOps
import sys

def get_arguments():

    #check if the number of command-line arguments is 3: python code, input file name and output file name

    if len(sys.argv) == 3:
        my_input = sys.argv[1]
        my_output = sys.argv[2]
        return my_input, my_output
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def check_if_valid(file):

    #case-insensitive check if the name of the file is in valid format: jpg, jpeg or png

    if file.lower().endswith(".jpg") or file.lower().endswith(".png") or file.lower().endswith("jpeg"):
        return True
    else:
        return False

def check_if_the_same_format(i,o):

    #try to split the input file name and the output file name to get the file extension
    try:
        name_i, ext_i = i.split(".")
        name_o, ext_o = o.split(".")
    except ValueError:
        sys.exit("Can not split by .")

    #check if the file extension is the same for input and output files

    if ext_i.lower() == ext_o.lower():
        return True
    else:
        return False

def main():

    try:
        my_in_file, my_out_file = get_arguments()

        if check_if_valid(my_in_file) == False:
            sys.exit("Invalid input")

        if check_if_valid(my_out_file) == False:
            sys.exit("Invalid output")

        if check_if_the_same_format(my_in_file, my_out_file) == False:
            sys.exit("Input and output have different extensions")

        with Image.open(my_in_file) as im:

            with Image.open("shirt.png") as shirt:
                size = shirt.size
                b = ImageOps.fit(im, size, method= Image.Resampling.BICUBIC, bleed= 0.0, centering=(0.5, 0.5))
                b.paste(shirt,mask=shirt)
                #b2 = im.crop((0,0,im.width, im.width))
                b.save(my_out_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()

