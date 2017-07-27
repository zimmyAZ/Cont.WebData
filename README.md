# Cont.WebData
----------------------
HomeBrew is required.

brew install...
    -python (program is written in pythin)
    -imagemagick (handles conversion)
    -ghostscript (handles PDF)
    -tesseract (grabs text from converted images)

----------------------
pdfHandler, as is, prompts user for the pdf file they wish to check, then prompts for the
location that the user would like to save the converted png files. It then takes that 
information and converts to output().png. It will then take those images and run them
through the neural net.
