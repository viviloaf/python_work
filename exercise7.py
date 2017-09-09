#this is more printing in python

print "Mary had a little lamb."
print"Its fleece was white as %s." % 'snow'
#the % prints a string that is declared later in the same line, it can be used in place of a veriable when you want to print a global variable that is declared elsewhere
print"And everywhere that Mary went."
print"." * 10 #figure out what this does in code
#this acts as a multiplier and prints x10 of the string '.'

endl1 = "C"
endl2 = "h"
endl3 = "e"
endl4 = "e"
endl5 = "s"
endl6 = "e"
endl7 = "B"
endl8 = "u"
endl9 = "r"
endl10 = "g"
endl11 = "e"
endl12 = "r"

#Watch the comma at the end, and see what happens when you remove it
print endl1 + endl2 + endl3 + endl4 + endl5 + endl6,
#the comma adds a physical space and prints both words on the same line
print endl7 + endl8 + endl9 + endl10 + endl11 + endl12

print endl1 + endl2 + endl3 + endl4 + endl5 + endl6
#without the ',' , the words print on different lines in the command prompt
print endl7 + endl8 + endl9 + endl10 + endl11 + endl12
