for i in range(0,3):
    name=input("name of student:")
    roll_no=int(input("enetr the rollno:"))
    marks_of_course1=int(input("enter the marks of course 1:"))
    marks_of_course2=int(input("enter the marks of course 2:"))
    marks_of_course3=int(input("enter the marks of course 3:"))
    total_marks_obtained=marks_of_course1+marks_of_course2+marks_of_course3
    percentage=(total_marks_obtained)/300*100
    print("name of student=",name)
    print("roll no of the student=",roll_no)
    print("total marks obtained by student=",total_marks_obtained)
    print(f"percentage of student={percentage:.2f}")

