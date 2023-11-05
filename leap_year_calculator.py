def leapyear(year):
	if 1000<= year <= 9999:

		if year % 4 == 0: 
			return True

		else:
			return False	 
	else:
		result ="ERROR"
		return result

inputyear = int(input("4桁の西暦年を入力："))

result = leapyear(inputyear)
if result == "ERROR":
	print("４桁を数値を入力してください")
elif result ==True:
	print(inputyear,"年は閏年です。")
else :
	print(inputyear,"年は平年です。")