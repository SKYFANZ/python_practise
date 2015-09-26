## Get the user input of Binary

getTheBinary = raw_input("Enter the Binary: ")

flag = True
count = 0
## Check the user input, make sure IT IS A BINARY

while flag:
		
	if count > 0:
		getTheBinary = raw_input("Enter the Binary again: ")
	try:
		convertToNumber = abs(int(getTheBinary))
		checkWhetherItisNegative = int(getTheBinary[0])
		flag = False
	except:
		print getTheBinary + " is not a Binary" 	
	finally:
		count = 1

theResult = 0

## Calculate the binary into number
	
for number in range(len(getTheBinary)):
	theResult += int(getTheBinary[len(getTheBinary)-1-number])*2**number	

## Print the result

print "The corresponding number of Binary "+getTheBinary+" is : "+str(theResult)

