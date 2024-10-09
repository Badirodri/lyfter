import csv

class Student:
  students_list=[]
  general_mean=0

  def __init__(self, name='', section='', spanish=0, english=0,social=0,science=0, mean=0):
    self.name = name
    self.section = section
    self.spanish = spanish
    self.english = english
    self.social = social
    self.science = science
    self.mean= mean

  def add_new_student(self):
      try:
          self.name = input("What is the student's name: ")
          self.section = input("What is their section: ")
          self.spanish = number_between_100('Spanish grade: ')
          self.english = number_between_100('English grade: ')
          self.social = number_between_100('Social Studies grade: ')
          self.science = number_between_100('Science grade: ')
          mean = (self.spanish+self.english+self.social+self.science)/4

          new_student = {
              "full_name": self.name,
              "section": self.section,
              "spanish": self.spanish,
              "english": self.english,
              "social": self.social,
              "science": self.science,
              "mean": mean,
          }
          self.students_list.append(new_student)
          print(self.students_list)
          return new_student
      except ValueError as ex:
          print(f"Invalid input, try again: {ex}")

  def print_list(self):
    for index in range(0, len(self.students_list)):
      print(f'''
            ----------------------
            {index+1})
            Info: {self.students_list[index]}
            ''')


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