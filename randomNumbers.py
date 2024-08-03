import tkinter
import random

def rollagain():
    global randnum
    global smallest_num
    global biggest_num
    global min_num
    global max_num
    smallest_num = int(min_num.get())
    biggest_num = int(max_num.get())
    randnum.destroy()
    randnum = tkinter.Label(
    text=random.randint(smallest_num, biggest_num),
    foreground="black",
    background="gray",
    width=10,
    height=5,
    font=("Helvetica", 16))
    randnum.pack()

smallest_num = 1
biggest_num = 100

window = tkinter.Tk()
window.title("Random number generator Beta 2")
window.geometry("400x300")
rerollbutton = tkinter.Button(
    text="Re-roll", command=rollagain)
randnumtext = tkinter.Label(text="\n\nYour random number is: ")
randnum = tkinter.Label(
text=random.randint(smallest_num, biggest_num),
foreground="black",
background="gray",
width=10,
height=5,
font=("Helvetica", 16))
min_num_text = tkinter.Label(text="Select numbers between")
max_num_text = tkinter.Label(text="and")
min_num = tkinter.Entry()
max_num = tkinter.Entry()
min_num_text.pack()
min_num.pack()
max_num_text.pack()
max_num.pack()
randnumtext.pack()
rerollbutton.pack()
randnum.pack()
min_num.insert(0, "1")
max_num.insert(0, "100")

print("You can minimalize this window")
window.mainloop()

