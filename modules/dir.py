import os
import tkinter as tk
from tkinter import filedialog

def selectParentFolder():           # Select parent folder for 'output'
    root = tk.Tk()
    root.withdraw()
    parent_folder = filedialog.askdirectory(title="Оберіть директорію для створення папки 'outpuy'")
    root.destroy()
    return parent_folder

def initOutputDir(parent_folder):   # Initialize output directory
    output_dir = os.path.join(parent_folder, "output")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def initMediaDir(output_dir):
    media_dir = os.path.join(output_dir, "media")
    os.makedirs(media_dir, exist_ok=True)
    return media_dir