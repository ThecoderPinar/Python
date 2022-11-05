from datetime import*

birth = datetime.strptime(input("Your birth date (d.m.Y): "), "%d.%m.%Y")
age = datetime.now() - birth

print("You survived {} seconds.".format(age.total_seconds()))