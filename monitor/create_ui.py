import Tkinter

from utilities.db import DbService
from Tkinter import *

dbService = DbService()

def build_ui():
    master = Tk()
    serviceName = StringVar()
    URL = StringVar()

    topFrame = Frame(master)
    topFrame.pack()

    bottomFrame = Frame(master)
    bottomFrame.pack(side=BOTTOM)

    def okCallBack():
    	dbService.insert(1,serviceName.get(),URL.get(),"0")
    	dbService.print_all()

    def cancelCallBack():
        master.destroy()

    okButton = Button(bottomFrame,text="OK",command=okCallBack)
    okButton.pack(side=RIGHT)
    cancelButton = Button(bottomFrame,text="Cancel",command=cancelCallBack)
    cancelButton.pack(side=LEFT)

    theNameLabel = Label(topFrame, text="Enter the service name")
    theNameLabel.grid(row=0)
    theNameInput = Entry(topFrame,textvariable=serviceName)
    theNameInput.grid(row=0,column=1)

    theUrlLabel = Label(topFrame, text="Enter the service URL")
    theUrlLabel.grid(row=1)
    theUrlInput = Entry(topFrame,textvariable=URL)
    theUrlInput.grid(row=1,column=1)

    master.mainloop()

if __name__ == '__main__':
    build_ui()