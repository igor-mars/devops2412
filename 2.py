a = 4
b = 14
if a < b:
    print('a is lower')

fname = "igor"
lname = "shainsky"
full_name = "igor" + "shainsky"
another_full_name = "%s %s" % ("igor", "Shainsky")
another_full_name2 = f"{fname} {lname}"
another_full_name3 = "{} {}".format(fname, lname)
print(full_name)
print(another_full_name)
print(another_full_name2)
print(another_full_name3)

my_full_description = "name: \"igor\"\nmarried: yes\nage: 55"
print(my_full_description)
