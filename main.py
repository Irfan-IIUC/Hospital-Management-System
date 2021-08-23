from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
import tk as tk


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1280x950+0+0")




        # ================== variable =====================

        self.tabletName = StringVar()
        self.refNo = StringVar()
        self.dose = StringVar()
        self.noOfTablet = StringVar()
        self.lotNo = StringVar()
        self.issueDate = StringVar()
        self.expDate = StringVar()
        self.dailyDose = StringVar()
        self.sideEff = StringVar()
        self.furtherInfo = StringVar()
        self.bloodPressure = StringVar()
        self.advice = StringVar()
        self.medication = StringVar()
        self.patientId = StringVar()
        self.nshNo = StringVar()
        self.patientName = StringVar()
        self.dob = StringVar()
        self.address = StringVar()






        l1 = Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System",
                   font=("Times New Roman", 45, "bold"), fg="red", bg="darkGreen")
        l1.pack(side=TOP, fill=X)





        # ============== Top Frame ================

        f1 = Frame(self.root, bd=20, relief=RIDGE)
        f1.place(x=0, y=120, width=1280, height=490)

        lf1 = LabelFrame(f1, bd=10, relief=RIDGE, text="Patient Information", font=
        ("Times New Roman", 25, "bold"), fg="blue")
        lf1.place(x=15, y=5, width=750, height=430)

        lf2 = LabelFrame(f1, bd=10, relief=RIDGE, text="Prescription", font=("Times New Roman",
        25, "bold"), fg="blue")
        lf2.place(x=780, y=5, width=445, height=430)






        # ============== Middle Frame ================

        f2 = Frame(self.root, bd=20, relief=RIDGE)
        f2.place(x=0, y=620, width=1280, height=80)







        # ============== Bottom Frame ================

        f3 = Frame(self.root, bd=20, relief=RIDGE)
        f3.place(x=0, y=710, width=1280, height=240)





        # =============== Frame 1 Lables and TextFields ==================

        l2 = Label(lf1, text="Tablet Name", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l2.place(x=20, y=15)

        cb1 = ttk.Combobox(lf1, textvariable=self.tabletName, font=("Times New Roman", 15, "bold"), width=15)
        cb1["values"] = ("Acetazolamide", "Amitriptyline", "Atenolol", "Chlorambucil",
                         "Dapsone", "Enalapril", "Glibenclamide")
        cb1.current(0)
        cb1.place(x=180, y=15)

        l2 = Label(lf1, text="Reference No", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l2.place(x=20, y=55)

        t1 = Entry(lf1, textvariable=self.refNo, font=("Times New Roman", 15, "bold"), width=17)
        t1.place(x=180, y=55)

        l3 = Label(lf1, text="Dose", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l3.place(x=20, y=95)

        t2 = Entry(lf1, textvariable=self.dose, font=("Times New Roman", 15, "bold"), width=17)
        t2.place(x=180, y=95)

        l4 = Label(lf1, text="No of Tablet", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l4.place(x=20, y=135)

        t3 = Entry(lf1, textvariable=self.noOfTablet, font=("Times New Roman", 15, "bold"), width=17)
        t3.place(x=180, y=135)

        l5 = Label(lf1, text="Lot No", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l5.place(x=20, y=175)

        t4 = Entry(lf1, textvariable=self.lotNo, font=("Times New Roman", 15, "bold"), width=17)
        t4.place(x=180, y=175)

        l6 = Label(lf1, text="Issue Date", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l6.place(x=20, y=215)

        t5 = Entry(lf1, textvariable=self.issueDate, font=("Times New Roman", 15, "bold"), width=17)
        t5.place(x=180, y=215)

        l7 = Label(lf1, text="Exp Date", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l7.place(x=20, y=255)

        t6 = Entry(lf1, textvariable=self.expDate, font=("Times New Roman", 15, "bold"), width=17)
        t6.place(x=180, y=255)

        l8 = Label(lf1, text="Daily Dose", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l8.place(x=20, y=295)

        t7 = Entry(lf1, textvariable=self.dailyDose, font=("Times New Roman", 15, "bold"), width=17)
        t7.place(x=180, y=295)

        l9 = Label(lf1, text="Side Effect", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l9.place(x=20, y=335)

        t8 = Entry(lf1, textvariable=self.sideEff, font=("Times New Roman", 15, "bold"), width=17)
        t8.place(x=180, y=335)

        l10 = Label(lf1, text="Further Info", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l10.place(x=370, y=15)

        t9 = Entry(lf1, textvariable=self.furtherInfo, font=("Times New Roman", 15, "bold"), width=17)
        t9.place(x=530, y=15)

        l11 = Label(lf1, text="Blood Pressure", font=("Times New Roman", 16, "bold"), fg="darkGreen")
        l11.place(x=370, y=55)

        t10 = Entry(lf1, textvariable=self.bloodPressure, font=("Times New Roman", 15, "bold"), width=17)
        t10.place(x=530, y=55)

        l12 = Label(lf1, text="Storage Advice", font=("Times New Roman", 16, "bold"), fg="darkGreen")
        l12.place(x=370, y=95)

        t11 = Entry(lf1, textvariable=self.advice, font=("Times New Roman", 15, "bold"), width=17)
        t11.place(x=530, y=95)

        l13 = Label(lf1, text="Medication", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l13.place(x=370, y=135)

        t12 = Entry(lf1, textvariable=self.medication, font=("Times New Roman", 15, "bold"), width=17)
        t12.place(x=530, y=135)

        l14 = Label(lf1, text="Patient ID", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l14.place(x=370, y=175)

        t13 = Entry(lf1, textvariable=self.patientId, font=("Times New Roman", 15, "bold"), width=17)
        t13.place(x=530, y=175)

        l15 = Label(lf1, text="NHS Number", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l15.place(x=370, y=215)

        t14 = Entry(lf1, textvariable=self.nshNo, font=("Times New Roman", 15, "bold"), width=17)
        t14.place(x=530, y=215)

        l16 = Label(lf1, text="Patient Name", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l16.place(x=370, y=255)

        t15 = Entry(lf1, textvariable=self.patientName, font=("Times New Roman", 15, "bold"), width=17)
        t15.place(x=530, y=255)

        l17 = Label(lf1, text="Date of Birth", font=("Times New Roman", 17, "bold"), fg="darkGreen")
        l17.place(x=370, y=295)

        t16 = Entry(lf1, textvariable=self.dob, font=("Times New Roman", 15, "bold"), width=17)
        t16.place(x=530, y=295)

        l18 = Label(lf1, text="Patient Address", font=("Times New Roman", 16, "bold"), fg="darkGreen")
        l18.place(x=370, y=335)

        t17 = Entry(lf1, textvariable=self.address, font=("Times New Roman", 15, "bold"), width=17)
        t17.place(x=530, y=335)





        # =================== Prescription =====================

        self.t = Text(lf2, font=("Times New Roman", 15), width=38, height=16)
        self.t.place(x=20, y=10)





        # ================= Button ===================

        b1 = Button(f2, command=self.prescription, text="Prescription", font=("Times New Roman", 15), bg="violet",
                    fg="white", height=1, width=15)
        b1.place(x=20, y=0)

        b2 = Button(f2, command=self.prescriptionData, text="Prescription Data", font=("Times New Roman", 15), bg="RosyBrown3",
                    fg="white", height=1, width=15)
        b2.place(x=210, y=0)

        b3 = Button(f2, command=self.updateData, text="Update", font=("Times New Roman", 15), bg="darkGreen",
                    fg="white", height=1, width=15)
        b3.place(x=400, y=0)

        b4 = Button(f2, command=self.delete, text="Delete", font=("Times New Roman", 15), bg="red",
                    fg="white", height=1, width=15)
        b4.place(x=660, y=0)

        b5 = Button(f2, command=self.clear, text="Clear", font=("Times New Roman", 15), bg="gray12",
                    fg="white", height=1, width=15)
        b5.place(x=850, y=0)

        b6 = Button(f2, command=self.exit, text="Exit", font=("Times New Roman", 15), bg="OrangeRed4",
                    fg="white", height=1, width=15)
        b6.place(x=1040, y=0)





        # ================= Table ==================

        scrX = ttk.Scrollbar(f3, orient=HORIZONTAL)
        scrY = ttk.Scrollbar(f3, orient=VERTICAL)

        self.table = ttk.Treeview(f3, column=("tabletName", "refNo", "dose", "noOfTablet",
                                         "lotNo", "issueDate", "expDate", "dailyDose",
                                         "storage", "nshNo", "patient", "dob",
                                         "address"), xscrollcommand=scrX, yscrollcommand=scrY)

        scrX.pack(side=BOTTOM, fill=X)
        scrY.pack(side=RIGHT, fill=Y)

        scrX = ttk.Scrollbar(command=self.table.xview)
        scrY = ttk.Scrollbar(command=self.table.yview)

        self.table.heading("tabletName", text="Tablet Name")
        self.table.heading("refNo", text="Reference No")
        self.table.heading("dose", text="Dose")
        self.table.heading("noOfTablet", text="No of Tablet")
        self.table.heading("lotNo", text="Lot No")
        self.table.heading("issueDate", text="Issue Date")
        self.table.heading("expDate", text="Expiry Date")
        self.table.heading("dailyDose", text="Daily Dose")
        self.table.heading("storage", text="Storage")
        self.table.heading("nshNo", text="NSH No")
        self.table.heading("patient", text="Patient Name")
        self.table.heading("dob", text="Date of Birth")
        self.table.heading("address", text="Address")

        self.table["show"] = "headings"

        self.table.column("tabletName", width=100)
        self.table.column("refNo", width=100)
        self.table.column("dose", width=100)
        self.table.column("noOfTablet", width=100)
        self.table.column("lotNo", width=100)
        self.table.column("issueDate", width=100)
        self.table.column("expDate", width=100)
        self.table.column("dailyDose", width=100)
        self.table.column("storage", width=100)
        self.table.column("nshNo", width=100)
        self.table.column("patient", width=100)
        self.table.column("dob", width=100)
        self.table.column("address", width=100)

        self.table.pack(fill=BOTH, expand=1)

        self.table.bind("<ButtonRelease-1>", self.select)
        self.showData()





    # ============ Button Function =================

    def prescriptionData(self):

        if self.tabletName.get() == "" or self.lotNo.get() == "":
            messagebox.showerror("Message", "All Fields are Required !")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                           database="projecthms1")
            my_cursor = conn.cursor()

            my_cursor.execute("insert into data values(%s, %s, %s, %s, %s, %s, %s, %s, %s, "
                              "%s, %s, %s, %s)", (self.tabletName.get(), self.refNo.get(),
                                self.dose.get(), self.noOfTablet.get(), self.lotNo.get(),
                                self.issueDate.get(), self.expDate.get(), self.dailyDose.get(),
                                self.advice.get(), self.nshNo.get(), self.patientName.get(),
                                self.dob.get(), self.address.get()))

            conn.commit()
            messagebox.showinfo("Message", "Data inserted successfully")
            self.showData()
            conn.close()





    def showData(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="projecthms1")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from data")

        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.table.delete(*self.table.get_children())

            for i in rows:
                self.table.insert("", END, values=i)
                conn.commit()

        conn.close()





    def select(self, event=""):
        x = self.table.focus()
        y = self.table.item(x)
        z = y["values"]

        self.tabletName.set(z[0])
        self.refNo.set(z[1])
        self.dose.set(z[2])
        self.noOfTablet.set(z[3])
        self.lotNo.set(z[4])
        self.issueDate.set(z[5])
        self.expDate.set(z[6])
        self.dailyDose.set(z[7])
        self.advice.set(z[8])
        self.nshNo.set(z[9])
        self.patientName.set(z[10])
        self.dob.set(z[11])
        self.address.set(z[12])





    def updateData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="projecthms1")
        my_cursor = conn.cursor()

        my_cursor.execute("update data set tabletName=%s, dose=%s, noOfTablet=%s,"
                          "lotNo=%s, issueDate=%s, expDate=%s, dailyDose=%s, storage=%s,"
                          "nshNo=%s, patient=%s, dob=%s, address=%s where refNo=%s",
                          (self.tabletName.get(), self.dose.get(), self.noOfTablet.get(),
                           self.lotNo.get(), self.issueDate.get(), self.expDate.get(),
                           self.dailyDose.get(), self.advice.get(), self.nshNo.get(),
                           self.patientName.get(), self.dob.get(), self.address.get(),
                           self.refNo.get()))

        conn.commit()
        messagebox.showinfo("Message", "Data updated successfully")
        self.showData()
        conn.close()





    def prescription(self):

        self.t.insert(END, "Tablet Name:\t\t\t" + self.tabletName.get() + "\n")
        self.t.insert(END, "Reference No:\t\t\t" + self.refNo.get() + "\n")
        self.t.insert(END, "Dose:\t\t\t" + self.dose.get() + "\n")
        self.t.insert(END, "No of Tablet:\t\t\t" + self.noOfTablet.get() + "\n")
        self.t.insert(END, "Lot No:\t\t\t" + self.lotNo.get() + "\n")
        self.t.insert(END, "Issue Date:\t\t\t" + self.issueDate.get() + "\n")
        self.t.insert(END, "Expiry Date:\t\t\t" + self.expDate.get() + "\n")
        self.t.insert(END, "Daily Dose:\t\t\t" + self.dailyDose.get() + "\n")
        self.t.insert(END, "Side Effect:\t\t\t" + self.sideEff.get() + "\n")
        self.t.insert(END, "Further Info:\t\t\t" + self.furtherInfo.get() + "\n")
        self.t.insert(END, "Blood Pressure:\t\t\t" + self.bloodPressure.get() + "\n")
        self.t.insert(END, "Storage Advice:\t\t\t" + self.advice.get() + "\n")
        self.t.insert(END, "Medication:\t\t\t" + self.medication.get() + "\n")
        self.t.insert(END, "Patient ID:\t\t\t" + self.patientId.get() + "\n")
        self.t.insert(END, "NHS No:\t\t\t" + self.nshNo.get() + "\n")
        self.t.insert(END, "Patient Name:\t\t\t" + self.patientName.get() + "\n")
        self.t.insert(END, "Date of Birth:\t\t\t" + self.dob.get() + "\n")
        self.t.insert(END, "Patient Address:\t\t\t" + self.address.get() + "\n")

        #self.t.config(state=DISABLED)





    def delete(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="root",
                                       database="projecthms1")
        my_cursor = conn.cursor()

        my_cursor.execute("delete from data where refNo=%s", (self.refNo.get(),))

        conn.commit()
        messagebox.showinfo("Message", "Data deleted successfully")
        self.showData()
        conn.close()





    def clear(self):

        self.tabletName.set("")
        self.refNo.set("")
        self.dose.set("")
        self.noOfTablet.set("")
        self.lotNo.set("")
        self.issueDate.set("")
        self.expDate.set("")
        self.dailyDose.set("")
        self.sideEff.set("")
        self.furtherInfo.set("")
        self.bloodPressure.set("")
        self.advice.set("")
        self.medication.set("")
        self.patientId.set("")
        self.nshNo.set("")
        self.patientName.set("")
        self.dob.set("")
        self.address.set("")

        self.t.delete("1.0", END)





    def exit(self):

        a = messagebox.askyesno("Hospital Management System", "Do you want to Exit ?")
        if a>0:
            root.destroy()
            return



root = Tk()
ob = Hospital(root)
root.mainloop()
