import sqlite3
conn = sqlite3.connect("test.db")
conn.execute(
    '''CREATE TABLE STUDENT
    (
        Roll INT PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        Marks INT NOT NULL
    );'''
)
conn.execute(
    INSERT INTO STUDENT (Roll, Name, Marks)\
        VLUES
    )