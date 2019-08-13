from tkinter import *
import maze0
import PIL
def main(event):
    img = img_entry.get()
    maze0.main(img)
    root.destroy()
root = Tk()
root.title('Maze')
root.geometry('300x300')
img_label = Label(root,text='Enter Image Name:')
img_entry = Entry(root)
img_button = Button(root,text='Submit')
img_button.bind('<Button-1>',main)
img_label.pack()
img_entry.pack()
img_button.pack()
root.mainloop()