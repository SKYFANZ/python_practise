getTheInput = int(float(raw_input("Enter a dicimal number: ")))

if getTheInput < 0:
	isNeg = True
else:
	isNeg = False

getTheInput = abs(int(getTheInput))	
result = ""

if getTheInput == 0:
	result = "0"

while getTheInput > 0:
	result = str(getTheInput%2) + result
	getTheInput = getTheInput/2

if isNeg:
	result = "-" + result

print result

