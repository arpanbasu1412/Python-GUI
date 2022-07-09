from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("544x655")
root.title("Calculator")
root.option_add('*Font', 'arial 20 bold')

# root.wm_iconbitmap("1.ico")
# root.wm_iconbitmap("https://d26tpo4cm8sb6k.cloudfront.net/icon-32x32.png")

# root.resizable(False,True)
# width, height
root.minsize(400,655)

# width, height
root.maxsize(650,655)

scvalue = StringVar()
scvalue.set("")
# screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen = Entry(root, relief=RIDGE, textvariable=scvalue,justify='right', bd=15, bg="powder blue")#font=('Arial', 12)
# screen.pack(fill=X, ipadx=8, pady=10, padx=10)
screen.pack(fill=X,side=TOP,ipady=10,pady=8)   
#expand=YES
f = Frame(root, bg="grey")
b = Button(f, text="9", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="6", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="3", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")

b = Button(f, text="-", padx=18, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=18, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="/", padx=19, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=11, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="c", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=19, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=15, pady=10, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=3)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()