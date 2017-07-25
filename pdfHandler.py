import tkFileDialog
import os
import sys


def convert():
    print("Asking for PDF location.")
    f = tkFileDialog.askopenfilename()

    print("Checking file extension.")
    ext = os.path.splitext(f)[-1].lower()

    if ext != ".pdf":
        print("This is not a PDF file. Please check you the file you selected and run again.")
        sys.exit()

    print("Asking for conversion destination.")
    d = tkFileDialog.askdirectory()

    output_filename = raw_input("What would you like the name of the file to be? (Leave out extension) : ")

    command = ("convert " + f + " " + d + "/" + str(output_filename) + ".png")
    os.system(command)

    images_converted = len(os.walk(d).next()[2])
    test = str(os.walk(d).next()[2])

    print(test)
    print("PDF has been converted to " + str(images_converted) + " images.")
    print("Location : " + str(d) + "/")
    return d

convert()
