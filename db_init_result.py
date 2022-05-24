import sqlite3
from employee import Employee

conn = sqlite3.connect("employee.db")

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#     first text,
#     last text,
#     pay integer
# )""")#move into result model file

# c.execute("""INSERT INTO employees VALUES (
#     "Corey",
#     "Schafer",
#     50000
# )""")

emp_1 = Employee("Steve", "Jobs", 100000)
emp_2 = Employee("John", "Doe", 24000)

# c.execute("""INSERT INTO employees VALUES (
#     "Mary",
#     "Schafer",
#     70000
# )""")

# conn.commit()

# c.execute(f"""INSERT INTO employees VALUES (
#     ?,
#     ?,
#     ?
# )""", (emp_1.first, emp_1.last, emp_1.pay))

# conn.commit()

# c.execute(f"""INSERT INTO employees VALUES (
#     :first,
#     :last,
#     :pay
# )""", {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})

# conn.commit()

# c.execute("SELECT * FROM employees WHERE last='Schafer'")

# c.execute("SELECT * FROM employees WHERE last=':last'", {"last": "Doe"})

c.execute("SELECT * FROM employees")

#last and first wrong way round in class, still working!!

print(c.fetchall())

conn.commit()

conn.close()