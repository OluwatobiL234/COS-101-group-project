import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MARKET CALCULATOR")

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=('Bahnschrift SemiLight Condensed', 25), justify='right', bd=10)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '1', '2', '3', '+',
            '4', '5', '6', '*',
            '7', '8', '9', '-',
            '0', '.', '/', '='
        ]
    def button_click(self, value):
        current_expression = self.entry_var.get()

if __name__ == "__main__":
     root = tk.Tk()
     app = CalculatorApp(root)
     root.mainloop()
