import sqlite3
from user import User

conn = sqlite3.connect("users.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
    first_name text,
    last_name text,
    birthdate integer
)""")#move into user model file

emp_1 = User("Steve", "Jobs", 100000)
emp_2 = User("John", "Doe", 24000)

# c.execute("""INSERT INTO users VALUES (
#     "Mary",
#     "Schafer",
#     70000
# )""")

# conn.commit()

# c.execute(f"""INSERT INTO users VALUES (
#     ?,
#     ?,
#     ?
# )""", (emp_1.first_name, emp_1.last_name, emp_1.birthdate))

# conn.commit()

# c.execute(f"""INSERT INTO users VALUES (
#     :first_name,
#     :last_name,
#     :birthdate
# )""", {"first_name": emp_2.first_name, "last_name": emp_2.last_name, "birthdate": emp_2.birthdate})

# conn.commit()

# c.execute("SELECT * FROM users WHERE last_name='Schafer'")

# c.execute("SELECT * FROM users WHERE last_name=':last_name'", {"last_name": "Doe"})

c.execute("SELECT * FROM users")

#last_name and first_name wrong way round in class, still working!!

print(c.fetchall())

conn.commit()

conn.close()