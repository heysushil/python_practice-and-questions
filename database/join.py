import connection as con 

query = """CREATE TABLE IF NOT EXISTS student(
    id int(8) not null AUTO_INCREMENT PRIMARY KEY, 
    student_name varchar(500), 
    roll_no int(50), 
    date timestamp)"""
con.create.execute(query)

query = """CREATE TABLE IF NOT EXISTS class(
    id int(8) not null AUTO_INCREMENT PRIMARY KEY, 
    roll_no varchar(500), 
    class varchar(60), 
    date timestamp)"""
con.create.execute(query)


def option():
    print("""
    Choose Options:
    1. New Admission
    2. View Stduents
    3. Update Any Expence
    4. Delete Any Expence
    5. Exit
    """)
    user_input = input('\nEnter your option: ')
    if user_input == '1':
        student_admisstion()
    elif user_input == '2':
        query_data = "SELECT s.id, s.roll_no, c.class as class, s.student_name, s.date FROM student as s JOIN class as c ON c.roll_no=s.roll_no" 
        header_title = ['#','ID','Roll No','Class','Student Name','Date']
        title='View Details'
        con.view_data(query_data, header_title, title)
    elif user_input == '3':
        update_student()
    elif user_input == '4':
        delete_student()
    elif user_input == '5':
        print('\nExit')


def student_admisstion():
    student_data = {
        'student_name': input('\nEnter student name:'),
        'roll_no': input('\nEnter student roll number:'),
    }
    class_data = {
        'class': input('\nEnter student class name:'),
    }
    query = """INSERT INTO student(student_name, roll_no) VALUES('{}','{}')""".format(student_data['student_name'], student_data['roll_no'])
    con.create.execute(query)
    con.db.commit()
    query = """INSERT INTO class(roll_no, class) VALUES('{}','{}')""".format(student_data['roll_no'], class_data['class'])
    con.create.execute(query)
    con.db.commit()
    option()


def update_student():
    pass

def delete_student():
    pass


option()