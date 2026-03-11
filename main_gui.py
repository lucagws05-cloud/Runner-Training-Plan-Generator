# main_gui.py
import tkinter as tk
from gui import RunnerGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = RunnerGUI(root)
    root.mainloop()
    