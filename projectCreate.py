import os
import sys
import tkinter as tk
from tkinter import filedialog, Text
import tkinter.font as font
from tkinter.filedialog import asksaveasfile

# This is the variable that will store the root
rootloc = ''

# This will create the window that is used
# root = tk.Tk()
# root.title('Project Structure Creator')

# This will get the root directory
filename = filedialog.askdirectory(initialdir="/", title="Select Project Folder")
rootloc = filename

# This is a list of all the used services
services = ["_arch",
            "_mech",
            "_elec"]

# This is a list of all the nested folders withing each servies
nested = ["_drawings",
          "_data"]


# This will make these directories
for i in services:
    # This will change to root sothat the creation can begin
    os.chdir(rootloc)
    os.mkdir(i)
    os.chdir(os.path.join(rootloc, i))
    for j in nested:
        os.mkdir(j)
