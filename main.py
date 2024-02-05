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
        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, padx=40, pady=40, font=('Bahnschrift SemiLight Condensed', 20), command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    def button_click(self, value):
        current_expression = self.entry_var.get()
                if value == '=':
            try:
                result = eval(current_expression)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        else:
            self.entry_var.set(current_expression + value)

if __name__ == "__main__":
     root = tk.Tk()
     app = CalculatorApp(root)
     root.mainloop()
