#!/usr/bin/python


"""
future: try the same with pandas/numpy

# Columns needed with data type:
-------------------------------------
# Primary key ----- ID (auto incrementer)
# Draw date	------- Date (date_format ??)
# Winning Numbers -	Winning_Numbers	(numbers format ??)
# Mega Ball	------- Mega_Ball (interger)
# Multiplier ------ Multiplier (float)

# date format: 06/21/2019
"""

from csv import reader
import mysql.connector as mysql

class Lottery:

	def __init__(self, server, user, database, password):
		self.server = server
		self.user = user
		self.database = database
		self.password = password


	def file_parse(self, file):
		with open(file) as f:
			F = reader(f, delimiter=',')
			data = list(F)
		
		row_num = len(data)
		res = []
		for i, line in enumerate(data):
			if i != 0:
				date = line[0]
				win_nums = line[1]
				mega_ball = line[2]
				multiplier = line[3] if line[3] else "None"
				res.append([i, date, win_nums, mega_ball, multiplier])

		return res


	# Inserting into table connecting to database
	# res --> a list of lists. Each item of the list is a line in the DB
	def Lott_connect(self, res):
		try:
			conn = mysql.conneciton(
				host = self.server,
				database = self.database,
				user = self.user,
				password = self.password
			)
			
			query = "INSERT INTO TABLE (ID, Date, Winning_Numbers, Mega_Ball, Multiplier) VALUES (%d, %s, %s, %d, %s)"

			for i, record in enumerate(res):
				cursor = conn.cursor()
				cursor.execute(query, tuple(record))
				conn.commit()
				print("Successfully inserted %r" % record)

		except:
			print("Connection to database failed")

		finally:
			if conn.is_connected():
				cursor.close()
				conn.close()
			print("Closed MySQL conneciton.")


	def date_convert(self, date):
		D = date.split('/')
		MM = D[0]
		DD = D[1]
		YYYY = D[2]

		new_date  = "%s-%s-%s" % (YYYY, MM, DD)
		return new_date


if __name__ == '__main__':
	
	file = '/home/jkfer/git-projects/python-ETL-sample/MegaMillions_WinningNumbers2002.csv'
	
	L = Lottery('mysql.jkf.local', 'joseph', 'Lottery', '123456')
	res = L.file_parse(file)

	for row in res:
		row[1] = L.date_convert(row[1])

	L.Lott_connect(res)