import tkFileDialog
import os
import sys
import glob




def convert():
    print("Asking for PDF location.")
    f = tkFileDialog.askopenfilename()
    print("Checking file extension.")
    ext = os.path.splitext(f)[-1].lower()
    files = []

    if ext != ".pdf":
        print("This is not a PDF file. Please check you the file you selected and run again.")
        sys.exit()
    print("Asking for conversion destination.")
    d = tkFileDialog.askdirectory()
    output_filename = raw_input("What would you like the name of the file to be? (Leave out extension) : ")
    print("Running PDF to PNG conversion.")
    command = ("convert -verbose -density 300 " + f + " " + d + "/" + str(output_filename) + ".png")
    os.system(command)
    os.system("mkdir " + str(d) + "/resampled")
    print("Created /resampled")

    images_converted = len(os.walk(d).next()[2])
    resampled = (str(d) + "/resampled/")
    os.chdir(d)
    dirs = glob.glob("*.png")
    print("Added files to list")
    print("PDF has been converted to " + str(images_converted) + " images.")
    print("Location : " + str(d) + "/")
    i = 0
    for names in range(images_converted-1):
        print ("Pulling text from image #" + str(names))
      #  print("convert -verbose -units PixelsPerInch " + str(d) + "/" + output_filename + "-" + str(i) + ".png" + " -resample 300 " + resampled + str(dirs[i]))
        os.system("convert -verbose -units PixelsPerInch " + str(d) + "/" + output_filename + "-" + str(i) + ".png" + " -resample 300 " + resampled + output_filename + "-" + str(i))
      #  print("tesseract " + resampled + output_filename + "-" + str(i) + ".png" + " " + resampled + "output" + str(i))
        os.system("tesseract " + resampled + output_filename + "-" + str(i) + ".png" + " " + resampled + "output" + str(i))
        i += 1
    print("Deleting Lower DPI Images")
    os.system("rm " + str(d) + "/*.png")
    print("Finished")
convert()
