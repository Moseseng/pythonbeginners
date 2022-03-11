black_list = ['moses' ,'john' ,'ali' ,'mohamed', 'gggg']      
num_students = int(input("enter number of studen :"))
student_list = []
wehit_list = []
for student in range(num_students):
  prompt = input('input non-name')
  while prompt ==' ':
    prompt = input('input non-name')
  student_list.append(prompt)
for student in student_list:
  if student not in black_list:
    wehit_list.append(student)
print('THese' + str(len(wehit_list))+ "students are allowed to graduate.")
print(*sorted(wehit_list) ,sep='\n')
