import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="1478",
  host="localhost",
  port="5432"
)

print("Database opened successfully")

cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT  
     (ADMISSION INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE INT NOT NULL,
     COURSE CHAR(50),
     DEPARTMENT CHAR(50));''')

print("Table created successfully")
con.commit()
con.close()

print("Database opened successfully")
cur = con.cursor()
cur.execute(
  "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')"
)

con.commit()
print("Record inserted successfully")

con.close()