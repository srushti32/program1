import sys
#check if correct number of argu
if len (sys.argv)! = 3:
print("uasge: python student.py <name><rollno>")
#sys.argv[0] is always the program name
script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]

print("script name:",script_name)
print("student name:",name)
print("roll number:",rollno)
