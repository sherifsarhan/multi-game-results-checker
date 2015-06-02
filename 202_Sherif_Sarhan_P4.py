#-------------------------------------------------------------------------------
# Sherif Sarhan.
# This is a program designed to check the result of tic-tac-toe, sudoku,
# and connect four games.
#-------------------------------------------------------------------------------
#Creates a menu.
menu = '''
0 - check a finished tic-tac-toe
1 - check a finished sudoku
2 - check a finished connect four
3 - quit'''
#Creates a value to loop the menu again or not.
menuLoop = True
#Loops while menuLoop is true.
while (menuLoop):
	#Prints menu.
	print(menu)
	
	#Asks user for option selection.
	option_select = int(input("\nChoose your option: "))
	
	#Checks if user chose option 0.
	if option_select == 0:
		print("\nOK. Tic-tac-toe.\n")
		
		#Gets string input from user for first row and turns to list.
		first_row = list(input("top row   : "))
		
		#Gets string input from user for second row and turns to list.
		second_row = list(input("middle row: "))
		
		#Gets string input from user for third row and turns to list.
		third_row = list(input("bottom row: "))
		
		#Creates a new list of all the lists.
		complete_board = [first_row,second_row,third_row]
		
		#Creates a list of accepted symbols.
		acceptedSymbols = ["x","X","o","O","."]
			
		#Creates empty lists for each column and combines all into one list.
		first_column = []
		second_column = []
		third_column = []
		complete_columns = [first_column,second_column,third_column]
		
		#Takes each row in the complete board.
		for eachRow in complete_board:
			#Takes specific index of each row and appends to specific column.
			first_column.append(eachRow[0])
			second_column.append(eachRow[1])
			third_column.append(eachRow[2])
		
		#Sets the first diagonal from its row index.
		diagonal_one = [first_row[0],second_row[1],third_row[2]]
		
		diagonal_two = [first_row[2],second_row[1],third_row[0]]
		
		#Combines both diagonals into one list.
		diagonal_both = [diagonal_one,diagonal_two]

		#Creates counter for xs.
		xsCount = 0
		#Creates counter for os.
		osCount = 0
		
		#Boolean that x starts as not winning.
		xwins = False
		#Boolean that o starts as not winning.
		owins = False
		#Variable for the while loop to keep looping or not.
		keepgoing = True
		
		#Loops through every row in the complete_board list.
		for eachList in complete_board:
			#Checks if the length of each row is less than the valid.
			if len(eachList) < 3:
				print("invalid board - too few symbols")
			#Checks if the length of each row is more than the valid.
			if len(eachList) > 3:
				print("invalid board - too many symbols")
			
			#Loops through every symbol in each row.
			for eachSymbol in eachList:
				#Checks if each symbol is accepted.
				if eachSymbol not in acceptedSymbols:
					print("invalid board - invalid symbol "+"'"+eachSymbol+"'")
			
				#Condition for every symbol that is in the xs list.
				if eachSymbol == "x" or eachSymbol == "X":
					#Adds 1 to the counter for every instance..
					xsCount += 1
					
				#Condition for every symbol that is in the os list.
				if eachSymbol == "o" or eachSymbol == "O":
					#Add 1 to the counter for every instance.
					osCount += 1
			
		#Checks if the xs are more than the os by a difference of 1.
		if (xsCount) - (osCount) > 1:
			print("invalid board - x took too many turns")
			#Tells while loop to not check for a winner.
			keepgoing = False
		#Checks if the os are more than the xs.
		elif (xsCount) < (osCount):
			print("invalid board - o took too many turns")
			#Tells while loop to not check for a winner.
			keepgoing = False
		
		#Checks for a winner while keepgoing is true.
		while (keepgoing == True):	
			#Loops through every row in the complete_board list.
			for eachList in complete_board:
				#Creates a counter to count xs in a row.
				xwincount = 0
				#Creates a counter to count os in a row.
				owincount = 0	
				#Pulls each symbol in each list.
				for eachSymbol in eachList:
					#Checks if symbol is a move by x.
					if eachSymbol == "x" or eachSymbol == "X":
						#Adds 1 to counter variable for x in row.
						xwincount += 1
						#Checks if x counter variable in row is 3.
						if xwincount == 3:
							print("valid - x is the winner")
							#Stores the truth of x winning.
							xwins = True
							#Tells the while loop to stop checking.
							keepgoing = False
					#Checks if symbol is a move by o.
					if eachSymbol == "o" or eachSymbol == "O":
						#Adds 1 to counter for how many os in row.
						owincount += 1
						#Checks if o counter in row is 3.
						if owincount == 3:
							print("valid - o is the winner")
							#Stores truth value of o winning.
							owins = True
							#Tells while loop to stop checking.
							keepgoing = False
							#Scenario if both x and o winning are true.
							if xwins and owins:
								print("Nobody is the winner.")		
			
			#Pulls each column from the entire list of columns.
			for eachColumn in complete_columns:
				#Counters to count xs and os in each column.
				xcolumnCount = 0
				ocolumnCount = 0
				#Pulls each value from each column.
				for eachValue in eachColumn:
					#Checks if is x move.
					if eachValue == "x" or eachValue == "X":
						#Counts instance of x in each column.
						xcolumnCount += 1
						#Checks if 3 xs in column.
						if xcolumnCount == 3:
							print("valid - x is the winner")
							xwins = True
							keepgoing = False
					#Checks if is o move.
					if eachValue == "o" or eachValue == "O":
						ocolumnCount += 1
						#Checks if 3 os in column.
						if ocolumnCount == 3:
							print("valid - o is the winner")
							owins = True
							keepgoing = False
			
			#Pulls each diagonal from the entire diag. list.
			for eachDiag in diagonal_both:
				xdiagCount = 0
				odiagCount = 0
				#Pulls each diag. value from each diag.
				for eachVal in eachDiag:
					#Check if x move.
					if eachVal == "x" or eachVal == "X":
						#Counter for xs in each diag.
						xdiagCount += 1
						if xdiagCount == 3:
							print("valid - x is the winner")
							xwins = True
							keepgoing = False
					#Check if o move.
					if eachVal == "o" or eachVal == "O":
						odiagCount += 1
						#Check if o move.
						if odiagCount == 3:
							print("valid - o is the winner")
							owins = True
							keepgoing = False
		
			#Checks if xwins and owins boolean values unchanged.
			if xwins == False and owins == False:
				print("valid - nobody is the winner.")
				keepgoing = False
		
		
	
	#Checks if user chose option 1.
	elif option_select == 1:
		print("\nOK. Sudoku.\n")
		
		all_rows = []
		rowCounter = 0
		accepted_symbols = ["1","2","3","4","5","6","7","8","9"]
		too_many = False
		too_few = False
		invalid_symbol = False
		bad_row = False
		
		#Checks for too many or too few symbols in rows.
		while rowCounter < 9:
			rowCounter += 1
			row_input = list(input("row " + str(rowCounter) + ": "))
			if len(row_input) < 9:
				too_few = True
				print("invalid board - too few symbols")
			if len(row_input) > 9:
				too_many = True
				print("invalid board - too many symbols")
			all_rows.append(row_input)
		
		#Checks for invalid symbols and for duplicate numbers in rows.
		if too_few == False and too_many == False:	
			for eachRow in all_rows:
				for eachRow_value in eachRow:
					if eachRow_value not in accepted_symbols:
						print("invalid board - invalid symbol ","'",eachRow_value,"'")	
						bad_row = True
					if eachRow.count(eachRow_value) > 1:
						bad_row = True
		
			if bad_row == True:
				print("invalid board - bad row")
			
		#Creates lists for the new columns
		first_column = []
		second_column = []
		third_column = []
		fourth_column = []
		fifth_column = []
		sixth_column = []
		seventh_column = []
		eighth_column = []
		nineth_column = []
		#Puts all columns into one list.
		all_columns = [first_column,second_column,third_column,fourth_column\
		,fifth_column,sixth_column,seventh_column,eighth_column,nineth_column]
		
		everythingok = False
		#In the case that the rows don't have any errors.
		if bad_row == False and too_few == False and too_many == False:
			#That means everything is ok.
			everythingok = True
		
		bad_column = False
		#Deals with columns if everything is ok with the rows..
		if everythingok == True:	
			#Puts indexes of rows into their specific columns.
			for eachRow in all_rows:
				first_column.append(eachRow[0])
				second_column.append(eachRow[1])
				third_column.append(eachRow[2])
				fourth_column.append(eachRow[3])
				fifth_column.append(eachRow[4])
				sixth_column.append(eachRow[5])
				seventh_column.append(eachRow[6])
				eighth_column.append(eachRow[7])
				nineth_column.append(eachRow[8])
				
			
			bad_column = False
			#Checks if the columns have number duplicates.
			for eachColumn in all_columns:
				for eachColumn_value in eachColumn:
						if eachColumn.count(eachColumn_value) > 1:
							bad_column = True
		
			if bad_column == True:
				print("invalid board - bad column")
		
		#Checks for bad group with a quad-nested for loop.
		bad_group = False
		if everythingok == True:
			for i in range(0,9,3):
				for j in range(0,9,3):
					group = []
					for x in range(3):
						for y in range(3):
							group.append(all_rows[i+x][j+y])						
		
					#Checks for duplicates in each group.
					for each_val in group:
						if group.count(each_val) > 1:
							bad_group = True
							#Begins series of breaks to exit all the loops.
							break
					if bad_group == True:
						break
				if bad_group == True:
					break
		
			#If bad group, print bad group.
			if bad_group == True:
				print("invalid board - bad group")
			
			#Else, print valid since all conditions are met.
			if bad_group == False:
				print("this sudoku is valid")
				
	#Checks if user chose option 2.
	elif option_select == 2:
		print("\nOK. Connect four.\n")
		
		#Gets how many rows.
		x = 0
		while (x == 0):
			howmany_rows = int(input("How many rows: "))
			if howmany_rows < 4:
				print("Too few rows.")
			else:
				x = 1
		
		#Gets how many columns.
		x = 0
		while (x == 0):	
			howmany_columns = int(input("How many columns: "))
			if howmany_columns < 4:
				print("Too few columns")
			else:
				x = 1
		
		#Prints how many rows and columns the user entered.
		print("\nOK. ",howmany_rows," rows and ",howmany_columns," columns.\n")
		
		
		all_rowsConnect = []
		invalid_symbolCount = False
		accepted_symbolsConnect = ["x","X","o","O","."]
		
		#Gets user input for the rows.
		print("give me the rows from top down")
		for i in range(howmany_rows):
			each_row = list(input("next row: "))
			all_rowsConnect.append(each_row)
		
		#Checks if the length of each row is too few.
		for each_row in all_rowsConnect:
			if len(each_row) < (howmany_columns):
				print("invalid board - too few symbols in row")
				invalid_symbolCount = True
		
		#Checks if the length of each row is too many.
		for each_row in all_rowsConnect:
			if len(each_row) > (howmany_columns):
				print("invalid board - too many symbols in row")
				invalid_symbolCount = True
		
		#Checks if there are any invalid symbols in each row.
		for each_row in all_rowsConnect:	
			for eachVal in each_row:
				if eachVal not in accepted_symbolsConnect:
					print("invalid game - invalid symbol ",eachVal)
		
		
		all_columnsConnect = []
		count = 0
		#Converts board into columns.
		for each_col in range(howmany_columns):		
			each_columnConnect = []
			for each_row in range(howmany_rows):		
				each_columnConnect.append(all_rowsConnect[each_row][each_col])
			all_columnsConnect.append(each_columnConnect)		
		
		airGap = False
		#Checks for air gap.
		for eachColumn in all_columnsConnect:	
			eachColumnString = (''.join(eachColumn))
			if "x." in eachColumnString or "X." in eachColumnString:
				airGap = True
			if "o." in eachColumnString or "O." in eachColumnString:
				airGap = True
		if airGap == True:
			print("invalid board - air gap.")
		
		xnum_Connect = []
		onum_Connect = []
		#Checks if x or o took too many moves.
		for eachRow in all_rowsConnect:
			for eachVal in eachRow:
				if eachVal == "x" or eachVal == "X":
					xnum_Connect.append(eachVal)
				if eachVal == "o" or eachVal == "O":
					onum_Connect.append(eachVal)
		if len(xnum_Connect) < len(onum_Connect):
			print("invalid board - o took too many turns")
		if (len(xnum_Connect) - len(onum_Connect)) > 1:
			print("invalid board - x took too many turns")
		
		pleasebreak = False
		xwinsConnect = False
		owinsConnect = False
		#Checks if there is an air gap so it can continue.
		if airGap == False:
			#Checks for winner.
			for eachRow in all_rowsConnect:
				xcountConnect = 0
				ocountConnect = 0
				for eachVal in eachRow:
					#Checks if x wins.
					if eachVal == "x" or eachVal == "X":
						xcountConnect += 1
					if xcountConnect == 4:
						xwinsConnect = True
					if xcountConnect >= 1:
						if eachVal == "." or eachVal == "o" or eachVal == "O":
							pleasebreak = True
							break
					#Checks if o wins.
					if eachVal == "o" or eachVal == "O":
						ocountConnect += 1
					if ocountConnect == 4:
						owinsConnect = True
					if ocountConnect >= 1:
						if eachVal == "." or eachVal == "x" or eachVal == "X":
							pleasebreak = True
							break
		
		#Connect Four attempt.
		xdiagCount = 0
		odiagCount = 0
		xwinDiag = True
		owinDiag = False
		z = 0
		y = 0
		dudebreak = False
	
		for i in range(howmany_columns):
			for k in range(howmany_rows): 
				if all_rowsConnect[k-z][i-y] == "x":
					xdiagCount += 1
					z += 1
					y += 1
				if xdiagCount == 4:
					xwinDiag = True
				if z == howmany_rows:
					dudebreak = True
					break
				if y == howmany_columns:
					dudebreak = True
					break
			if dudebreak == True:
				break
		z = 0
		y = 0
		
		for i in range(howmany_columns):
			for k in range(howmany_rows): 
				if all_rowsConnect[k-z][i-y] == "o":
					odiagCount += 1
					z += 1
					y += 1
				if odiagCount == 4:
					owinDiag = True
				if z == howmany_rows:
					dudebreak = True
					break
				if y == howmany_columns:
					dudebreak = True
					break
			if dudebreak == True:
				break

		
		if xwinDiag == True:
			print("X wins diag.")
		if owinDiag == True:
			print("O wins diag.")
			
		
		
		#Checks who wins to see what to print.
		if xwinsConnect == True:
			print("valid board - x is the winner.")				
		
		if owinsConnect == True:
			print("valid board - o is the winner.")
			
		space_left = False
		for eachRow in all_rowsConnect:
			for eachVal in eachRow:	
				if eachVal == ".":
					space_left = True
		
		if xwinsConnect == False and owinsConnect == False and space_left == False:
			print("valid game - no winner.")
		
		if xwinsConnect == False and owinsConnect == False and space_left == True:
			print("invalid game - no winner and space left.")
		
	
	#Checks if user chose option 3.
	elif option_select == 3:
		print("\nOK. Quit.")
		menuLoop = False
	
	#Checks if user chose an invalid option.
	else:
		menuLoop = True
		