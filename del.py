from tkinter import *
from tkinter import messagebox
from connect import one_query
form = Tk()
form.title('delete')
form.geometry('300x50')

entry = Entry(form,width=20)
entry.pack()
l=Label(form,text='companyid')
l.place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.8)
entry.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.8)

show_msg=lambda x: messagebox.showinfo(x,x)

def f():
    s="DELETE FROM tb_company WHERE companyid = %s" % entry.get()
    try:
        one_query(s)
        show_msg('Success')
    except:
        show_msg('数据有误，请重试')
button = Button(form,text='删除',command=f)
button.pack()
button.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.8)

form.mainloop()