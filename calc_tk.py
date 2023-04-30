import tkinter as tk
window = tk.Tk()
window.title("SIMPLE CALCULATOR")
window.geometry("350x400")
window.resizable(0,0)
window.config(bg ="#c75c5c" )

operation = ""
def disable():
    if "." in entry_widget.get():
        decimal_button.config(state="disabled")

def operate(param):
    global operation
    operation = operation + str(param)
    entry_widget.delete("0", "end")
    entry_widget.insert("0", operation)

def inverse(param):
    global operation

    operation = operation + str( param)
    operate( "/")
    
def equals():
    global operation
    if "0" in entry_widget.get():
        result = "Error"
        entry_widget.delete("0", "end")
        entry_widget.insert("0", result)
    else:
        result = eval((operation))
        entry_widget.delete("0", "end")
        entry_widget.insert("0", result)

def square():
    global operation
    operation = entry_widget.get()
    #operation = operation + str(100)
    print(operation)
    operation = ((float(operation))**2)
    entry_widget.delete("0", "end")
    entry_widget.insert("0", operation)

def clears():
    global operation 
    operation = ""
    entry_widget.delete("0", "end")

#creating the frames
#i didn't specify how long or wide i want the two frames to be in the entry sticky = "we" pulls it right from the beginning
# to the end of the whole parent window then ipadx and ipady to increase the button size
display_frame= tk.Frame(window)
button_frame= tk.Frame(window)

# display_frame.pack(padx=(30,0),0))
# button_frame.pack(padx=20,pady=(0,20))

display_frame.pack(padx=5, pady=(10,10))
button_frame.pack(padx=1,pady=(0,5))

#THe child entry widget
#how will i know that width 50 is actually going to fill the first frame 
entry_widget = tk.Entry(display_frame, width=50, borderwidth=5)
entry_widget.pack(ipadx=5, ipady=15)


#Second child button widget
clear_button = tk.Button(button_frame, text= "C", font = ("Cambria, 15"), bg= "grey", command=clears)
inverse_button = tk.Button(button_frame, text= "1/x", bg = "grey",font = ("Cambria, 15"), command=lambda:inverse(1))
exponent_button= tk.Button(button_frame, text= "x^n", bg = "grey",font = ("Cambria, 15"), command=lambda:operate("**"))
divide_button = tk.Button(button_frame, text= "/", bg = "grey",font = ("Cambria, 15"), command=lambda:operate("/"))
num7_button = tk.Button(button_frame, text= "7", bg = "white",font = ("Cambria, 15"), command=lambda:operate(7))
num8_button = tk.Button(button_frame, text= "8", bg = "white",font = ("Cambria, 15"), command=lambda:operate(8))
frame_label7 = tk.Button(button_frame, text= "9", bg = "white",font = ("Cambria, 15"),command=lambda:operate(9))
multiply_button = tk.Button(button_frame, text= "*", bg = "grey",font = ("Cambria, 15"), command=lambda:operate("*"))
num4_button = tk.Button(button_frame, text= "4", bg = "white",font = ("Cambria, 15"), command=lambda:operate(4))
num5_button = tk.Button(button_frame, text= "5", bg = "white",font = ("Cambria, 15"), command=lambda:operate(5))
num6_button = tk.Button(button_frame, text= "6", bg = "white",font = ("Cambria, 15"), command=lambda:operate(6))
substract_button = tk.Button(button_frame, text= "-", bg = "grey",font = ("Cambria, 15"), command=lambda:operate("-"))
num1_button = tk.Button(button_frame, text= "1", bg = "white",font = ("Cambria, 15"),command=lambda:operate(1))
num2_button = tk.Button(button_frame, text= "2", bg = "white",font = ("Cambria, 15"),command=lambda:operate(2))
num3_button = tk.Button(button_frame, text= "3", bg = "white",font = ("Cambria, 15"),command=lambda:operate(3))
add_button = tk.Button(button_frame, text= "+", bg = "grey",font = ("Cambria, 15"), command=lambda:operate("+"))
square_button = tk.Button(button_frame, text= "x^2", bg = "grey",font = ("Cambria, 15"), command=square)
num0_button = tk.Button(button_frame, text= "0", bg = "grey",font = ("Cambria, 15"),command=lambda:operate(0))
decimal_button = tk.Button(button_frame, text= ".", bg = "grey",font = ("Cambria, 15"),command=lambda:operate("."))
equals_button = tk.Button(button_frame, text= "=", bg = "grey",font = ("Cambria, 15"), command=equals)
#display to the screen row1
clear_button.grid(row=0, column=0, pady = 1, sticky="WE", ipadx=20, ipady= 10)
inverse_button.grid(row=0, column=1, pady= 1, sticky="WE",ipadx=20,ipady= 10)
exponent_button.grid(row=0, column=3, pady=1, sticky="WE",ipadx=20,ipady= 10)
divide_button.grid(row=4, column=0,pady=1, sticky="WE",ipadx=20,ipady= 10)
# diplay row2 to the child widget
num7_button.grid(row=1, column=0, sticky="WE", ipadx=20,ipady= 10)
num8_button.grid(row=1, column=1, sticky="WE", ipadx=20,ipady= 10)
frame_label7.grid(row=1, column=2, sticky="WE", ipadx=20,ipady= 10)
multiply_button.grid(row=1, column=3, sticky="WE", ipadx=20,ipady= 10)

#display row3 in the child widget row 3
num4_button.grid(row=2, column=0, sticky="WE", ipadx=20,ipady= 10)
num5_button.grid(row=2, column=1, sticky="WE", ipadx=20,ipady= 10)
num6_button.grid(row=2, column=2, sticky="WE", ipadx=20,ipady= 10)
substract_button.grid(row=2, column=3, sticky="WE", ipadx=20,ipady= 10)
#display row4  in the child widget row 4
num1_button.grid(row=3, column=0, sticky="WE", ipadx=20,ipady= 10)
num2_button.grid(row=3, column=1, sticky="WE", ipadx=20,ipady= 10)
num3_button.grid(row=3, column=2, sticky="WE", ipadx=20,ipady= 10)
add_button.grid(row=3, column=3, sticky="WE", ipadx=20,ipady= 10)
#display row4 in the child widget 
square_button.grid(row=0, column=2, sticky="WE", ipadx=20,ipady= 10)
num0_button.grid(row=4, column=1, sticky="WE", ipadx=20,ipady= 10)
decimal_button.grid(row=4, column=2, sticky="WE", ipadx=20,ipady= 10)
equals_button.grid(row=4, column=3, sticky="WE", ipadx=20,ipady= 10)






window.mainloop()
