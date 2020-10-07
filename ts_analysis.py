global a,b
a = input()
a = int(a)
b = a%4
print("輸入的年份:",a)
if b == 0:
  c = a%100
  if c == 0:
    d = a%400
    print("該年為閏年") 
  else:
    print("該年不為閏年")
else:
  print("該年不為閏年")
