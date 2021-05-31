from tkinter import *
from tkinter.ttk import *

import openpyxl as o
from openpyxl.styles import Font, colors
path=r"E:\MAJOR8\attendance.xlsx"
wb = o.load_workbook(path)
sheet = wb.active
number=1
while(number!=0):
    print("\nPress\n1- to insert employee\n2- to delete employee\n3- count attendance\n0- exit\n")
    number= int(input())
    if(number==1):
        name=input("name to insert\n")
        uid=input("id to insert\n")
        rows=[[uid,name]]
        for r in rows:
            sheet.append(r)
        print('Inserted')
        wb.save(r"E:\MAJOR8\attendance.xlsx")
        
    if(number==2):
        i=input("id to delete\n")
        for c in sheet['A']:
            if c.value==i:
                rnum=c.row
        sheet.delete_rows(rnum)
        print('Deleted')
        wb.save(r"E:\MAJOR8\attendance.xlsx")
        
    if(number==3):
        i=input("id whose total attendance need\n")
        print("left he")

    if (number==0):
        exit




'''
t = Tk()
t.state('zoomed')



t.mainloop()
'''
