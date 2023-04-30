import tkinter as tk
#from tkinter import delete
window = tk.Tk()
window.title("Hello GUI World")
window.geometry("500x500")
window.resizable(0,0)


var = tk.StringVar()
var.set("none")

###########i do not want to the write that default keep learning tkinter, how do i do it??????

#define function
def submit_name():
    """
    print to the output frame in either upper case or normal
    """
    if var.get() == "normal":
        name_label = tk.Label(output_frame, text = ("Hello " + name_entry.get() + " Keep learning Tkinter"), bg= colorf1)

    else:
        name_label = tk.Label(output_frame, text =("Hello " + name_entry.get() +" Keep learning Tkinter").upper(), bg= colorf2)
    name_label.pack()
    #print(name_label)

    #to delete the name after submitting
    name_entry.delete(0, "end")


colorb = "#224870"
colorf1= "#2a4494"
colorf2 = "#4ea5d9"

#backg = tk.Label(window, bg= colorb).pack(fill="both", expand= True)
window.config(bg=colorb)
#defining frames 
input_frame = tk.Frame(window, bg=colorf1, height=100, width= 400)
output_frame = tk.Frame(window, bg=colorf2, height=300, width=500)
input_frame.pack_propagate(0)
output_frame.pack_propagate(0)

#packing to the window
input_pack = input_frame.pack( pady=10, ipady=5)
output_pack = output_frame.pack(padx=10, pady=(0,10), fill="both", expand= True)


#name entry
name_entry = tk.Entry(input_frame, text= "Enter your name", width= 25)
done = tk.Button(input_frame, text="Submit", width=10, command= submit_name)

name_entry.grid(row=0, column=0, ipadx=10, ipady=5, padx=10, pady=10)
done.grid(row= 0, column= 1, ipadx=5, padx=10, pady=10)

#radio button
normalc_radio = tk.Radiobutton(input_frame, text= "Normal Case", variable= var, value = "normal")
upperc_radio = tk.Radiobutton(input_frame, text= "Upper Case", variable= var, value= "upper")

normalc_radio.grid(row= 1, column=0)
upperc_radio.grid(row=1, column=1)


submit_name()
window.mainloop()