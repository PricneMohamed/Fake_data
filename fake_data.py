from faker import Faker

fk = Faker()

detect = input("""Hello , Sir
                Do you want CSV or SQLITE or No ?
                    """).strip().upper()
count = int(input("""
                How many the rows sir?
                    """))

def sql(count):
    import sqlite3
    file = input("""
            Enter File Name Please: 
                """)
    table = input("""
            Enter Table Name Please: 
                """)


    db = sqlite3.connect(f"{file}.db")
    cr = db.cursor()
    cr.execute(f"CREATE TABLE IF NOT EXISTS {table}(Name TEXT, Phone TEXT , Email TEXT , Job TEXT)")
    for _ in range(count):
            cr.execute(f"INSERT INTO {table}(Name, Phone, Email, Job) VALUES('{fk.name()}', '{fk.phone_number()}' , '{fk.free_email()}' , '{fk.job()}')")
    else:
        result = cr.execute(f"SELECT * FROM {table}")
        print(result.fetchall())
    db.commit()    
    db.close()

def pross(count):
    data_name = []
    data_phone = []
    data_email = []
    data_job = []

    for _ in range(count):
            data_name.append(fk.name())
            data_job.append(fk.job())
            data_email.append(fk.free_email())
            data_phone.append(fk.phone_number())
    else:
        print(data_name)
        print(data_job)
        print(data_email)
        print(data_phone)


def csv(count):
    import csv
    file = input("""
            Enter File Name Please: 
                """)
    key =['Name','Email','Phone','Job']
    with open(f"{file}.csv", 'w' ,newline='') as f:
        w = csv.DictWriter(f , fieldnames=key)
        w.writeheader()
        for _ in range(count):
            data_dict = {
                    'Name': fk.name(),
                    'Email': fk.free_email(),
                    'Phone': fk.phone_number(),
                    'Job': fk.job(),
                        }
            w.writerow(data_dict)

if detect == "SQL" or detect == "SQLITE":
    sql(count)

elif detect == "CSV" :
    csv(count)
elif detect ==  "NO":

    pross(count)



