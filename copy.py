import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter.messagebox import showinfo
class Application(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()
        self.srcString = tk.StringVar()
        self.dstString = tk.StringVar()
        # self.label = ttk.Label(self)
        # self.label["text"] = "Remote File Backup System"
        # # self.label["font"] = ('Helvetica', '12')
        # self.label.grid(row=0,column=0,sticky=tk.W)
        self.srcLabel = ttk.Label(self)
        self.srcLabel["text"] = "Source Folder:"
        # self.srcLabel["font"] = ('Helvetica', '12')
        self.srcLabel.grid(row=1,column=0,sticky=tk.W)
        self.srcInput = ttk.Entry(self,width=70, textvariable=self.srcString)
        self.srcString.set(r"\\tbsvmdc1backend-124-prod\mtb_site_rpa\TEST\RPA_yingjunhuang\src")
        self.srcInput.grid(row=1, column=1, padx=10)

        self.dstLabel = ttk.Label(self)
        self.dstLabel["text"] = "Destination Folder:"
        # self.srcLabel["font"] = ('Helvetica', '12')
        self.dstLabel.grid(row=2,column=0,sticky=tk.W)
        self.dstInput = ttk.Entry(self,width=70, textvariable=self.dstString)
        self.dstString.set(r"\\tbsvmdc1backend-124-prod\mtb_site_rpa\TEST\RPA_yingjunhuang\dst")
        self.dstInput.grid(row=2, column=1, padx=10)

                                                                      
        self.button = ttk.Button(self)
        self.button["text"] = "Click Me!"
        self.button["command"] = self.copy
        self.button.grid(row=3,column=0)
    
    def copy(self):
        subprocess.call(['robocopy',self.srcString.get(),self.dstString.get(),"/E"])
        

root = tk.Tk()
app = Application(root)
root.mainloop()