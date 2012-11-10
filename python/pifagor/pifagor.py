# all info - http://clck.ru/3skVp
# coding: utf-8



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


i = "06.11.1977"

#checking good format of date, need to add numbers checking
if i[2] == "." and i[5] == "." and len(i) == 10:
	print "good format"

else:
	print "Give me a good format! Good means dd.mm.yyyy"



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
print "first work number is %r" %first_work

#second work number - sum of 1st number digits
second_work = sum(number_to_list(first_work))
print "second work number is %r" %second_work

# Из полученного первого рабочего числа отнимаем первую цифру своего дня рождения,
#умноженную на 2 (два) - это постоянный множитель: 32 – 1 х 2 = 32 – 2 = 30
#К примеру, если дата рождения начинается на 0 (09) – 0 отбрасывается,
#умножается 9 на постоянный множитель 2 (два)
#(да, мне лень переводить это на английский)

if day[0] != 0:
	birth_day = day[0]
else:
	birth_day = day[1]

third_work = first_work - birth_day*2
print "third work number is %r" %third_work


# fourth work number - sum of 3rd number digits
fourth_work = sum(number_to_list(third_work))
print "fourth work number is %r" %fourth_work

# first list - numbers of day, month, year, its all_date
print "first list is %r" %all_date

#second list - all work numbers (некрасиво! переделать)
second_list = number_to_list(first_work) + number_to_list(second_work) + number_to_list(third_work) + number_to_list(fourth_work)
print "second list is %r" %second_list

full_list = all_date + second_list
print "full list of numbers is %r" %full_list


#delete nulls from full list

full_list = [x for x in full_list if x > 0] # офигеть красиво!
print full_list
print "it's your %r life" %len(full_list)

#count all digits

count_of_digits = [full_list.count(x) for x in range(1, 10)]

#print results!

for i in range(len(count_of_digits)):
	texts = open("texts/t" + str(i+1) + ".txt")
	tex = texts.read()
	text = tex.split("---")
	numbers = count_of_digits[i]
	if numbers > len(text):
		print text[-1].strip()
	else:
		print text[numbers].strip()

	texts.close()

