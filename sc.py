def y():
	ty=str(input("Enter a number operation (+, -, /, *, **, %):"));
	if ty == "+":
		num1=int(input("Enter your 1st number:"));
		num2=int(input("Enter your 2nd number:"));
		print(num1+num2);
	elif ty == "-":
		num1=int(input("Enter your 1st number:"));
		num2=int(input("Enter your 2nd number:"));
		print(num1-num2);
	elif ty == "/":
		num1=int(input("Enter your 1st number:"));
		num2=int(input("Enter your 2nd number:"));
		print(num1/num2);
	elif ty == "*":
		num1=int(input("Enter your 1st number:"));
		num2=int(input("Enter your 2nd number:"));
		print(num1*num2);
	elif ty == "**":
		num1=int(input("Enter your 1st number:"));
		num2=int(input("Enter your 2nd number:"));
		print(num1**num2);
	elif ty == "%":
		num1=int(input("Enter your 1st number:"));
		num2=int(input("Enter your 2nd number:"));
		print(num1%num2);
	else: print("Sorry, try a listed function")
	again = input("Again?(yes/no)");
	if again =="yes":
		y()
	elif again == "no":
		print("Bye and have a great day!");
	else:
		print("Sorry, did not understand!");
		
y()
