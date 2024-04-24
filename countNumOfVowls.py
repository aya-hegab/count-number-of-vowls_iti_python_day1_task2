# myStr = "ahmed Hegab"
myStr = input("Enter myString: ")
count = 0
for i in myStr.lower():
      if(i in ('a', 'e', 'i', 'o', 'u')):
            count = count + 1

print(count)