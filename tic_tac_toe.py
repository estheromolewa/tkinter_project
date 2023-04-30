import tkinter as tk
from tkinter import messagebox
window =tk.Tk()
window.title("TIC TAC TOE")
window.geometry("350x350")
window.config(bg ="#c75c5c" )
window.resizable(0,0)

#X starts so true
clicked = True
count = 0

def button_click(b):
    global clicked, count
    #label.config(text= "qweee")
    if (b["text"])  == " " and (clicked == True):
        b["text"] = "X"
        clicked = False
        count += 1
        check_win()

    elif (b["text"])  == " " and (clicked == False):
        b["text"] = "O"
        clicked = True
        count += 1
        check_win()
    else:
        messagebox.showerror("Hey! That box has already been selected\n Pls select another box")

    
    

def disable_buttons():
    b1.config(state = "disabled")
    b2.config(state= "disabled")
    b3.config(state= "disabled")
    b4.config(state= "disabled")
    b5.config(state= "disabled")
    b6.config(state= "disabled")
    b7.config(state= "disabled")
    b8.config(state= "disabled")
    b9.config(state= "disabled")

def check_win():
    global winner
    winner = False
    #check for O wins
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "grey")
        b2.config(bg="grey")
        b3.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = "grey")
        b5.config(bg="grey")
        b6.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = "grey")
        b8.config(bg="grey")
        b9.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()


    if b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = "grey")
        b4.config(bg="grey")
        b7.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()

    if b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "grey")
        b5.config(bg="grey")
        b8.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round")
        disable_buttons()


    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "grey")
        b6.config(bg="grey")
        b9.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons() 


    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "grey")
        b5.config(bg="grey")
        b9.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round")
        disable_buttons() 

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "grey")
        b5.config(bg="grey")
        b9.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()

    ##check for O
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = "grey")
        b2.config(bg="grey")
        b3.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = "grey")
        b5.config(bg="grey")
        b6.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round")
        disable_buttons() 

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg = "grey")
        b8.config(bg="grey")
        b9.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()


    if b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg = "grey")
        b4.config(bg="grey")
        b7.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()
    if b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = "grey")
        b5.config(bg="grey")
        b8.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round")
        disable_buttons()


    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = "grey")
        b6.config(bg="grey")
        b9.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons() 


    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = "grey")
        b5.config(bg="grey")
        b9.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = "grey")
        b5.config(bg="grey")
        b9.config(bg= "grey")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations X wins this round") 
        disable_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("TIc Tac Toe", "It's a tie!!! \n No one wins!")
        disable_buttons()


score_frame = tk.Frame(window)
button_frame = tk.Frame(window)

score_frame.pack(padx=10, pady=20)
button_frame.pack(padx=10, pady=10)


name_label = tk.Label(score_frame, text= "Enter your name")
versus_label = tk.Label(score_frame, text= "VS")
player1_entry = tk.Entry(score_frame )
player2_entry = tk.Entry(score_frame)


name_label.grid(row= 0, column=0, columnspan = 3, sticky= "WE" )
player1_entry.grid(row=1 , column=0)
versus_label.grid(row=1, column=1)
player2_entry.grid(row= 1, column=2)

#building my buttons
b1 = tk.Button(button_frame, text = " ", font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b1))
b2 = tk.Button(button_frame, text = " ",font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b2))
b3 = tk.Button(button_frame, text = " ",font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b3))
b4 = tk.Button(button_frame, text = " ",font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b4))
b5 = tk.Button(button_frame,text = " ", font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b5))
b6 = tk.Button(button_frame,text = " ", font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b6))
b7 = tk.Button(button_frame,text = " ", font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b7))
b8 = tk.Button(button_frame, text = " ",font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b8))
b9 = tk.Button(button_frame, text = " ",font=("Helvetica, 20"), bg= "SystemButtonFace", command=lambda:button_click(b9))
#display buttons to the screen
b1.grid(row=0, column=0, sticky= "WE", ipadx=20, ipady= 10)
b2.grid(row=0, column=1, sticky= "WE", ipadx=20, ipady= 10)
b3.grid(row=0, column=2, sticky= "WE", ipadx=20, ipady= 10)
b4.grid(row=1, column=0, sticky= "WE", ipadx=20, ipady= 10)
b5.grid(row=1, column=1, sticky= "WE", ipadx=20, ipady= 10)
b6.grid(row=1, column=2, sticky= "WE", ipadx=20, ipady= 10)
b7.grid(row=2, column=0, sticky= "WE", ipadx=20, ipady= 10)
b8.grid(row=2, column=1, sticky= "WE", ipadx=20, ipady= 10)
b9.grid(row=2, column=2, sticky= "WE", ipadx=20, ipady= 10)








window.mainloop()