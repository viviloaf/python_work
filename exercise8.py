#printing printing printing in python
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
    "I had this thing",
    "That could could type up right.",
    "But it didn't sing.",
    "So I said goodnight"
)
#i am not sure why the last line of input uses both single and double quotes
