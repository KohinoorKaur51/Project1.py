
def student_report():
    print("----BATCH PROGRESS TRACKER----")

    name = input("Enter student name: ")
    roll_no = int(input("Enter roll no: "))

    PSP_marks = float(input("Enter PSP marks : "))
    Maths_marks = float(input("Enter Maths marks: "))
    SAE_marks = float(input("Enter SAE marks: "))
    Attendance = float(input("Enter attendance: "))

    if (PSP_marks < 0 or PSP_marks>100 or Maths_marks<0 or Maths_marks>100 or SAE_marks<0 or SAE_marks>100 or Attendance<0 or Attendance>100):
        print("Invalid marks or attendance!") 
        return

    average = (PSP_marks + Maths_marks + SAE_marks)/3

    print("----STUDENT PROGRESS REPORT----")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Average Marks:", round(average,2), "%")
    print("Attendance:", Attendance, "%")

    if average >= 75 and Attendance >= 75:
        print("Status: On Track")
    elif average>=50 and Attendance>=75:
        print("Status: Needs Improvement")
    else:
        print("Status: Academic Support Required")

    if PSP_marks<40:
        print("Focus Area: program solving with Python")
    if Maths_marks<40:
        print("Focus Area: Mathematics")
    if SAE_marks<40:
        print("Focus Area: System and AI Essentials")

student_report()