import sqlite3
conn = sqlite3.connect("login.db")
try:
	conn.execute(''' CREATE TABLE Records
					 (Id INT PRIMARY KEY NOT NULL,
					  Pass TEXT NOT NULL,
					  Name TEXT NOT NULL);''')
	
	conn.execute("INSERT INTO Records(Id,Pass,Name)\
					VALUES(48,'123','Abuzar Shaikh')");
										  
	conn.execute("INSERT INTO Records(Id,Pass,Name)\
					VALUES(49,'321','Aisha Shaikh')");
	
	conn.execute("INSERT INTO Records(Id,Pass,Name)\
					VALUES(60,'213','Zaid Siddiqui')");

	while True:
		user = int(input('Enter UserID: '))
		pw = input('Enter Password: ')
		flag = 0
		cursor = conn.execute("SELECT Id, Pass, Name FROM Records")
		for row in cursor:
			if row[0] == user and pw == row[1]:
				print('Welcome {}\n'.format(row[2]))
				flag = 1
				break
		if flag == 0:
			print('Invalid User\n')
		c = input('Continue [Y/N]: ')
		if c.upper() == 'N':
			break
finally:
	conn.execute("DROP TABLE Records")
	conn.close()
	
"""
conn = sqlite3.connect("login.db")
conn.execute("DROP TABLE Records")
"""
