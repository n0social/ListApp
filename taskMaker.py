#TaskMaker


#imports
import tkinter as tk
import time
from tkinter import *
from tkinter.ttk import *
import pickle

#root
root= tk.Tk()
root.title("To Do List")

#Add Menu
#menu = Menu(root)

#new_item = Menu(menu)
#menu.add_cascade(label="File")
#new_item.add_command(label="View")
#new_item.add_separator()

lbl = tk.Label(root, text="Do you have any tasks today?")
lbl.grid(column=1,row=1)



#def sendToMainroot():
#    
task_Name = tk.StringVar()
task_descrip = tk.StringVar()


def submit():
    taskName = task_Name.get()
    taskDescrip = task_descrip.get()

    #Debugging
    print("The task name is: " + taskName)
    print("The task entails: " + taskDescrip)


    global pname
    pname = taskName
    #yourTask = tk.Label(root, text=f'{pname} ' + taskDescrip)
    #yourTask.grid(column=1,row=5)    


    #main_Tasks = [taskName,taskDescrip]
    #for task in main_Tasks:
    #    yourTask.insert(0,task)

    #main_Tasks_label = tk.Label(root,textvariable=main_Tasks)
    #main_Tasks_label.grid(column=1,row=6)

    lB1.insert("end","- " + taskName + ": "  + taskDescrip)
    lB1.insert("end","""
    
    """)
    





def clearButton():
    entryDesc.delete(0,END)
    name_entry.delete(0,END)

def deleteButton():
    lB1.delete(tk.ACTIVE)

#def printValue():
#    pname = task_Name.get()
#    Label(root, text=f'{pname}, ' + task_descrip, pady=20, bg='#ffbf00').pack()








label_add_task_Name = tk.Label(root,text="Add Task Name: ")
label_add_task_Name.grid(column=0,row=2)
name_entry = tk.Entry(root, textvariable=task_Name, width=50)
name_entry.grid(column=1,row=2)


label_add_task_desc = tk.Label(root,text="Add Task Description: ")
label_add_task_desc.grid(column=0,row=3)
entryDesc = Entry(root, textvariable=task_descrip, width=50)
entryDesc.grid(column=1,row=3)

#btnDesc = tk.Button(root, text="Add item", command= submit)
#btnDesc.grid(column=3, row=3)

btn_clear = tk.Button(root, text="Clear", command=clearButton)
btn_clear.grid(column=1, row=5)

btnSave = tk.Button(root, text="Add Item", command=submit)
btnSave.grid(column=0, row=4)

btnDel = tk.Button(root, text="Delete Item", command=deleteButton)
btnDel.grid(column=0, row=5)

#btn_Save = tk.Button(root, text="Save", command=printValue)
#btn_Save.grid(column=3, row=3)

#btn_Register = tk.Button(root, text="Register", command=some_command)
#btn_Register.grid(column=3, row=4)



#Shows Task - Would like to find a way to save it to a variable
#label_show_task = tk.Label(root, textvariable=task_Name)
#label_show_task.grid(column=0,row=3)
#variableTask = label_show_task
#variableTask.grid(column=0,row=3)

#label_show_task = tk.Label(root, textvariable=task_descrip)
#label_show_task.grid(column=1,row=3)

lB1 = Listbox(root, width=50, selectmode=tk.EXTENDED)
lB1.grid(column=1,row=4)


#for i in range(1):
                #self.label_list.insert(1, tk.Label(self.label_frame, text="Tasks"))
                #self.label_list[i].grid(row=i)
        #label_show_task = tk.Label(root, textvariable=task_descrip)
        #label_show_task[i].grid(row=i)



#label_show_task = tk.Label(root, textvariable=task_descrip)
#label_show_task.grid(column=1,row=3)



root.mainloop()

#root.mainloop()

#def btnYPress():
#    rootY = tk.Tk()
#    rootY.title("Add Task")
#    label_add_task_Name = tk.Label(rootY,text="Add Task Name: ")
#    label_add_task_Name.grid(column=0,row=0)
#    name_entry = tk.Entry(rootY, textvariable=task_Name)
#    name_entry.grid(column=1,row=0)
    #btnName = Button(rootY, text="Enter")
    #btnName.grid(column=2, row=0)
    #labl_ent = Label(root)
    #labl_ent.grid(column=3, row=1)
    
#    label_add_task_desc = tk.Label(rootY,text="Add Task Description: ")
#    label_add_task_desc.grid(column=0,row=1)
#    entryDesc = Entry(rootY, textvariable=task_descrip)
#    entryDesc.grid(column=1,row=1)

#    btnDesc = tk.Button(rootY, text="Enter", command=submit)
#    btnDesc.grid(column=2, row=1)
    
    #lablDesc = Label(root)
    #lablDesc.grid(column=3, row=1)

#Appending the information from name and description into a list format on the main root3

#I'm thinking next step is to make the task a class. Then adding each iteration of the class to the main root
#class tasks {
#        
#}

#btnY = tk.Button(root, text="Yes", command=btnYPress)
#btnY.grid(column=0,row=2)
#btnN = tk.Button(root, text="No" )
#btnN.grid(column=1, row=2)

#label_show_entry = Label(root, text="Show Entry here")




#root.mainloop()
