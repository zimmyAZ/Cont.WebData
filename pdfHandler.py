import tkFileDialog
import os


f = tkFileDialog.askopenfilename()
d = tkFileDialog.askdirectory()
command = ("convert " + f + " " + d + "/output.png")
DIR = ' + d + '
os.system(command)
images_converted = len(os.walk(d).next()[2])
