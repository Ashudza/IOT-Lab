##display the number of lines and words in a each line#
f1=open(input("open a file:"))
count=0
for i in f1:
	x=i.split()
	count=count+1
	print("the number of words in",count,"the list",len(x))
