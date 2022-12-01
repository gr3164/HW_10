from tkinter import *
from tp_bot import *

count = 0
r = None
id = None

with open("report.txt", "r", encoding="utf-8") as f:
    data = f.read().split('\n')
    print(data)
   
m = [i.replace("||", " ").split() for i in data]
# print(m)

def Print_text():
    global count, m, r, id
    if len(m[count]) <= 1:
        entry_q.configure(state=NORMAL)
        entry_q.delete(0.0, END)
        entry_q.insert(1.0, f"Нет вопросов")
        entry_q.configure(state=DISABLED)
        entry_a.configure(state=DISABLED)
    else:  
        entry_q.configure(state=NORMAL)
        entry_q.delete(0.0, END)
        entry_q.insert(1.0, f"Имя: {m[count][1]}\nВопрос: {m[count][2]}")
        r = entry_q.get("1.0", END).split()
        id = m[count][0]
        entry_q.configure(state=DISABLED)
        button_on_click() 
    

def button_on_click():
    global count
    count += 1
    return count

def Send():
    global r, id
    q = r[-1]
    answer = entry_a.get("1.0", END)
    Send_message(id, answer, q)
    Print_text()
    entry_a.delete('1.0', END)

root = Tk()
root.title('Служба поддержки')
root.geometry('500x300')



Label_q = Label(root, text="Вопрос")
Label_q.grid(column=2, row=1)
entry_q = Text(root, width=30, height=10)
entry_q.grid(column=2, row=2)
btn = Button(root, text="Следующий вопрос", command=Print_text)
btn.grid(row=3, column=2)


Label_a = Label(root, text="Ответ")
Label_a.grid(column=4, row=1)
entry_a = Text(root, width=30, height=10)
entry_a.grid(column=4, row=2)
btn_a = Button(root, text="Отправить", command=Send)
btn_a.grid(row=3, column=4)



root.mainloop()

