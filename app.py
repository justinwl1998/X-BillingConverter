import os
from threading import Thread
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from helpers import getRMCPage, getCharges, outputToSpreadsheet

def threading():
    progress.place(anchor = CENTER, relx = 0.5, rely = .6)
    t1 = Thread(target=scanCallBack)
    t1.start()

def directorySelectCallBack():
    folder_selected = fd.askdirectory()
    entry_text.set(folder_selected)
    return

def scanCallBack():
    if os.path.isdir(entry_text.get()):
        B1["state"] = "disabled"
        B2["state"] = "disabled"
        progress.start(2)
        outputToSpreadsheet(entry_text.get(), status_text)
        progress.stop()
        progress.place_forget()
        msg_box = messagebox.askquestion("Status", "Charges written to " + os.getcwd() + "\output.xls\n\nDo you want to open the file?")

        if msg_box == 'yes':
            os.system("start output.xls")

    else:
        progress.place_forget()
        messagebox.showerror("Error", "Directory does not exist!")
    B1["state"] = "normal"
    B2["state"] = "normal"
    status_text.set("")
    return
    
root = Tk()
root.title('Xfinity Billing Statement Converter')
root.resizable(False, False)
root.geometry('400x200')

L1 = Label(root, text="Statements directory", justify="left", anchor="w")
L1.grid(column=0, row=3, sticky=W, pady=(15,0), padx=(30,0))

entry_text = StringVar()
E1 = Entry(root, width=45, bd = 5, state=DISABLED, textvariable=entry_text)
E1.grid(column=0, row=4, sticky=W, padx=(30,0))
B1 = Button(root, text= "...", command = directorySelectCallBack, width=8)
B1.grid(column=1, row=4, sticky=W)

status_text = StringVar(root, value="")
StatusLabel = Label(root, textvariable=status_text, justify="left", anchor="w")
StatusLabel.grid(column=0, row=5, sticky=W, padx=(30,0))

progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 200, mode='indeterminate')
#progress.place(anchor = CENTER, relx = 0.5, rely = .6)

B2 = Button(root, text="Convert to spreadsheet", command = threading)
B2.place(relx=0.5, rely=0.8, anchor=CENTER, height=32, width=150)
root.mainloop()







    
    
