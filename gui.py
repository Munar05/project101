import tkinter as tk

def calc():
    try:
        price = eval(e.get())
        result.config(text="Итого: " + str(price) + " ₸")
    except:
        result.config(text="Ошибка ввода")

w = tk.Tk()
w.title("GUI модуль магазина")

tk.Label(w, text="Цена товара").pack()

e = tk.Entry(w)
e.pack()

tk.Button(w, text="Посчитать", command=calc).pack()

result = tk.Label(w, text="")
result.pack()

w.mainloop()