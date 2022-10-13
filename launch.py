import os, random

random.seed()

# getting the last name of "main.exe"
with open("last_name.txt", "r") as d:
    last_name = d.read()

# getting options for renaming
with open("valid_names.txt", "r") as d:
    options = d.readlines()

# remove "\n" from the entrys
for index, value in enumerate(options):
    if value[-1] == "\n":
        value = value[:-1]
        options[index] = value

# get a random name that is not the same as "last_name"
new_name = "hello"
for i in range(0, 10, 1):
    x = random.choice(options)
    if x != last_name:
        new_name = x
        break
new_name = new_name + ".exe"

# rename the file
os.rename(last_name, new_name)

# save the new name
with open("last_name.txt", "w") as d:
    d.write(new_name)

os.startfile(new_name)