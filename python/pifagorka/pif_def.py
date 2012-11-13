# all info - http://clck.ru/3skVp
# coding: utf-8
import sys; reload(sys); sys.setdefaultencoding('utf-8') # magic string for printing russian text

def pif(user_date):


	def char_to_digit(some_list):
		nums = []
		for x in some_list:
			nums.append(int(x))
		return nums


	def number_to_list(some_number):
		nums = []
		for x in str(some_number):
			nums.append(int(x))
		return nums



	# что делать с проверкой формата - мне совершенно не ясно :(
	# def data_check():
	# 	# Бесконечный цикл, который завершается только по return k, иначе бесконечно выполняется
	# 	while True:
	# 		k = raw_input("дата рождения в формате дд.мм.гггг: ")
	# 		if len(k) == 10:
	# 			if k[2] == "." and k[5] == ".":
	# 				return k


	i = user_date
	#i = data_check()

	
	
	i = i.split(".")
	day = i[0]
	month = i[1]
	year = i[2]

	day = char_to_digit(day)
	month = char_to_digit(month)
	year = char_to_digit(year)


	#first work number - sum of all
	all_date = day + month + year
	first_work = sum(all_date)

	#second work number - sum of 1st number digits
	second_work = sum(number_to_list(first_work))

	# third work number
	if day[0] != 0:
		birth_day = day[0]
	else:
		birth_day = day[1]

	third_work = first_work - birth_day*2


	# fourth work number - sum of 3rd number digits
	fourth_work = sum(number_to_list(third_work))

	# first list - numbers of day, month, year, its all_date
	# second list - all work numbers (некрасиво! переделать)
	second_list = number_to_list(first_work) + number_to_list(second_work) + number_to_list(third_work) + number_to_list(fourth_work)

	full_list = all_date + second_list


	#delete nulls from full list
	full_list = [x for x in full_list if x > 0] # офигеть красиво!
	print "it's your %r life" %len(full_list)

	#count all digits
	count_of_digits = [full_list.count(x) for x in range(1, 10)]

	#print result
	for i in range(len(count_of_digits)):
		heads = open("texts/heads.txt")
		h = heads.read()
		head = h.split("---")
		print head[i]
		heads.close()

		texts = open("texts/t%r.txt" % (i+1))
		tex = texts.read()
		text = tex.split("---")
		numbers = count_of_digits[i]
		if numbers >= len(text):
			print text[-1].strip()
		else:
			print text[numbers].strip()

		texts.close()


#pif(raw_input("date: "))