import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var) #t.insert(1.1, var)


e = tk.Entry(window, show='*') #show=None 直接显示输入 show="1"显示1
e.pack()

b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
