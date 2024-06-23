#     creating tuples!


#    TUPLE: screen.draw.text("p", color = "pink"., midtop = (30,30), fontsize = 3)
#    parentheses: syntax
#    inside parentheses: parameters
#    parentheses inside parentheses: ex: coordinates, tuple (MOST CASES)
#    tuple: the parentheses inside a function or a set of parentheses that can stand alone CHANGE: ANYTHING THAT CAN STAND ALONE IN MOST CASES



address = (3333, "meow street", "cat land", "cat nation", 929292)

for unit in address:
    print(unit)

marks = 100, 99, 98

print(marks)

#    creating nested tuples!

cat = ("calico", "tabby", ["striped", "tortoise", "CAT", "KITTYY"], (1, 2, 3))

#    calico

print(cat[1])

#    tuple

print(cat[3])

#    tortoise

print(cat[2][1])

#    1

print(cat[3][0])

#    print t in tabby

print(cat[1][0])

#    print tabby and list using slice operator

print(cat[1:2], cat[1:3])

#    NEGATIVE INDEXING WITH SLICE OPERATOR (list to tuple)

print(cat[-2:])