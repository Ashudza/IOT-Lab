#word and character count of a given string#
string=str(input("Enter a sentence:"))
print("the number of character in string with space:",len(string))
char=string.split()
print("the number of words in the string:",len(char))
if(len(string)==0):
  print("toal number of char without space:",len(string)-len(char))
else:
  print("total char without space:",len(string)-len(char)+1)
