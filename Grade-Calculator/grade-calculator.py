name = input("Enter your name: ")

sub1 = input("enter subject 1 name: ")
m1 = int(input(f"{sub1} marks: "))

sub2 = input("enter subject 2 name: ")
m2 = int(input(f"{sub2} marks: "))

sub3 = input("enter subject 3 name: ")
m3 = int(input(f"{sub3} marks: "))

average = (m1 + m2 + m3) / 3

print("total average: ", average)

if average >= 80:
    print('your grade is A+')
elif average >= 70:
    print('your grade is A')
elif average >= 60:
    print('your grade is B')
elif average >= 50:
    print('your grade is C')
elif average >= 40:
    print('your grade is D')
else:
    print('your grade is F')
