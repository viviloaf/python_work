#Strings and Text

#stringception is here
types_of_people = 10
x = f"There are {types_of_people} types of people."

#stringception is here
binary = "binary"
do_not = "don't"
y = f"Those do know {binary} and those who {do_not}"

print (x)
print (y)

#stringception is here
print(f"I said: {x}")
print(f"I also said: '{y}'")

#stringception is here
hillarous = False
joke_evaluation = "Isn't that joke so funny?! {}"

#stringception is not here, this is a boolean
print(joke_evaluation.format(hillarous))

w = "This is the left side of..."
e = "a string with a right side."

#This makes a big string because you have two baby string put together end to end added like abcd + efgh = abcdefgh
print (w + e)

#note
# "" and '' are the same damn thing in python
#The differences are used for clarification. Usual style includes this format:
# blah_blah = 17
# derp = "I am a '{blah_blah}'"
#The '' are used inside of "", technically you could go the other way but it would make no god damn sense so don't do it
#don't be a rebel
