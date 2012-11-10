#coding: utf-8




count_of_digits = [3, 3, 1, 0, 1, 1, 2, 0, 1]

for i in range(len(count_of_digits)):
	texts = open("texts/t" + str(i+1) + ".txt")
	tex = texts.read()
	text = tex.split("---")
	numbers = count_of_digits[i]
	if numbers > len(text):
		print text[-1]
	else:
		print text[numbers]

	texts.close()


