import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
    def button_click(self, value):
        current_expression = self.entry_var.get()

if __name__ == "__main__":
     root = tk.Tk()
     app = CalculatorApp(root)
     root.mainloop()