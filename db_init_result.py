import sqlite3
from result import Result

conn = sqlite3.connect("result.db")

c = conn.cursor()

# c.execute("""CREATE TABLE results (
#     first text,
#     last text,
#     pay integer
# )""")#move into result model file

# c.execute("""INSERT INTO results VALUES (
#     "Corey",
#     "Schafer",
#     50000
# )""")

emp_1 = Result("Steve", "Jobs", 100000)
emp_2 = Result("John", "Doe", 24000)

# c.execute("""INSERT INTO results VALUES (
#     "Mary",
#     "Schafer",
#     70000
# )""")

# conn.commit()

# c.execute(f"""INSERT INTO results VALUES (
#     ?,
#     ?,
#     ?
# )""", (emp_1.first, emp_1.last, emp_1.pay))

# conn.commit()

# c.execute(f"""INSERT INTO results VALUES (
#     :first,
#     :last,
#     :pay
# )""", {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})

# conn.commit()

# c.execute("SELECT * FROM results WHERE last='Schafer'")

# c.execute("SELECT * FROM results WHERE last=':last'", {"last": "Doe"})

c.execute("SELECT * FROM results")

#last and first wrong way round in class, still working!!

print(c.fetchall())

conn.commit()

conn.close()