#coding: utf-8

#it's only for testing some parts of pifagor.py

def data_request_and_check():
	c = 1
	while c:
		k = raw_input("дата рождения в формате дд.мм.гггг: ")
		if len(k) == 10:
			if k[2] == "." and k[5] == ".":
				c = 0

	return k

i = data_request_and_check()
print i


# def data_request_and_check():

# 	k = raw_input("дата рождения в формате дд.мм.гггг: ")

# 	#checking good format of date, need to add numbers checking
# 	if k[2] == "." and k[5] == "." and len(k) == 10:
# 		print "good format"
# 		return k

# 	else:
# 		print "Give me a good format! Good means dd.mm.yyyy"
# 		return data_request_and_check()


# i = data_request_and_check()
# print i