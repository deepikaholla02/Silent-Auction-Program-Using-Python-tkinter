from tkinter import *
from tkinter import messagebox

bidders={}

def submit():
    name=name_entry.get()
    bid=int(bid_entry.get())
    bidders[name]=bid
    history_listbox.insert(END, f"{name}  -  {bid}")

    more_bidders=messagebox.askyesnocancel("Silent Auction program","Bid Added Successfully!!! Are there any bidders?")
    if more_bidders:
        name_entry.delete(0, 'end')
        bid_entry.delete(0, 'end')
        name_entry.focus()
    else:
        window.destroy()
        result()


# Result Window
def result():
    res_window=Tk()
    res_window.title("Silent Auction Program")
    res_window.geometry("600x250")
    res_window.config(background="black")
    head_label=Label(res_window,text="SILENT AUCTION RESULTS",font=("Times New Roman",30,"bold"),fg="orange",bg="black",relief=RAISED,bd=10)
    head_label.pack()

    highest_bidder=max(bidders,key=bidders.get)
    winner_text = f"The winner is {highest_bidder} with a bid of {bidders[highest_bidder]}"
    res_label=Label(res_window,text=winner_text,font=("Times New Roman",20,"bold"),fg="yellow",bg="black")
    res_label.pack(pady=40)
    
    exit_button=Button(res_window,text="EXIT",font=("Times New roman",20,"bold"),bg="black",fg="orange",command=res_window.destroy)
    exit_button.pack()
        
# ------- GUI Window ---------

window=Tk()
window.title("Silent Auction Program")
window.geometry("800x600")
window.config(background="black")

title_label=Label(window,text="SILENT AUCTION",font=("Times New Roman",30,"bold"),fg="cyan",bg="black",relief=RAISED,bd=10)
title_label.place(x=230,y=0)

# Bidder's Name
name_label=Label(window,text="Bidder Name : ",font=("Times New Roman",15),bg="black",fg="orange")
name_label.place(x=230,y=90)

name_entry=Entry()
name_entry.config(font=("Times New Roman",15),bg="black",fg="orange")
name_entry.place(x=410,y=90,width=160)

# Bid Amount
bid_label=Label(window,text="Bid Amount : ",font=("Times New Roman",15),bg="black",fg="orange")
bid_label.place(x=230,y=150)

# Validating Bid amount by ensuring only integers are entered
def only_integers(P):
    return P.isdigit() or P == ""
vcmd = window.register(only_integers)

bid_entry=Entry(window,font=("Times New Roman", 15),bg="black",fg="orange",validate="key",validatecommand=(vcmd, "%P"))
bid_entry.config(font=("Times New Roman",15),bg="black",fg="orange")
bid_entry.place(x=410,y=150,width=160)

# Bid History
history_label = Label(window,text="Bid History",font=("Times New Roman", 18, "bold"),bg="black",fg="cyan")
history_label.place(x=310, y=330)

history_listbox = Listbox(window,width=25,height=8,font=("Times New Roman", 12),bg="black",fg="yellow",highlightbackground="orange",selectbackground="orange")
history_listbox.place(x=285, y=380)

# Submit Bid
submit=Button(window,text="Submit Bid", font=("Times New Roman",20,"bold"),bg="black",fg="cyan",command=submit)
submit.place(x=300,y=230)

window.mainloop()