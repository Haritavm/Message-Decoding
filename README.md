# Message-Decoding
The current file, main.py, appears to be part of a project named Message_decode. This file includes functionality for encoding a message using base64 encryption and displaying the encrypted message in a GUI. The GUI is built using the tkinter library.

-Key Components:
   1- Base64 Encoding:
      >  The message is encoded using base64.
      >  The encoded message is then converted to an ASCII string.
   2- GUI Elements:
      >  A label is created to display "Encrypted Message".
      >  A text box is created to display the encrypted message.
      >  Error messages are shown using messagebox.showerror if the provided key is incorrect or empty.
   3- Global Variables:
      >  screen, text1, and code are declared as global variables.
      
Functions:
    main_screen():
      > This function is intended to create the main screen of the application. However, the implementation details are not provided in the visible code.
Example Usage:
      > The user inputs a message and a key.
      > If the key is correct, the message is encrypted and displayed.
      > If the key is incorrect or empty, an error message is shown.
Dependencies:
      > tkinter: Used for creating the GUI.
      > base64: Used for encoding the message.
Notes:
     >  Ensure that the main_screen() function is properly implemented to initialize the GUI.
     >  Handle exceptions and edge cases for better user experience.
This documentation provides an overview of the functionality and structure of the main.py file in the Message_decode project.
