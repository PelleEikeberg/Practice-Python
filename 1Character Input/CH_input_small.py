iinnppuutt = input("name and age? please write as ´name, age´")
name, age = iinnppuutt.split(",")
print(name, " will turn 100 years in ", 100-int(age), " years. the year will be ", 2019-int(age) + 100)