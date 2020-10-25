def reverse(x):
	a = str(x)
	mark = ""
	new_s = []
	if a[0].isdigit() == False:
		mark = a[0]
		a = a[1:]
	if a[-1] =="0":
		a = a[:-1]

	for i in range(len(a)):
		new_s.append(a[len(a)-i-1])
			# print(a[i])
			# print(a[len(a)-i-1])
	a = "".join(new_s)
	a = mark+a
	return int(a)

print(reverse(120))
