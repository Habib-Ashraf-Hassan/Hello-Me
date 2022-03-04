student_name = []
all_students = {}
pass_list = []
failed = []
switch = 1
while switch == 1:
    student = input('Enter the student name:')
    student_name.append(student)
    maths = int(input('Enter the MATHS score of the student:'))
    english = int(input('Enter the ENGLISH score of the student:'))
    science = int(input('Enter the SCIENCE score of the student:'))
    religious_studies = int(input('Enter the RELIGIOUS studies score:'))
    swahili = int(input('Enter the SWAHILI studies score:'))
    total = maths + english + science + religious_studies + swahili
    all_students.update({student: total})
    if total >= 250:
        pass_list.append(student)
    else:
        failed.append(student)
    opt_to_continue = input("Do you wish to continue?(YES/NO)").upper()
    if opt_to_continue == 'NO':
        switch = 0
    elif opt_to_continue == 'YES':
        switch = 1
    else:
        print('Please enter a VALID choice!!')
        opt_to_continue = input("Do you wish to continue?(YES/NO)").upper()
print('Names of students and their marks:')
for i in all_students.items():
    print(i)
print('Students who surpassed the pass mark:')
for i in pass_list:
    print(i)

print('Students that failed i.e will have to repeat the class are:')
for i in failed:
    print(i)
