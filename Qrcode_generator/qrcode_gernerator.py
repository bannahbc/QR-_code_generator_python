import qrcode,PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk,filedialog,messagebox


window=tk.Tk()
window.title("QR CODE Generator")
window.geometry("300x380")
window.resizable(0,0)
window.config(bg="beige")

def createQR(*args) :
    data=text_entry.get()

    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280,250))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0,0,anchor=tk.NW,image=tkimage)
        qr_canvas.image = tkimage
    else:
           messagebox.showwarning("Error","Enter some Data First" )

def saveQR() :
    data=text_entry.get()

    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280,250))
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
           resized_img.save(path)
           messagebox.showinfo("sucess","QR Code is Saved")
        else:
           messagebox.showwarning("Error","Enter some Data First" )

#frames
frame1=tk.Frame(window,bd=2,relief=tk.RAISED)
frame1.place(x=10,y=0,width=280,height=250)

frame2=tk.Frame(window,bd=2,relief=tk.SUNKEN)
frame2.place(x=10,y=260,width=280,height=100)

cover_img = tk.PhotoImage(file="Big.Buck.Bunny.-.Opening.Screen.png")

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0,anchor=tk.NW,image=cover_img)
qr_canvas.image=cover_img
qr_canvas.bind("<Double-1>",saveQR)
qr_canvas.pack(fill=tk.BOTH)

text_entry=ttk.Entry(frame2,width=26,font=("ariel",11),justify=tk.CENTER)
text_entry.place(x=20,y=5)

btn1=ttk.Button(frame2,text="CREATE",width=10,command=createQR)
btn1.place(x=25,y=50)

btn2=ttk.Button(frame2,text="SAVE",width=10,command=saveQR)
btn2.place(x=100,y=50)

btn3=ttk.Button(frame2,text="EXIT",width=10,command=window.quit)
btn3.place(x=175,y=50)


window.mainloop()

