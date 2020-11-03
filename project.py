import tkinter
from tkinter import Button
import webbrowser
window = tkinter.Tk()
window['bg']='grey'
window.wm_title("Number Form Convertor ")
window.wm_geometry('1080x900')
btn = Button(window, text = 'Quit :)', bd = '5', 
                         command = window.destroy, width=30 , height=10) 
#button = Button(window, text = 'Quit :)', bg='#ffffff', activebackground='#00ff00')  
#button.pack()  
  
#btn = Button(tkWindow, bg='red')
#tkinter.Screen().bgcolor("orange") 
btn.pack(side = 'bottom')      
Base_Number=""
new=1
url="https://www.tutorialspoint.com/basics_of_computers/basics_of_computers_number_system_conversion.htm"
def openweb():
    webbrowser.open(url,new=new)
Btn=Button(window,text="Explanation",command=openweb)
Btn.pack(side='bottom')

def evaluate(event):
    if Base_Number == "Binary":    #from binary to other
        try:
            dec = int(Myentry.get(),2)
            myhex = hex(dec)
            myoct = oct(dec)
            result1.configure(text = "Octal is: "+str(myoct))
            result2.configure(text = "Decimal is: "+str(dec))
            result3.configure(text = "Hex is: "+str(myhex))
            
        except ValueError:
            result1.configure(text = "Please enter valid binary")
            result2.configure(text = "")
            result3.configure(text = "")
            
    elif Base_Number == "Octal":          #from octal to other
        try:
            dec = int(Myentry.get(),8)
            myhex = hex(dec)
            mybin = bin(dec)
            result1.configure(text = "Decimal is: "+str(dec))
            result2.configure(text = "Hex is: "+str(myhex))
            result3.configure(text = "Binary is: "+str(mybin))
            
        except ValueError:
            result1.configure(text = "Please enter valid binary")
            result2.configure(text = "")
            result3.configure(text = "")
            
    elif Base_Number == "Decimal":          #from decimal to other
        try:
            dec = int(Myentry.get())
            mybin = bin(dec)
            myhex = hex(dec)
            myoct = oct(dec)
            result1.configure(text = "Binary is: "+str(mybin))
            result2.configure(text = "Octal is: "+str(myoct))
            result3.configure(text = "Hex is: "+str(myhex))
            
        except ValueError:
            result1.configure(text = "Please enter valid decimal")
            result2.configure(text = "")
            result3.configure(text = "")
            
    elif Base_Number == "Hex":           #from hexadecimal to other
        try:
            dec =int(Myentry.get(),16)
            mybin = bin(dec)
            myoct = oct(dec)
            result1.configure(text = "Decimal is: "+str(dec))
            result2.configure(text = "Binary is: "+str(mybin))
            result3.configure(text = "Octal is: "+str(myoct))
            
        except ValueError:
            result1.configure(text = "Please enter valid hexadecimal")
            result2.configure(text = "")
            result3.configure(text = "")
    else:
        result1.configure(text = "Please select a BASE!")
 
def calcStyle():
    global Base_Number
    Base_Number=base.get()
    print(base.get())
 
MyTitle = tkinter.Label(window, text="Number Convertor ")
MyTitle.pack()
 
Myentry = tkinter.Entry(window)
Myentry.bind("<Return>", evaluate)
Myentry.pack()
 
result1 = tkinter.Label(window, text="1. Choose a base")
result1.pack()
 
result2 = tkinter.Label(window, text="2. Enter a number ")
result2.pack()

result3 = tkinter.Label(window, text="3. Press<enter>")
result3.pack()
 
base = tkinter.StringVar()
tkinter.Radiobutton(window, text="Binary", variable=base, value="Binary", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Octal", variable=base, value="Octal", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Decimal", variable=base, value="Decimal", command=calcStyle).pack()
tkinter.Radiobutton(window, text="Hex", variable=base, value="Hex", command=calcStyle).pack()
 
window.mainloop()