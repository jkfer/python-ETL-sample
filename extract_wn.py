#!/usr/bin/python

# Columns needed with data type:

# Primary key		ID		auto incrementer
# Draw date		Date		date_format ??
# Winning Numbers	Winning_Numbers	numbers format ??
# Mega Ball		Mega_Ball	interger
# Multiplier		Multiplier	float


# date format: 06/21/2019


from csv import reader

class Lottery:
	def __init__(self, server, database, table, password):
		self.server = server
		self.database = database
		self.password = password

	def file_parse(file):
		with open(file, 'rb') as f:
			F = reader(f)
			date = list(F)


file = './Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv'


def date_convert(date):
	# Acceptable MySQL format: YYYY-MM-DD
	D = date.split('/')
	MM = D[0]
	DD = D[1]
	YYYY = D[2]

	new_date  = "%s-%s-%s" % (YYYY, MM, DD)
	return new_date


with open(file, 'rb') as f:
	F = reader(f)
	data = list(F)

row_num = len(data)

for num, line in enumerate(data):
	if num != 0:
		date = line[0]
		win_nums = line[1]
		mega_ball = line[2]
		multiplier = line[3]

		new_date = date_convert(date)

		print("%s, %s, %s, %s, %s" % (num, new_date, win_nums, mega_ball, multiplier))



