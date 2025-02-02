from tkinter import *
from tkinter import messagebox
import base64
import os

# Decrypt function
def decrypt():
    password = code.get() # Get the key

    if password == "1234": # Check if the key is correct
        screen2=Toplevel(screen)    # Create a new window
        screen2.title("Decryption") # Set the title of the new window
        screen2.geometry("400x200") # Set the size of the new window
        screen2.configure(bg="light blue") # Set the background color of the new window

        message=text1.get("1.0",END) # Get the encrypted message from the text box
        message=message.encode("ascii") # Convert the message to bytes
        base64_bytes=base64.b64decode(message) # Decrypt the message using base64
        decryped_message=base64_bytes.decode("ascii") # Decrypt the message using base64


        Label(screen2,text="Decrypted Message",bg="light blue",fg="white",font=("Arial",15)).pack()    # Create a label
        text2=Text(screen2,font=("Arial",15),bg="white",relief=GROOVE,bd=1,wrap=WORD)
        text2.place(x=10,y=50,width=380,height=100)

        text2.insert(END,decryped_message) # Insert the decrypted message into the text box

    elif password != "1234": # Check if the key is incorrect
        messagebox.showerror("Error","Invalid Key")

    elif password == "":
        messagebox.showerror("Error","Key is empty")

# Encrypt function
def encrypt():
    password = code.get() # Get the key

    if password == "1234": # Check if the key is correct
        screen1=Toplevel(screen) # Create a new window
        screen1.title("Encryption") # Set the title of the window
        screen1.geometry("400x200") # Set the size of the window
        screen1.configure(bg="#0066cc") # Set the background color of the window

        message=text1.get("1.0",END) # Get the text from the input field
        message=message.encode("ascii") # Convert the text to bytes
        base64_bytes=base64.b64encode(message) # Encrypt the text using base64
        encrypted_message=base64_bytes.decode("ascii") # Convert the encrypted bytes to text


        Label(screen1,text="Encrypted Message",bg="white",fg="#0066cc",font=("Arial",15)).pack()    # Create a label
        text2=Text(screen1,font=("Arial",15),bg="white",relief=GROOVE,bd=1,wrap=WORD)
        text2.place(x=10,y=50,width=380,height=100)

        text2.insert(END,encrypted_message)  # Insert the encrypted message into the text box

    elif password != "1234": # Check if the key is incorrect
        messagebox.showerror("Error","Invalid Key") 

    elif password == "":
        messagebox.showerror("Error","Key is empty")

# Create main screen
def main_screen():


# Make the variables global
    global screen 
    global text1
    global code


    screen = Tk()
    screen.geometry("500x500")  # Set window size
    screen.title("Cypher App") # Set window title
    screen.configure(bg="lightyellow")  # Set background color

    # Set application icon
    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)


    # Function to reset the text input and key
    def reset():
        code.set("")
        text1.delete(1.0, END)


    # Label for text input
    Label(text="Enter text for Encryption and Decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)

    # Textbox for input
    text1 = Text(font=("Arial", 14), bg="white", relief=GROOVE, wrap=WORD, bd=1)
    text1.place(x=10, y=40, width=480, height=120)  # Adjusted width and height

    # Label for encryption key input
    Label(text="Enter key for Encryption and Decryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)

    # Key entry field
    code = StringVar()
    key = Entry(textvariable=code, font=("Arial", 18), width=22, show="*", bg="white", relief=GROOVE, bd=1)
    key.place(x=10, y=200)

    # Buttons for Encrypt, Decrypt, and Reset
    Button(text="ENCRYPT", height=2, width=23, bg="#0066cc", bd=0,command=encrypt, font=("Calibri", 13)).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="light blue", bd=0,command=decrypt, font=("Calibri", 13)).place(x=260, y=250)
    Button(text="RESET", height=2, width=50, bg="peach puff", bd=0, command=reset, font=("Calibri", 13)).place(x=10, y=320)

    # Run the application
    screen.mainloop()


main_screen()
