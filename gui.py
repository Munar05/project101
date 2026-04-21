import tkinter as tk

def calc():
    total = int(e.get())
    r.config(text="Итого: " + str(total))

w = tk.Tk()
w.title("Подсчет заказа")

e = tk.Entry(w)
e.pack()

b = tk.Button(w, text="Посчитать", command=calc)
b.pack()

r = tk.Label(w, text="")
r.pack()

w.mainloop()