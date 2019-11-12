from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk


try:
    con = mysql.connector.connect(host='localhost',user='root',passwd='mommy&daddy15',database='simran')
    cur = con.cursor()

except mysql.connector.Error as e:
    print(e)

class Student:
    def __init__(self,root):
        self.root=root
        self.student_id = Label(root, text='Student_Id:', bg='lightblue', font=('Arial', 12, 'bold'))
        self.first_name = Label(root, text='First Name:', bg='lightblue', font=('Arial', 12, 'bold'))
        self.last_name = Label(root, text='Last Name:', bg='lightblue', font=('Arial', 12, 'bold'))
        self.degree = Label(root, text='Degree:', bg='lightblue', font=('Arial', 12, 'bold'))
        self.address = Label(root, text='Address:', bg='lightblue', font=('Arial', 12, 'bold'))
        self.contact_no = Label(root, text='Contact Number:', bg='lightblue', font=('Arial', 12, 'bold'))

        self.student_id.grid(row=1, column=0, padx=10, pady=10)
        self.first_name.grid(row=2, column=0, padx=10, pady=10)
        self.last_name.grid(row=3, column=0, padx=10, pady=10)
        self.degree.grid(row=4, column=0, padx=10, pady=10)
        self.address.grid(row=6, column=0, padx=10, pady=10)
        self.contact_no.grid(row=7, column=0, padx=10, pady=10)

        # Entry
        self.entrystudent_id = Entry(root)
        self.entryfirst_name = Entry(root)
        self.entrylast_name = Entry(root)
        self.degree=Entry(root)
        self.entryaddress = Entry(root)
        self.entrycontact_no = Entry(root)

        self.entrystudent_id.grid(row=1, column=1, padx=10, pady=10)
        self.entryfirst_name.grid(row=2, column=1, padx=10, pady=10)
        self.entrylast_name.grid(row=3, column=1, padx=10, pady=10)
        self.entryaddress.grid(row=6, column=1, padx=10, pady=10)
        self.entrycontact_no.grid(row=7, column=1, padx=10, pady=10)

        self.btn_frame = Frame(root, bd=4, relief=RIDGE, bg='slategray3')
        self.btn_frame.place(x=20, y=300, width=350, height=50)

        self.table_frame = Frame(root, bd=4, relief=RIDGE, bg='gray')
        self.table_frame.place(x=400, y=190, width=720, height=400)

        # scrollbar
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # table
        self.student_table = ttk.Treeview(self.table_frame, column=(
        'student_id', 'first_name', 'last_name', 'degree', 'address', 'contact_no'), xscrollcommand=self.scroll_x.set,
                                     yscrollcommand=self.scroll_y.set)
        self.student_table.heading('student_id', text="Id")
        self.student_table.heading('first_name', text="First Name")
        self.student_table.heading('last_name', text="Last Name")
        self.student_table.heading('degree', text="Degree")
        self.student_table.heading('address', text="Address")
        self.student_table.heading('contact_no', text="Contact Number")
        self.student_table['show'] = 'headings'

        self.student_table.column('student_id', width=120)
        self.student_table.column('first_name', width=120)
        self.student_table.column('last_name', width=120)
        self.student_table.column('degree', width=120)
        self.student_table.column('address', width=120)
        self.student_table.column('contact_no', width=120)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.show()

        self.student_table.bind(('<ButtonRelease-1>'), self.pointer)
        self.student_table.pack(fill=BOTH, expand=True)

        # Buttons
        self.addbutton = Button(self.btn_frame, text='Add', command=self.add_info, width=8, height=2)
        self.addbutton.grid(row=7, column=0, padx=10)

        self.btn_update = Button(self.btn_frame, text='Update', width=8, height=2, command=self.update)
        self.btn_update.grid(row=7, column=1, padx=10)

        self.delete = Button(self.btn_frame, text='Delete', command=self.delete_data, width=8, height=2)
        self.delete.grid(row=7, column=2, padx=10)

        self.btn_clear = Button(self.btn_frame, text='Reset', width=8, height=2, command = lambda:[self.clear(),self.show()])
        self.btn_clear.grid(row=7, column=3, padx=10)

        self.btn_search = Button(root, text='search', height=1, command=self.search, font=('Arial', 12, 'bold'))
        self.btn_search.place(x=500,y=60,width=90)

        self.lbl_search = Label(root, text='Search By:', font=('Arial', 12, 'bold'))
        self.lbl_search.place(x=500,y=30)
        self.combo_search = ttk.Combobox(root, font=('Arial', 10, 'bold'))
        self.combo_search['values'] = ('student_id', 'first_name', 'last_name', 'degree', 'address', 'contact_no')
        self.combo_search.set('student_id')
        self.combo_search.place(x=600,y=30)

        self.btn_sort = Button(root, text='sort', width=10, command=self.sorting, font=('Arial', 10, 'bold'))
        self.btn_sort.place(x=800,y=60)
        self.lbl_sort = Label(root, text='sort by:',width=10, font=('Arial', 10, 'bold'))
        self.lbl_sort.place(x=800,y=30)

        self.combo_sort = ttk.Combobox(root, font=('Arial', 10, 'bold'))
        self.combo_sort['values'] = ('student_id', 'first_name', 'last_name', 'degree', 'address', 'contact_no')
        self.combo_sort.set('student_id')
        self.combo_sort.place(x=900,y=30)

        self.Esearch = Entry(root,width=27)
        self.Esearch.place(x=600,y=60)
        self.degree=ttk.Combobox(self.root,width=20)
        self.degree['values']= ('Bsc(Hons)computing','Bsc(Hons)ethical')
        self.degree.grid(row=4,column=1,padx=10,pady=10)
        self.degree.set('Bsc(Hons)ethical')


    def add_info(self):
        student_id = int(self.entrystudent_id.get())
        first_name = self.entryfirst_name.get()
        last_name = self.entrylast_name.get()
        degree = self.degree.get()
        address = self.entryaddress.get()
        contact_no = int(self.entrycontact_no.get())
        query = 'insert into lalisa values(%s,%s,%s,%s,%s,%s)'
        values = (student_id, first_name, last_name, degree, address, contact_no)
        cur.execute(query, values)
        print('Data saved successfully')
        con.commit()
        self.show()
        self.clear()

    def show(self):
        query = 'select * from lalisa'
        cur.execute(query)
        result = cur.fetchall()
        if len(result) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in result:
                self.student_table.insert('', END, values=row)
                con.commit()

    def delete_data(self):
        student_id = int(self.entrystudent_id.get())
        query = 'delete from lalisa where student_id=%s'
        values = (student_id,)
        cur.execute(query, values)
        print('data deleted successfully')
        con.commit()
        self.show()


    def clear(self):

        self.entrystudent_id.delete(0, END)
        self.entryfirst_name.delete(0, END)
        self.entrylast_name.delete(0, END)
        self.degree.delete(0,END)
        self.entryaddress.delete(0, END)
        self.entrycontact_no.delete(0, END)


    def pointer(self,event):
        point = self.student_table.focus()
        content = self.student_table.item(point)
        row = content['values']
        self.clear()
        self.entrystudent_id.insert(0, row[0])
        self.entryfirst_name.insert(0, row[1])
        self.entrylast_name.insert(0, row[2])
        self.degree.insert(0,row[3])
        self.entryaddress.insert(0, row[4])
        self.entrycontact_no.insert(0, row[5])


    def update(self):
        query = 'update lalisa set first_name=%s,last_name=%s,degree=%s,address=%s,contact_no=%s where student_id=%s'
        student_id = int(self.entrystudent_id.get())
        first_name = self.entryfirst_name.get()
        last_name = self.entrylast_name.get()
        degree = self.degree.get()
        address = self.entryaddress.get()
        contact_no = int(self.entrycontact_no.get())
        values = (first_name, last_name, degree, address, contact_no, student_id)
        cur.execute(query, values)
        con.commit()
        self.show()
        self.clear()

    def search(self, mylist=None):
        if not mylist:
            querys = 'select * from lalisa'
            cur.execute(querys)
            table1 = cur.fetchall()
        else:
            table1 = mylist
        rows = self.search_item(table1)

        if len(table1) != 0:
            self.student_table.delete(*self.student_table.get_children())
        for row in rows:
            self.student_table.insert('', END, values=row)

    def search_item(self,list):

        a2 = self.combo_search.get()
        a3 = self.Esearch.get()

        if a2 == 'student_id':
            fieldId = 0
            a3 = int(self.Esearch.get())
        elif a2 == 'first_name':
            fieldId = 1
        elif a2 == 'last_name':
            fieldId = 2
        elif a2 == 'degree':
            fieldId = 3
        elif a2 == 'address':
            fieldId = 4
        elif a2 == 'contact_no':
            a3 = int(self.Esearch.get())
            fieldId = 5
        else:
            fieldId = 6

        found = []
        for xyz in list:
            if a3 == xyz[fieldId]:
                found.append(xyz)
        return found

    def bubble_sort(self, array):
        x = len(array)

        b1 = self.combo_sort.get()
        if b1 == 'student_id':
            fieldID = 0
        elif b1 == 'first_name':
            fieldID = 1
        elif b1 == 'last_name':
            fieldID = 2
        elif b1 == 'degree':
            fieldID = 3
        elif b1 == 'address':
            fieldID = 4
        elif b1 == 'contact_no':
            fieldID = 5
        else:
            fieldID = 6


        # Transversing through all array elements
        for i in range(x):

             # Last i elements are already in place
            for j in range(0, x - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if array[j][fieldID] > array[j + 1][fieldID]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    def sorting(self):
        querys = 'select * from lalisa'
        cur.execute(querys)
        table1 = cur.fetchall()
        con.commit()
        rows1 = self.bubble_sort(table1)

        if len(rows1) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows1:

            self.student_table.insert('', END, values=row)
        messagebox.showinfo('successfully sorted')

if __name__ == '__main__':
    root = Tk()
    root.title('Student Management')
    gui = Student(root)
    size = root.geometry('1150x600')
    root.configure(bg='black')
    root.mainloop()





