# import required libirary
from tkinter import *
from pip import PyDictionary
# Create Object
dictionary = PyDictionary()
root = Tk()
#Set geometry
root.geomentry("400x400")

def dict(): 
    meaning.config(text=dictionary.meaning(word.get())['None'][0])
    
    synonym.config(text=dictionary.synonym(word.get()))
    
    antonym.config(text=dictionary.antonym(word.get()))
    
# Add Labels, Button and Frames

Label(root, text="Dictionary",font=("Helvetica 20 bold"), ffg="Green").pack(pady=10)

# Frames 1
frame = Frame(root)
Label(frame, txt="Type word", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))

word.pack()
frame.pack(pady=10)

#Frame 2
frame1 = Frame(root)
Label(frame1, text="Meaning:-", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)
# Frame 3
frame2 = Frame(root)
Label(frame2, text="Synonyms:- ", font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 10 bold"))
synonym.pack()
frame2.pack(pady=10)
# Frame 4
frame3 = Frame(root)
Label(frame3, text="Antonym:-", font=("Helvetica 10 bold"))
antonym = Label(frame3, text="", font=("Helvetica 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)
Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict).pack()
#Execute Tkinter
root.mainloop()

