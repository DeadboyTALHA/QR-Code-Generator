from tkinter import *
import qrcode

fun = Tk()
fun.title("Talha's QR Code Generator")
fun.geometry("1000x550")
fun.config(bg = "#AE2321")
fun.resizable(False, False)

def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("qrs/" + str(name) + ".png")
    
    global Image
    Image = PhotoImage(file = "qrs/" + str(name) + ".png")
    Image_view.config(image = Image)

Image_view = Label(fun, bg = "#AE2321")
Image_view.pack(padx = 50, pady = 10, side = RIGHT)

Label(fun, text = "Title", fg = "white", bg = "#AE2321", font = 15).place(x = 50, y = 170)

title = Entry(fun, width = 13, font = "Arial 15")
title.place(x = 50, y = 200)

entry = Entry(fun, width = 28, font = "Arial 15")
entry.place(x = 50, y = 250)

Button(fun, text = "Generate", width = 20, height = 2, bg = "black", fg = "white", command = generate).place(x = 50, y = 300)

fun.mainloop()