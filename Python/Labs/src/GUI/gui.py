from tkinter import *
import csv


class GUI:
    def __init__(self, window):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the name, status, and save button.
        """
        self.window = window

        self.frame1 = Frame(self.window)
        self.label_name = Label(self.frame1, text= "Name")
        self.entry_name = Entry(self.frame1)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame1.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.
        self.frame2 = Frame(self.window)
        self.label_age = Label(self.frame2, text=f'{"Age ":<7}')
        self.entry_age = Entry(self.frame2)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=5, side='left')
        self.frame2.pack(anchor='w', pady=10)
        self.frame3 = Frame(self.window)
        self.var = StringVar()
        self.label_status = Label(self.frame3, text="Status")
        self.label_status.pack(padx=5, side='left')
        self.student = Radiobutton(self.frame3, text= "Student", variable=self.var, value="Student", tristatevalue="None")
        self.staff = Radiobutton(self.frame3, text= "Staff", variable=self.var, value="Staff", tristatevalue="None")
        self.both = Radiobutton(self.frame3, text= "Both", variable=self.var, value="Both", tristatevalue="None")
        self.student.pack(padx=5, side="left")
        self.staff.pack(padx=5, side="left")
        self.both.pack(padx=5, side="left")
        self.frame3.pack(anchor='w', pady=10)
        self.frame4 = Frame(self.window)
        self.save = Button(self.frame4, text="SAVE", command=self.clicked)
        self.save.pack(padx=5, anchor="center")
        self.frame4.pack(anchor= "center", pady= 10)




    def clicked(self):
        out_append = open("records.csv", "a")
        csvWriter = csv.writer(out_append)
        name = self.entry_name.get()
        age = self.entry_age.get()
        try:
            age = int(age)
        except ValueError:
            print()
        age *= 2
        choice = self.var.get()
        choice = choice.strip()
        csvWriter.writerow([name,age,choice])
        self.entry_age.delete(0, END)
        self.entry_name.delete(0, END)
        self.staff.deselect()
        self.student.deselect()
        self.both.deselect()
        print(name, age)
        print(choice)
        out_append.close()


        """
        - This method should only be called when the save button is clicked.
        - Retrieve the name, age, and status values.
        - The age must be doubled (e.g. if someone entered 5 for age, their age would be stored as 10).
        - Determine the person status based off the value of the radio button selected.

        - Open the records.csv file and append the new person's details.
        - I suggest first viewing the csv file's contents to understand how your data should be sent to it.

        - Clear the name and age values that were entered in the GUI.
        - Make sure you clear the status value (i.e, No status value should be selected).
        """

