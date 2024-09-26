import csv

def mean_grade(grade_1, grade_2, grade_3, grade_4):
  mean=(grade_1 + grade_2 + grade_3 + grade_4)/4
  return mean

def add_new_student():
    try:
        name = input("What is the student's name: ")
        section = input("What is their section: ")
        spanish = number_between_100('Spanish grade: ')
        english = number_between_100('English grade: ')
        social = number_between_100('Social Studies grade: ')
        science = number_between_100('Science grade: ')
        mean = mean_grade(spanish,english,social,science)

        new_student = {
            "full_name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social": social,
            "science": science,
            "mean": mean,

        }
        return new_student
    except ValueError as ex:
        print(f"Invalid input, try again: {ex}")
        add_new_student()

def number_between_100(text):
    while True:
        try:
            grade = int(input(text))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def show_top_3_students(students_list):
  top_3=[]
  sorted_students = sorted(students_list, key=lambda students_list: students_list["mean"],reverse=True)
  if len(sorted_students) > 3:
    for index in range(0,3):
      name = sorted_students[index]['full_name']
      mean = sorted_students[index]['mean']

      add_student = {
              "Name": name,
              "Mean": mean
            }
      top_3.append(add_student)
    return (top_3)
  else:
    for index in range(0,len(sorted_students)):
      name = sorted_students[index]['full_name']
      mean = sorted_students[index]['mean']

      add_student = {
              "Name": name,
              "Mean": mean
            }
      top_3.append(add_student)
  print('''
        //////////////////////
        Top 3 students mean:
        =====================
        ''')
  for index in range(0, len(top_3)):
    print(f'{top_3[index]['Name']}: {top_3[index]['Mean']}')

def print_list(students_list):
  for index in range(0, len(students_list)):
    print(f'''
          ----------------------
          {index+1})
          Name: {students_list[index]['full_name']}
          Section: {students_list[index]['section']}
          Average Grade: {students_list[index]['mean']}
          Spanish: {students_list[index]['spanish']}
          English: {students_list[index]['english']}
          Social Studies: {students_list[index]['social']}
          Science: {students_list[index]['science']}''')

def calculate_general_mean(student_list):
  if student_list==[]:
    print('There are no students')
    print('General Mean: 0')
  else:
    all_grades_sum=0
    for index in range (0, len(student_list)):
      all_grades_sum += float(student_list[index]['mean'])

    general_mean= all_grades_sum/ (len(student_list))
    print(f'''
            General Mean: {general_mean:.2f}
          ''')
    return general_mean


def write_csv_file(file_path, students_list, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(students_list)
    print('The CSV has been saved')

def read_csv_file(file_path):
  data=[]
  with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
    return data