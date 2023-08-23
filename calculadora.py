import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.result = tk.StringVar()

        self.input_frame = tk.Frame(master, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.input_frame.pack(side=tk.TOP)

        self.result_label = tk.Label(self.input_frame, textvariable=self.result, font=("Arial", 18), width=50, bg="white", bd=0, justify=tk.RIGHT)
        self.result_label.grid(row=0, column=0)
        self.result.set("0")

        self.button_frame = tk.Frame(master, width=312, height=272.5, bg="white")
        self.button_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/"
        ]
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.calculate(x)
            if button == "0":
                tk.Button(self.button_frame, text=button, bg="#f0f0f0", font=("Arial", 16), width=8, height=2, command=command).grid(row=row, column=col, columnspan=2, padx=1, pady=1)
            elif button == "=":
                tk.Button(self.button_frame, text=button, bg="#4CAF50", font=("Arial", 16), width=8, height=2, command=command).grid(row=row, column=col, padx=1, pady=1)
            elif button == "C":
                tk.Button(self.button_frame, text=button, bg="#f44336", font=("Arial", 16), width=8, height=2, command=command).grid(row=row, column=col, padx=1, pady=1)
            else:
                tk.Button(self.button_frame, text=button, bg="#f0f0f0", font=("Arial", 16), width=8, height=2, command=command).grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def calculate(self, key):
        if key == "=":
            try:
                result = str(eval(self.result.get()))
                self.result.set(result)
            except:
                self.result.set("")
        elif key == "C":
            self.result.set("")
        else:
            self.result.set(self.result.get() + key)


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
