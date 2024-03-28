import pypyodbc as odbc 
import sys

records = [
    ['12345','Tran Duc Binh'],
    ['65432','Binh Tran Duc'],
    ['34596','Tran Quoc Viet'],
    ['32195','Nguyen Tan Phong']
]

fix = ['12348', 'Tran Duc Duc Binh']

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'LAPTOP-7RMK354H' #get from SELECT @@SERVERNAME
DATABASE_NAME = 'test'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
try:
    conn = odbc.connect(connection_string)
except Exception as e:
    print(e)
    print("Task is failed: ")
    sys.exit()
else:
    cursor = conn.cursor()

insert_statement = """
    INSERT INTO NGUOIDUNG
    VALUES (?,?)
"""
# first ? is string with size for id = 5, second ? is 30 maximum size string for name 
update_name_statement = """
    UPDATE NGUOIDUNG
    SET HOTEN = ?
    WHERE ID = ?
"""
# first ? is the name you want to change to, second ? is for the person with that id to change that person's name

update_id_statement = """
    UPDATE NGUOIDUNG
    SET ID = ?
    WHERE HOTEN = ?
"""
# similar to update_name_statement but reverse

delete_statement = """
    DELETE FROM NGUOIDUNG
    WHERE ID = ?
"""
# ? for the id of the person you want to delete from data base
select_statement = """
    SELECT*
    FROM NGUOIDUNG
    WHERE ID = ?
"""
# ? for the id of the person you want to get information

def insert(data):
    if all(isinstance(sub_data, list) for sub_data in data):
        for d in data:
            print(d)
            cursor.execute(insert_statement,d)
    else:
        cursor.execute(insert_statement,data)
def delete_id(id):
    cursor.execute(delete_statement,(id,))

def update_name(record):
    cursor.execute(update_name_statement,(record[1],record[0]))
def update_id(record):
    cursor.execute(update_id_statement,(record[0],record[1]))
def find_name(id):
    cursor.execute(select_statement,(id,))


# main here
try:
    update_id(['24624','Nguyen Tan Phong'])
except Exception as e:
    cursor.rollback()
    print(e.value)
    print('rollback')
else:
    print('successfully')
    cursor.commit()
    cursor.close()
finally:
    if conn.connected == 1:
        print('connection closed')
        conn.close()

