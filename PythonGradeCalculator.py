#Mitchell Boesche

print("Welcome to Mitchell's Grade Calculator!")
print("---------------------------------------")
grade = float(0)
totalweight = float(0)
go = int(1)

while go == 1:
    weight = float(input("Please enter the weight of the category!: "))
    totalweight = totalweight + weight
    possible = float(input("Please enter the total amount of possible points!: "))
    earned = float(input("Please enter the number of points earned!: "))
    points = (earned/possible) * weight
    grade = grade + points
    go = int(input("1 = Another Category or 0 = Done: "))

if totalweight > 100:
    print("----------------------------------")
    print("Error! Total weight cannot be greater than 100!")
    print("----------------------------------")

elif grade >= 90:
    print("----------------------------------")
    print("Your grade is ",grade, " which is an A!")
    print("----------------------------------")
    
elif grade >= 80:
    print("----------------------------------")
    print("Your grade is ",grade, " which is a B!")
    print("----------------------------------")
    
elif grade >= 70:
    print("----------------------------------")
    print("Your grade is ",grade, " which is a C!")
    print("----------------------------------")
    
elif grade >= 60:
    print("----------------------------------")
    print("Your grade is ",grade, " which is a D!")
    print("----------------------------------")
    
else:
    print("----------------------------------")
    print("Your grade is ",grade, " which is a F!")
    print("----------------------------------")