import mysql.connector as sq
import matplotlib.pyplot as plt
import datetime

    
def add():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()
    rc = str(input("enter the roll code: "))
    sn = str(input("enter the name of the student: "))
    while True:
        try:
            ph = int(input("enter the phone no.: "))
            break
        except Exception:
            print("something went wrong try again..")
    ft = str(input("enter the father's name: "))
    query1 = "insert into student2 values('{}', '{}', {}, '{}')".format(rc, sn, ph, ft)
    query3 = "insert into att values('{}',0)".format(rc)
    cur.execute(query1)
    cur.execute(query3)
    con.commit()
    now = datetime.datetime.now()
    tod = now.month
    if tod == 8:
        query2 = "insert into fees values('{}','pending..','pending..','pending..','pending..','pending..','paid')".format(rc)
        cur.execute(query2)
        con.commit()
    elif tod == 9:
        query2 = "insert into fees values('{}','paid','pending..','pending..','pending..','pending..','paid')".format(rc)
        cur.execute(query2)
        con.commit()
    elif tod == 10:
        query2 = "insert into fees values('{}','paid','paid','pending..','pending..','pending..','paid')".format(rc)
        cur.execute(query2)
        con.commit()
    elif tod == 11:
        query2 = "insert into fees values('{}','paid','paid','paid','pending..','pending..','paid')".format(rc)
        cur.execute(query2)
        con.commit()
    elif tod == 12:
        query2 = "insert into fees values('{}','paid','paid','paid','paid','pending..','paid')".format(rc)
        cur.execute(query2)
        con.commit()
    elif tod == 1:
        query2 = "insert into fees values('{}', 'paid','paid','paid','paid','paid','paid')".format(rc)
        cur.execute(query2)
        con.commit()
    print("added successfully..")
    con.close()
    
def display():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()
    cur.execute("select*from student2")
    record = cur.fetchall()
    print("rollcode", " ", "studname", "    ", "phoneno.", "      ", "fathername")
    for (rc, sn, ph, ft) in record:
        print(rc, "\t  ", sn, "\t", ph, "\t", ft)
    query = "select count(*) from student2"
    cur.execute(query)
    a = cur.fetchall()
    print("Total entities =>", a[0][0])
    con.close()
        
def delete():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()
    rc = str(input("enter the rollcode of the entity which you want to delete(if you don't know the rollno type none): "))
    if rc == 'none':
        while True:
            try:
                ph = int(input("enter the phone no.: "))
                break
            except Exception:
                print("something went wrong try again..")
        q = "select rollcode from student2 where phone = {}".format(ph)
        #cur.execute(q)
        x = cur.fetchall()
        query1 = "delete from fees where rollcode = '{}'".format(str(x[0][0]))
        query2 = "delete from student2 where rollcode = '{}'".format(str(x[0][0]))
        query3 = "delete from att where rollcode = '{}'".format(str(x[0][0]))
        try:
            query4 = "delete from oldreport where rollcode = '{}'".format(str(x[0][0]))
            query5 = "delete from newreport where rollcode = '{}'".format(str(x[0][0]))
            cur.execute(query4)
            cur.execute(query5)
            con.commit()
        except Exception:
            print("The required record doesn't exist in report data")
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        print("deleted successfully...")
        con.commit()
    else:
        query1 = "delete from fees where rollcode = '{}'".format(rc)
        query2 = "delete from student2 where rollcode = '{}'".format(rc)
        query3 = "delete from att where rollcode = '{}'".format(rc)
        try:
            query4 = "delete from oldreport where rollcode = '{}'".format(rc)
            query5 = "delete from newreport where rollcode = '{}'".format(rc)
            cur.execute(query4)
            cur.execute(query5)
            con.commit()
        except Exception as e:
            print("The required record doesn't exist in report data")
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        print("deleted successfully...")    
        con.commit()    
    con.close()
    
def update():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()#
    while True:
        print("-----------------------")
        print("|1. Student records   |")
        print("|2. New report        |")
        print("|3. back to main menu |")
        print("-----------------------")
        while True:
            try:
                ch1 = int(input("Which table you wonna update: "))
                break
            except Exception:
                print("something went wrong try again..")
        if ch1 == 1:
            while True:
                print("------------------------")
                print("| 1. student name      |")
                print("| 2. phone no.         |")
                print("| 3. father's name     |")
                print("| 4. back              |")
                print("------------------------")
                while True:
                    try:
                        ch = int(input("Which field you wonna update: "))
                        break
                    except Exception:
                        print("something went wrong try again..")    
                if ch == 1:
                    rc = str(input("enter the rollcode of the entity which you wonna update: "))
                    sn = str(input("enter the correct student name: "))
                    query = "update student2 set studname = '{}' where rollcode = '{}'".format(sn, rc)
                    cur.execute(query)
                    print("updated successfully...")
                    con.commit()
                elif ch == 2:
                    rc = str(input("enter the rollcode of the entity which you wonna update: "))
                    while True:
                        try:
                            ph = int(input("enter the phone no.: "))
                            break#
                        except Exception:
                            print("something went wrong try again..")
                    query = "update student2 set phone = '{}' where rollcode = '{}'".format(ph, rc)
                    cur.execute(query)
                    print("updated successfully...")
                    con.commit()
                elif ch == 3:
                    rc = str(input("enter the rollcode of the entity which you wonna update: "))
                    ft = str(input("enter the correct father's name: "))
                    query = "update student2 set fathername = '{}' where rollcode = '{}'".format(ft, rc)
                    cur.execute(query)
                    print("updated successfully...")
                    con.commit()
                elif ch == 4:
                    break
                else:
                    print("Invalid choice...")
        elif ch1 == 2:
            while True:
                print("----------------")
                print("| 1. English   |")
                print("| 2. Physics   |")
                print("| 3. Chemistry |")
                print("| 4. Maths     |")
                print("| 5. Python    |")
                print("| 6. Back      |")
                print("----------------")
                while True:
                    try:
                        ch = int(input("Which field you wonna update: "))
                        break
                    except Exception:
                        print("something went wrong try again..")
                if ch == 1:
                    rc = str(input("enter the rollcode of the entity which you wonna update: "))
                    eng = int(input("enter the updated marks of english: "))
                    q = "update newreport set English = {} where rollcode = '{}'".format(eng,rc)
                    q1 = "update newreport set Total = (English+Physics+Chemistry+Maths+Python)/5 where rollcode = '{}'".format(rc)
                    try:#
                        cur.execute(q)
                        cur.execute(q1)
                        con.commit()
                        print("updated successfull..")
                    except Exception as e:
                        print("the record you wonna update does'nt exist in report data !!")
                elif ch == 2:
                    rc = str(input("enter the rollcode of the entity which you wonna update: "))
                    phy = int(input("enter the updated marks of physics: "))
                    q = "update newreport set Physics = {} where rollcode = '{}'".format(phy,rc)
                    q1 = "update newreport set Total = (English+Physics+Chemistry+Maths+Python)/5 where rollcode = '{}'".format(rc)
                    try:
                        cur.execute(q)
                        cur.execute(q1)
                        con.commit()
                        print("updated successfully..")
                    except Exception as e:
                        print("the record you wonna update does'nt exist in report data !!")
                elif ch == 3:
                    rc = str(input("enter the rollcode of the entity which you wonna update: "))
                    chem = int(input("enter the updated marks of chemistry: "))
                    q = "update newreport set Chemistry = {} where rollcode = '{}'".format(chem,rc)
                    q1 = "update newreport set Total = (English+Physics+Chemistry+Maths+Python)/5 where rollcode = '{}'".format(rc)
                    try:
                        cur.execute(q)
                        cur.execute(q1)
                        con.commit()
                        print("updated successfully..")
                    except Exception as e:
                        print("the record you wonna update does'nt exist in report data !!")
                elif ch == 4:
                    rc = str(input("enter the rollcode of the entity which you wonna update: "))
                    math = int(input("enter the updated marks of maths: "))
                    q = "update newreport set Maths = {} where rollcode = '{}'".format(math,rc)
                    q1 = "update newreport set Total = (English+Physics+Chemistry+Maths+Python)/5 where rollcode = '{}'".format(rc)
                    try:
                        cur.execute(q)
                        cur.execute(q1)
                        con.commit()
                        print("updated successfully..")
                    except Exception as e:
                        print("the record you wonna update does'nt exist in report data !!")
                elif ch == 5:
                    rc = str(input("enter the rollcode of the entity which you wonna update: "))
                    pyt = int(input("enter the updated marks of python: "))
                    q = "update newreport set Python = {} where rollcode = '{}'".format(pyt,rc)
                    q1 = "update newreport set Total = (English+Physics+Chemistry+Maths+Python)/5 where rollcode = '{}'".format(rc)
                    try:
                        cur.execute(q)
                        cur.execute(q1)
                        con.commit()
                        print("updated successfully..")
                    except Exception as e:
                        print("the record you wonna update does'nt exist in report data !!")
                elif ch == 6:
                    break
                else:
                    print("Invalid choice..")
        elif ch1 == 3:
            break
        else:
            print("Invalid choice..")
    con.close()
    
def search():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()
    rc = str(input("Enter the roll code: "))
    while True:
        ch = str(input("Do you want the latest report also(yes/no): "))
        if ch == 'yes':
            try:
                q1 = "select phone from student2 where rollcode = '{}'".format(rc)
                cur.execute(q1)
                ph = cur.fetchall()
                q2 = "select*from student2, newreport where student2.rollcode = newreport.rollcode and phone = {}".format(ph[0][0])
                cur.execute(q2)
                r = cur.fetchall()
                print("Student details..")
                print("Rollcode => ", r[0][0])
                print("Name => ", r[0][1])
                print("Phone no. => ",  r[0][2])
                print("Father's name => ", r[0][3])
                print()
                print("====== Report ======")
                print("English => ", r[0][5])
                print("Physics => ", r[0][6])
                print("Chemistry => ", r[0][7])
                print("Maths => ", r[0][8])
                print("Python => ", r[0][9])
                print("--------------------")
                print("Total => ", r[0][10])
                print("--------------------")
            except Exception as e:
                print("Data unavailable try again..")
            finally:
                break
        elif ch == 'no':
            q = "select*from student2 where rollcode = '{}'".format(rc)
            cur.execute(q)
            r = cur.fetchall()
            print("Rollcode => ", r[0][0])
            print("Name => ", r[0][1])
            print("Phone no. => ",  r[0][2])
            print("Father's name => ", r[0][3])
            break
        else:
            print("Invalid choice!! Try again..")
    con.close()
                   
def displayreport():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()
    cur.execute("select*from newreport")
    record = cur.fetchall()
    print("rollcode", " ", "English", " ", "Physics", " ", "Chemistry", " ","Maths"," ", "Python"," ","Total")
    for i in record:
        print(i[0],'\t\t',i[1],'\t',i[2],'\t  ',i[3],'\t  ',i[4],'\t  ', i[5],'\t   ',i[6])
    ma = "select max(Total) from newreport"
    cur.execute(ma)
    x = cur.fetchall()
    q = "select rollcode from newreport where Total = {}".format(x[0][0])
    cur.execute(q)
    r = cur.fetchall()
    q1 = "select studname from student2 where rollcode = '{}'".format(str(r[0][0]))
    cur.execute(q1)
    r1 = cur.fetchall()
    print("TOPPER")
    print("Rollcode => ",r[0][0])
    print("Name => ",str(r1[0][0]))
    con.close()
    
def performance():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()
    rc = str(input("enter the roll code: "))
    q1 = "select r_id from oldreport where rollcode = '{}'".format(rc)
    cur.execute(q1)
    ri = cur.fetchall()
    q2 = "select r_id,ut1,midterm,ut2,preboard1,Total from oldreport,newreport where r_id = {} and oldreport.rollcode = newreport.rollcode".format(ri[0][0])
    cur.execute(q2)
    r = cur.fetchall()
    x = ['ut1','midterm','ut2','preboard1','final']
    y = [r[0][1], r[0][2], r[0][3], r[0][4], r[0][5]]
    q3 = "select studname from student2 where rollcode = '{}'".format(rc)
    cur.execute(q3)
    n = cur.fetchall()
    plt.xlabel('Exams')
    plt.ylabel('Total marks')
    plt.title(str(n[0][0])+' performance report')
    plt.plot(x,y,'bo',linestyle = 'dashdot')
    plt.show()
    con.close()

def attendance():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()
    rc = str(input("enter the roll code: "))
    q1 = "select studname from student2 where rollcode = '{}'".format(rc)
    cur.execute(q1)
    n = cur.fetchall()
    q2 = "select attendance from att where rollcode = '{}'".format(rc)
    cur.execute(q2)
    r = cur.fetchall()
    if r[0][0] == 0:
        print("New student..")
    else:
        plt.title(str(n[0][0])+" attendance report")
        st = ['present','absent']
        qt = [r[0][0], 280-r[0][0]]
        colr = ['blue','red']
        plt.pie(qt, labels = st,colors = colr, autopct = '%2.2f%%')
        plt.show()
    con.close()

def feestatus():
    con = sq.connect(host = 'localhost', user = 'root', passwd = 'VIVEK', database = 'school')
    cur = con.cursor()
    print("======================================================================")
    print("-----------------Welcome to the fees checking service-----------------")
    print("======================================================================")
    rc = str(input("Enter the roll code for which you wonna check the fees status: "))
    q = "select*from fees where rollcode='{}'".format(rc)
    cur.execute(q)
    r = cur.fetchall()
    lst = []
    for i in r[0]:
        lst.append(i)
    while True:
        print("----------------------------------------------------------------------")
        print("1. August fees")
        print("2. September fees")
        print("3. October fees")
        print("4. November fees")
        print("5. December fees")
        print("6. January fees")
        print("7. Back to main menu")
        while True:
            try:
                ch1 = int(input("enter your choice: "))
                break
            except Exception:
                print("Something went wrong, try again..")
        if ch1 == 1:
            print("| Fee status => ",lst[6]," |")
        elif ch1 == 2:
            print("| Fee status => ",lst[1]," |")
        elif ch1 == 3:
            print("| Fee status => ",lst[2]," |")
        elif ch1 == 4:
            print("| Fee status => ",lst[3]," |")
        elif ch1 == 5:
            print("| Fee status => ",lst[4]," |")
        elif ch1 == 6:
            print("| Fee status => ",lst[5]," |")
        elif ch1 == 7:
            break
        else:
            print("invalid choice..")
    con.close()
                    
#MAIN PROGRAMME    
while True:
    print("==========================")
    print("--------MAIN MENU---------")
    print("| 1. Add                 |")
    print("| 2. Display             |")
    print("| 3. Delete              |")
    print("| 4. Update              |")
    print("| 5. Check fees status   |")
    print("| 6. Search              |")
    print("| 7. Display report      |")
    print("| 8. Performance report  |")
    print("| 9. Attendance          |")
    print("| 10.Exit                |")
    print("--------------------------")
    print("==========================")
    while True:
        try:
            ch = int(input("Enter your required operation => "))
            break
        except Exception:
            print("something went wrong try again..")
    if ch == 1:
        add()
    elif ch == 2:
        display()
    elif ch == 3:
        delete()
    elif ch == 4:
        update()
    elif ch == 5:
        feestatus()
    elif ch == 6:
        search()
    elif ch == 7:
        displayreport()
    elif ch == 8:
        performance()
    elif ch == 9:
        attendance()
    elif ch == 10:
        break
    else:
        print("Invalid choice...")
