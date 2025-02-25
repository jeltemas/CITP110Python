# add your code to this cell
# remember to include comments like this one for most of your code
# remember to "Run cell" once you're done, excecuting your code so the output is displayed below

while True:
  number = float(input("Enter a positive nonzero number: "))
  if number > 0:
   print ("Valid input")
   break # exit the loop if input is vaild
  else:
    print("error: please enter a positive nonzero number")

