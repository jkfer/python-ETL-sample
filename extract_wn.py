#!/usr/bin/python

"""
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

class Lottery:

	#def __init__(self, server, user, database, table, password):
	#	self.server = server
	#	self.user = user
	# 	self.database = database
	#	self.password = password


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


	def date_convert(self, date):
		D = date.split('/')
		MM = D[0]
		DD = D[1]
		YYYY = D[2]

		new_date  = "%s-%s-%s" % (YYYY, MM, DD)
		return new_date


	def insert_data(self, data):
		# take the list of data and form the SQL queries for insertion
		# SQL_query = ''
		pass



if __name__ == '__main__':
	file = './MegaMillions_WinningNumbers2002.csv'
	L = Lottery()
	res = L.file_parse(file)
	for row in res:
		row[1] = L.date_convert(row[1])

	print(res)