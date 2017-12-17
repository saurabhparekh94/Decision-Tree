
'''
this is the output of the decision tree training file. it actually creates a decisionr tree in the form of if-else
condition.
this file is arounf 6 level long.
'''



input1=[]
flag=False
total_greyhound=0
total_wippet=0
targets=[]
with open('HW_05C_DecTree_TESTING__FOR_STUDENTS__v540.csv') as file:
	for lines in file:
		lines = lines.strip().split(',')
		if flag == False:
			flag = True
		else:
			input1.append([float(lines[0]), float(lines[1]), float(lines[2]), float(lines[3]), float(lines[4]),float(lines[5])])
ans=[]
for item in range(len(input1)):
	if input1[item][4] <2.86:
		if input1[item][2] <8.17:
			if input1[item][3] <0.01:
				if input1[item][0] <8.13:
					ans.append("Greyhound")
				elif input1[item][0] >=8.13:
					ans.append("Whippet")
			elif input1[item][3] >=0.01:
				if input1[item][5] <2.93:
					if input1[item][3] <2.99:
						ans.append("Greyhound")
					elif input1[item][3] >=2.99:
						ans.append("Whippet")
				elif input1[item][5] >=2.93:
					if input1[item][3] <3.87:
						if input1[item][5] <4.85:
							ans.append("Greyhound")
						elif input1[item][5] >=4.85:
							ans.append("Whippet")
					elif input1[item][3] >=3.87:
						if input1[item][5] <4.93:
							ans.append("Whippet")
						elif input1[item][5] >=4.93:
							ans.append("Greyhound")
		elif input1[item][2] >=8.17:
			ans.append("Greyhound")
	elif input1[item][4] >=2.86:
		if input1[item][3] <4.0:
			if input1[item][5] <4.86:
				ans.append("Greyhound")
			elif input1[item][5] >=4.86:
				if input1[item][3] <3.82:
					ans.append("Whippet")
				elif input1[item][3] >=3.82:
					ans.append("Greyhound")
		elif input1[item][3] >=4.0:
			if input1[item][5] <4.81:
				ans.append("Whippet")
			elif input1[item][5] >=4.81:
				ans.append("Greyhound")
with open('HW_05_MyClassification.csv','w') as myfile:
	for lines in range(len(ans)):
		row= ans[lines]
		myfile.write(row)
		myfile.write('\n')