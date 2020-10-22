# if char has even index in string and is not z its added as its ascii number + 1
# if it has odd index in string and its not a its added as ascii number - 1

def encode_string(string):
	char_list = ''
	count = 0
	for char in string:
		if ' ' == char:
			char_list += ' '
			continue
		ascii = ord(char)
		if (count % 2) == 0:
			if (ascii+1) < 123:
				new_char = chr(ascii+1)
		else:
			if (ascii-1) > 96:
				new_char = chr(ascii-1)
		char_list += str(new_char)
		count += 1
	return char_list
