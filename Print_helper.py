from Print import  Display

def OLED_print(text):
	MAX_Char_limit = 14
	words = text.split()
	words.reverse()
	
	line1 = " "
	line2 = " "
	line3 = " "
	line4 = " "
	
	for word in words:
		if len(line4) <= MAX_Char_limit: 
			word += (" "+line4)
			line4 = word
		elif len(line3) <= MAX_Char_limit: 
			word += (" "+line3)
			line3 = word
		elif len(line2) <= MAX_Char_limit: 
			word += (" "+line2)
			line2 = word
		elif len(line1) <= MAX_Char_limit: 
			word += (" "+line1)
			line1 = word
			
	Display([line1,
	line2,
	line3,
	line4])

if __name__=="__main__":
	OLED_print("This is a test")
