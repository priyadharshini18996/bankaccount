def user_input():
    pass
student_roll_no=raw_input("Enter roll number:")
student_name=raw_input("Enter student name:")
subjects=("English","Physics","Chemistry","Biology")
percentage=""

english=input("Enter English Mark : ")
physics=input("Enter Physics Mark : ")
chemistry=input("Enter Chemistry Mark : ")
biology=input("Enter Biology Mark : ")

total=english+physics+chemistry+biology
print "Total marks obtained by student --->" ,total


def grade():
    if(percentage  >= 60):
        print "  congrats  " ,student_name 
        print "***first class***"

    elif (percentage < 60 and percentage  >= 45):
        print "  congrats  " ,student_name 
        print "***second class***"

    else:
        print "fail-***detained in the same class***"

percentage=total/4
print "scored% :",percentage
user_input()
grade()