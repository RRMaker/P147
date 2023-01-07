from tkinter import *
root = Tk()
root.title("ASCII Encrypted")
root.geometry("400x400")
root.configure(background = "green")
enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label = Label(root, text = "Name in ASCII : ", bg = "orange", fg = "white")
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label2 = Label(root, text = "Encrypted : ", bg = "blue", fg = "yellow")
label2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

def ASCII():
    input_word = enter_word.get()
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"] += str(chr(encrypted))
    
    
button = Button(root, text = "Show Name In ASCII and the Encrypted Name", bg = "purple", fg = "white", command = ASCII)
button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()