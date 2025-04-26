"""
Zen Counter - A minimalist to-do list with pomodoro timer
Main entry point for the application
"""
import tkinter as tk
from src.app import ZenDoApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ZenDoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()