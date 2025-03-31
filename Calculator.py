import tkinter as tk
import math
root = tk.Tk()
root.geometry("300x430")
root.title("Calculator")

# Entry Textbox

entry = tk.Entry(root, width= 35, font=("Arial", 17), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Frame for Buttons

buttonframe = tk.Frame(root)
for i in range(4):
    buttonframe.columnconfigure(i, weight=1)
for i in range(6):
    buttonframe.rowconfigure(i, weight=1 )

# Function for adding Buttons

def button_click(number):
    current = entry.get()
    if number == "." and "." in current:
        return
    if current == "0" and number != ".":
        entry.delete(0, tk.END)
        entry.insert(0, number)
        return
    if current == "" and number == ".":
        current = "0"
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Function for Operations

def button_plus():
    first_number = entry.get()
    global first_n, operation
    operation = "+"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.delete(0, tk.END)

def button_minus():
    first_number = entry.get()
    global first_n, operation
    operation = "-"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global first_n, operation
    operation = "*"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global first_n, operation
    operation = "/"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.delete(0, tk.END)

def button_modulo():
    first_number = entry.get()
    global first_n, operation
    operation = "mod"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.delete(0, tk.END)

def button_sin():
    first_number = entry.get()
    global first_n, operation
    operation = "sin"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.insert(0, math.sin(first_n))

def button_cos():
    first_number = entry.get()
    global first_n, operation
    operation = "cos"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.insert(0, math.cos(first_n))

def button_tan():
    first_number = entry.get()
    global first_n, operation
    operation = "tan"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.insert(0, math.tan(first_n))

def button_cot():
    first_number = entry.get()
    global first_n, operation
    operation = "cot"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.insert(0, 1/math.tan(first_n))

def button_percent():
    first_number = entry.get()
    entry.delete(0, tk.END)
    global first_n, operation
    operation = "%"
    if "." in first_number:
        first_n = float(first_number)
    else:
        first_n = int(first_number)
    entry.insert(0, first_n/100)
    



# Function for delivering the result

def button_result():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if "%" in second_number:
        raw_percent = float(second_number.replace("%", ""))
        second_n = (first_n * raw_percent) / 100
    else:
        if "." in second_number:
            second_n = float(second_number)
        else:
            second_n = int(second_number)
    
    if operation == "+":
        entry.insert(0, first_n + second_n)
    elif operation == "-":
        entry.insert(0, first_n - second_n)
    elif operation == "*":
        entry.insert(0, first_n * second_n)
    elif operation == "/":
        if second_n != 0:
            result = first_n / second_n
            if result.is_integer():
                entry.insert(0, int(result))
            else:
                entry.insert(0, result)
        else:
            entry.insert(0, "Error, cannot divide by 0")
    elif operation == "mod":
        entry.insert(0, first_n % second_n)

# Function for clear "C"

def button_clear():
    entry.delete(0, tk.END)

# Function for delete "<"

def button_delete():
    entry.delete(len(entry.get()) - 1, tk.END)

# Define Number Buttons and Put on Frame

btn_9 = tk.Button(buttonframe, text="9", font=("Arial", 18), width=4, command=lambda: button_click(9))
btn_9.grid(row = 2, column = 2, sticky="nsew")

btn_8 = tk.Button(buttonframe, text="8", font=("Arial", 18), width=4, command=lambda: button_click(8))
btn_8.grid(row = 2, column = 1, sticky="nsew")

btn_7 = tk.Button(buttonframe, text="7", font=("Arial", 18), width=4, command=lambda: button_click(7))
btn_7.grid(row = 2, column = 0, sticky="nsew")

btn_6 = tk.Button(buttonframe, text="6", font=("Arial", 18), width=4, command=lambda: button_click(6))
btn_6.grid(row = 3, column = 2, sticky="nsew")

btn_5 = tk.Button(buttonframe, text="5", font=("Arial", 18), width=4, command=lambda: button_click(5))
btn_5.grid(row = 3, column = 1, sticky="nsew")

btn_4 = tk.Button(buttonframe, text="4", font=("Arial", 18), width=4, command=lambda: button_click(4))
btn_4.grid(row = 3, column = 0, sticky="nsew")

btn_3 = tk.Button(buttonframe, text="3", font=("Arial", 18), width=4, command=lambda: button_click(3))
btn_3.grid(row = 4, column = 2, sticky="nsew")

btn_2 = tk.Button(buttonframe, text="2", font=("Arial", 18), width=4, command=lambda: button_click(2))
btn_2.grid(row = 4, column = 1, sticky="nsew")

btn_1 = tk.Button(buttonframe, text="1", font=("Arial", 18), width=4, command=lambda: button_click(1))
btn_1.grid(row = 4, column = 0, sticky="nsew")

btn_0 = tk.Button(buttonframe, text="0", font=("Arial", 18), width=4, command=lambda: button_click(0))
btn_0.grid(row = 5, column = 1, sticky="nsew")

# Define Operation Buttons and Put on Frame

btn_sin = tk.Button(buttonframe, text="sin", font=("Arial", 18), width=4, command=button_sin)
btn_sin.grid(row = 0, column = 0, sticky="nsew")

btn_cos = tk.Button(buttonframe, text="cos", font=("Arial", 18), width=4, command=button_cos)
btn_cos.grid(row = 0, column = 1, sticky="nsew")

btn_tan = tk.Button(buttonframe, text="tan", font=("Arial", 18), width=4, command=button_tan)
btn_tan.grid(row = 1, column = 0, sticky="nsew")

btn_cot = tk.Button(buttonframe, text="cot", font=("Arial", 18), width=4, command=button_cot)
btn_cot.grid(row = 1, column = 1, sticky="nsew")

btn_clear = tk.Button(buttonframe, text="C", font=("Arial", 18), width=4, command=button_clear)
btn_clear.grid(row = 0, column = 2, sticky="nsew")

btn_delete = tk.Button(buttonframe, text="<", font=("Arial", 18), width=4, command=button_delete)
btn_delete.grid(row = 0, column = 3, sticky="nsew")

btn_modulo = tk.Button(buttonframe, text="mod", font=("Arial", 18), width=4, command=button_modulo)
btn_modulo.grid(row = 1, column = 2, sticky="nsew")

btn_divide = tk.Button(buttonframe, text="÷", font=("Arial", 18), width=4, command=button_divide)
btn_divide.grid(row = 2, column = 3, sticky="nsew")

btn_multiply = tk.Button(buttonframe, text="x", font=("Arial", 18), width=4, command=button_multiply)
btn_multiply.grid(row = 3, column = 3, sticky="nsew")

btn_minus = tk.Button(buttonframe, text="-", font=("Arial", 18), width=4, command=button_minus)
btn_minus.grid(row = 4, column = 3, sticky="nsew")

btn_plus = tk.Button(buttonframe, text="+", font=("Arial", 18), width=4, command=button_plus)
btn_plus.grid(row = 5, column = 3, sticky="nsew")

btn_result = tk.Button(buttonframe, text="=", font=("Arial", 18), width=4, command=button_result)
btn_result.grid(row = 5, column = 2, sticky="nsew")

btn_dot = tk.Button(buttonframe, text=".", font=("Arial", 18), width=4, command=lambda: button_click("."))
btn_dot.grid(row = 5, column = 0, sticky="nsew")

btn_percent = tk.Button(buttonframe, text="%", font=("Arial", 18), width=4, command=button_percent)
btn_percent.grid(row = 1, column = 3, sticky="nsew")

# Insert Frame on Parent Window

buttonframe.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Configure Parent Window

root.grid_columnconfigure(0, weight=5)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=5)

root.mainloop()