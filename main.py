from tkinter import *
from PIL import ImageTk, Image  #PIL -> pillow
import pymysql
from tkinter import messagebox
from Addbook import *
from DeleteBooks import *
from IssueBook import *
from ReturnBook import *
from ViewBooks import *


# Connecting to MYSql Server

mypass = "password" # Use your own password
mydatabase = "db"  # The database name

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()  # cur -> cursor

# Designing the window

root = Tk()
root.title("Library Management")
root.minsize(width=400,height=400)
root.maxsize(width=1024,height=900)
root.geometry("600x500")

same=True
n=0.72

# Adding a background image
background_image =Image.open("library.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

# Setting up the Head Frame
headingFrame1 = Frame(root,bg="grey",bd=3)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome To MegaMind Library", bg="silver", fg="white", font=('Courier',15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


# Adding the Buttons
btn1 = Button(root, text="Add Book Detail", bg="black", fg="white", command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg="black", fg="white", command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg="black", fg="white", command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book To Student", bg="black", fg="white", command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg="black", fg="white", command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()
