# ansii colors from https://stackoverflow.com/a/21786287, can't understand, just magic

import random

alph = ('alpha', 'bravo', 'charlie','delta', 'echo', 'foxtrot',
		'golf', 'hotel', 'india','juliett', 'kilo', 'lima',
		'mike', 'november', 'oscar','papa', 'quebec', 'romeo',
		'sierra', 'tango', 'uniform','victor', 'whiskey', 'x ray',
		'yankee', 'zulu')

#counter
correct_ans = 0
wrong_ans = 0

#color staff
green = '\x1b[1;32;40m'
red = '\x1b[1;31;40m'
red_w_line = '\x1b[4;31;40m'
end_block = '\x1b[0m'

while True:
	quest = random.choice(alph)
	ans = input(f'Word for {quest[0].upper()}: ').lower()
	if not ans:
		break
	if ans == quest:
		correct_ans += 1
		print(f'{green} yes {end_block}')

	else:
		wrong_ans += 1
		print(f'{red_w_line} no {end_block}\nWord for {quest[0].upper()} is {red}{quest}{end_block}')
	print(f'{green} {correct_ans} {end_block} : {red} {wrong_ans} {end_block}\n')





