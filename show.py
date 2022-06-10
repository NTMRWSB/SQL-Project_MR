from tkinter import *
from tkinter.ttk import Treeview
from connect import one_query

form = Tk()
form.title('show')
form.geometry('720x480')

xscroll = Scrollbar(form, orient=HORIZONTAL)
yscroll = Scrollbar(form, orient=VERTICAL)
table=Treeview(form,xscrollcommand=xscroll.set,
            yscrollcommand=yscroll.set,show='headings')
table["columns"] = ('companyid','company_name','company_email','username','add_time')
for i in table["columns"]:
    table.heading(i, text=i)
table.column("companyid", width=20)
table.column("company_name", width=100)
table.column("company_email", width=100)
table.column("username", width=100)
table.column("add_time", width=100)
s = 'select companyid,company_name,company_email,username,add_time from tb_company;'
data=one_query(s)
for i in range(len(data)):
    # print(*data[i],sep=',\t')
    table.insert("", END, values=data[i])
xscroll.config(command=table.xview)
xscroll.pack(side=BOTTOM, fill=X)
yscroll.config(command=table.yview)
yscroll.pack(side=RIGHT, fill=Y)
table.pack()
table.place(relx=0, rely=0, relheight=0.95, relwidth=0.95)

form.mainloop()