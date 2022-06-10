from tkinter import *
from tkinter import messagebox
from connect import one_query
form = Tk()
form.title('add')
form.geometry('720x480')

h=('companyid','company_name','company_address','company_tel','company_contact_people','company_email','username','add_time')
entrys=[]
for i in range(8):
    l=Label(form,text=h[i])
    entry = Entry(form,width=20)
    entrys.append(entry)
    entry.pack()
    l.place(relx=0.05, rely=0.1*(i+1), relwidth=0.3)
    entry.place(relx=0.5, rely=0.1*(i+1), relwidth=0.3)

show_msg=lambda x: messagebox.showinfo(x,x)

def f():
    s="INSERT INTO tb_company (companyid,company_name,company_address,company_tel,company_contact_people,company_email,username,add_time) VALUES (%s,'%s','%s','%s','%s','%s','%s','%s');"%tuple((x.get() for x in entrys))
    try:
        one_query(s)
        show_msg('Success')
    except:
        show_msg('数据有误，请重试')
button = Button(form,text='添加',command=f)
button.pack()
button.place(relx=0.45, rely=0.9, relwidth=0.1)

form.mainloop()