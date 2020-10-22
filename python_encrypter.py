def jumble_string(regular_string):
	char_list = ''
	count = 0
	for char in regular_string:
		if ' ' == char:
			char_list += ' '
			continue
		ascii = ord(char)
		if (count % 2) == 0:
			if (ascii+1) < 123:
				new_char = chr(ascii+1)
		else:
		    if (ascii-1) >= 97:
		        new_char = chr(ascii-1)
		    else:
		        new_char = chr(ascii+1)
		char_list += str(new_char)
		count += 1
	return char_list

def solve_string(jumbled_string):
    char_list = ''
    count = 0
    for char in jumbled_string:
        if ' ' == char:
            char_list += ' '
            continue
        ascii = ord(char)
        if (count % 2) == 0:
            if (ascii-1) > 96:
                new_char = chr(ascii-1)
        else:
            if ascii == 98:
                new_char = chr(ascii-1)
            elif (ascii+1) < 123:
                new_char = chr(ascii+1)
        char_list += str(new_char)
        count += 1
    return char_list
