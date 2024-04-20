# Mini Projects in Python | Tikinter

## 1. Number Calculator
#### This is a Simple GUI calculator coded using Tkinter in Python 
#### [Code: calculator.py](https://github.com/akhilpsin/Python-Mini_projects/blob/master/Calculator/calculator.py)
### Algorithm
- Initially we Import everything from Tkinter using *.
- Next, Create an interface for the calculator.
- Next, Create buttons as input source that enters a number into the input field.
- Creat a function for clearing all element in the input field
- Creat a function for backspacing
- Create a function to perform equal to operation by evaluating input field
### Screenshot 
![Calculator Screenshot](https://github.com/akhilpsin/Python-Mini_projects/blob/master/Calculator/cal.PNG?raw=true)
---------------------------------------------------------------------------------------------------------------------------------------------------
## 2. QR Code generator
#### This is a Simple GUI QR code generator coded using Tkinter in Python 
#### [Code: Qr_code_generator.py](https://github.com/akhilpsin/Python-Mini_projects/blob/master/QR%20code%20generator/Qr_code_generator.py)
### Algorithm

- Initially we Import everything from Tkinter using * then import pyqrcode and finally ImageTk and Image from PIL
- Next, Create an interface/canvas for the labes, entry, botton and image.
- finally Creat a function for converting link to an image and view it on a button click.
### Screenshot 
![QR code generator Screenshot](https://github.com/akhilpsin/Python-Mini_projects/blob/master/QR%20code%20generator/OutputScreenShot.PNG?raw=true)
---------------------------------------------------------------------------------------------------------------------------------------------------
## 3. Video to ASCII Art
#### It is a simple python code to play videos in the terminal/cmd using characters as pixels
#### [Code: vid_asci_code.py ](https://github.com/akhilpsin/Python-Mini_projects/blob/master/Video%20to%20ASCI%20conversion/vid_asci_code.py)
### Algorithm

- Initially we Import required python libraries os, sys, cv2 and from PIL import Image
- initialise your characters to be seen in termina as a list (ASCII_CHARS - refer code)
- input the video to be processed 
- create a functions to resize and gray scale each frame of the video 
- create a functions to mapp each pixels from resized and grayscaled image and then allocate the ASCII character at those points
- create a functions to display ASCII image generated in cmd/terminal
### Screenshot 
![Video to ASCII Art Screenshot](https://github.com/akhilpsin/Python-Mini_projects/blob/master/Video%20to%20ASCI%20conversion/screenshot.PNG?raw=true)
---------------------------------------------------------------------------------------------------------------------------------------------------
## 4. Text to audio with python
### It is a simple python code to Convert Speech to Text Audio Mp3
#### [Code:Text_to_speech.py](https://github.com/akhilpsin/Python-Mini_projects/blob/master/Text_to_speach/Text_to_speech.py)
### Algorithm

- Import gTTS for text-to-speech functionality, os for system operations, and Tkinter for the GUI.
- Initialize the Tkinter window with a title and fixed dimensions.
- Create a text input field (Entry) and a "Convert To Audio" button (Button) on the GUI.
- Capture input text from the text field.
- Convert the text to speech using gTTS and save as an audio file.
- Play the audio file using the system's default media player.
### Screenshot 
![Video to ASCII Art Screenshot](https://github.com/akhilpsin/Python-Mini_projects/blob/master/Text_to_speach/UI_screenshot.PNG?raw=true)
