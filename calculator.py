import tkinter as tk
from tkinter import ttk


class Calculator(tk.Frame):  # pylint: disable=too-many-ancestors
    """My calculator."""

    def __init__(self, master=None):
        """Initialize calculator."""
        super().__init__(master)
        self.master = master
        self.configure_window()
        self.create_widgets()
        self.eval_history = []

    def configure_window(self):
        """Configure window."""
        self.master.title("Calculator")
        self.master.configure(bg="blue")
        self.master.minsize(300, 200)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(self.master, padding=5)
        self.mainframe.grid(column=0, row=0, sticky="NSEW")
        self.mainframe.columnconfigure((0, 1, 2, 3), weight=1, minsize=50)
        self.mainframe.rowconfigure((0, 1), weight=1, minsize=50)

    def create_widgets(self):
        """Create widgets."""
        self.output_text = tk.StringVar()
        self.output = ttk.Label(self.mainframe, textvariable=self.output_text)
        self.output['background'] = 'red'
        self.output.grid(rowspan=2, columnspan=4, sticky="NSWE")

        self.input = ttk.Entry(self.mainframe)
        self.input.grid(columnspan=4, sticky="NSWE")

        self.buttons = {}
        button_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                        "+", "-", "*", "/", ".", "="]
        for i in button_names:
            self.buttons[i] = tk.Button(self.mainframe)
            btn = self.buttons[i]
            btn["text"] = i
            btn["command"] = lambda val=i: self.notify(val)

        self.buttons["="]["command"] = self.calculate

        self.buttons["0"].grid(column=0, row=6, sticky="WE")
        self.buttons["1"].grid(column=0, row=5, sticky="WE")
        self.buttons["2"].grid(column=1, row=5, sticky="WE")
        self.buttons["3"].grid(column=2, row=5, sticky="WE")
        self.buttons["4"].grid(column=0, row=4, sticky="WE")
        self.buttons["5"].grid(column=1, row=4, sticky="WE")
        self.buttons["6"].grid(column=2, row=4, sticky="WE")
        self.buttons["7"].grid(column=0, row=3, sticky="WE")
        self.buttons["8"].grid(column=1, row=3, sticky="WE")
        self.buttons["9"].grid(column=2, row=3, sticky="WE")

        self.buttons["+"].grid(column=3, row=3, sticky="WE")
        self.buttons["-"].grid(column=3, row=4, sticky="WE")
        self.buttons["*"].grid(column=3, row=5, sticky="WE")
        self.buttons["/"].grid(column=3, row=6, sticky="WE")
        self.buttons["."].grid(column=1, row=6, sticky="WE")
        self.buttons["="].grid(column=2, row=6, sticky="WE")

        self.input.focus()
        self.master.bind("<Return>", lambda event: self.calculate())

    def calculate(self):
        """Calculate result."""
        text = self.input.get()
        res = text + " = " + str(eval(text))
        self.eval_history.append(res)
        self.eval_history = self.eval_history[-3:]
        self.output_text.set("\n".join(self.eval_history))
        self.input.delete(0, "end")

    def notify(self, text):
        """Print notification."""
        self.input.insert("end", text)


root = tk.Tk()
app = Calculator(master=root)
app.mainloop()
