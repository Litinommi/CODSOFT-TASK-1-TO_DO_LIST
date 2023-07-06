from tkinter import *

#CREATING BACKGROUND:
display = Tk()
display.title('To-Do List')
display.geometry('1500x750')
display.config(bg="maroon")

#TASKS TO BE PERFORMED:
def delete():
    tasks.delete(ANCHOR)

def edit():
    tasks.delete(ANCHOR)
    tasks.insert(0,"✍ "+ t)


def add():
    globals() ["t"]="✍ " + entryBox.get()
    if t !="":
        tasks.insert(0, t)
    else:
        tasks.delete(0, t)
def markcompleted():

    tasks.delete(ANCHOR)
    tasks.insert(ANCHOR,t + "  ✔")

def exit():
    display.destroy()




Label(display, text='TO DO LIST', bg='maroon', foreground='#EEEEAD', font=("comic sans ms", 50), wraplength=1000).place(x= 600, y=0)
tasks = Listbox(display, selectbackground='black', bg='#8B8B57', font=('Times new roman', 24), height=100, width=550, foreground= "maroon")

#TO USE SCROLLBAR:
scroller = Scrollbar(display, orient=VERTICAL, command=tasks.yview, bg="#8B8B57")
scroller.place(x=1100, y=200, height=350)


#TO CREATE AN ENTRY BOX:
entryBox= Entry(display, width=35, bg="#FFFFD3", foreground="maroon", font=("bold", 24))
entryBox.place(x=400,y=150,height=40)

tasks.config(yscrollcommand=scroller.set)

# INITIATING BUTTONS:

delete_button1=Button(display, text="DELETE", foreground="#EEEEAD", command=delete, width=30, bg="maroon", font="bold")
delete_button1.place(x=400, y=500, height=50)

edit_button2=Button(display, text="EDIT", foreground="#EEEEAD", command=edit, width=30, bg="maroon", font="bold")
edit_button2.place(x=760, y=450, height=50)

add_button3=Button(display, text="ADD TASK", foreground="#EEEEAD", command=add, width=10, bg="maroon", font="bold")
add_button3.place(x=1000, y=150, height=40)

completed_button4=Button(display, text="COMPLETED", foreground="#EEEEAD", command=markcompleted, width=30, bg="maroon", font="bold")
completed_button4.place(x=400, y=450, height=50)

exit_button1=Button(display, text="EXIT", foreground="#EEEEAD", command=exit, width=30, bg="maroon", font="bold")
exit_button1.place(x=760 , y=500, height=50)


tasks.pack(padx=400, pady=200)
display.update()
display.mainloop()