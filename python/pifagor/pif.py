#coding: utf-8


def data_check():

	k = raw_input("дата рождения в формате дд.мм.гггг: ")

	#checking good format of date, need to add numbers checking
	if k[2] == "." and k[5] == "." and len(k) == 10:
		print "good format"
		return k

	else:
		print "Give me a good format! Good means dd.mm.yyyy"
		return data_check()


i = data_check()
print i