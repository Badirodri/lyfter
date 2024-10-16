import csv

class Student:

  def __init__(self, name, section, spanish, english, social, science, mean):
    self.name = name
    self.section = section
    self.spanish = spanish
    self.english = english
    self.social = social
    self.science = science
    self.mean= mean

  def show_student(self):
    return(f'''
           Name: {self.name}
           Section: {self.section}
           Spanish: {self.spanish}
           English: {self.english}
           Social Studies: {self.social}
           Science: {self.science}
           ''')

  @classmethod
  def transform_dic_to_obj(cls, dic):
    return cls(
        name=dic.get('name'),
        section=dic.get('section'),
        spanish=int(dic.get('spanish')),
        english=int(dic.get('english')),
        social=int(dic.get('social')),
        science=int(dic.get('science')),
        mean=float(dic.get('mean'))
    )

class StudentUtilities:
  def __init__(self):
    self.student_list=[]
    self.general_mean=0

  def get_general_mean(self, student):
    return student.mean

  def add_student(self, student):
    self.student_list.append(student)

  def create_new_student(self):
      try:
          name = input("What is the student's name: ")
          section = input("What is their section: ")
          spanish = self.number_between_100('Spanish grade: ')
          english = self.number_between_100('English grade: ')
          social = self.number_between_100('Social Studies grade: ')
          science = self.number_between_100('Science grade: ')
          mean = (spanish+english+social+science)/4

          new_student = Student(name, section, spanish, english, social, science, mean)

          self.student_list.append(new_student)
          return new_student
      except ValueError as ex:
          print(f"Invalid input, try again: {ex}")

  def number_between_100(self, text):
    while True:
        try:
            grade = int(input(text))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

  def display_students(self):
        if not self.student_list:
            print("No students found.")
        else:
            print("List of Students:")
            for student in self.student_list:
                print(student.show_student())

  def show_top_3_students(self):
    if not self.student_list:
            print("No students to display.")
            return
    else:
        sorted_students = sorted(self.student_list, key=self.get_general_mean, reverse=True)
        top_3 = sorted_students[:3]
        print("Top 3 Students:")
        for student in top_3:
            print(student.show_student())

  def get_general_mean(self, student):
    return student.mean

  def calculate_general_mean(self):
    if self.student_list==[]:
      print('There are no students')
      print('General Mean: 0')
    else:
      all_grades_sum=0
      for student in self.student_list:
        all_grades_sum += self.get_general_mean(student)

      self.general_mean= all_grades_sum/ (len(self.student_list))
      print(f'''
              General Mean: {self.general_mean:.2f}
            ''')
      return self.general_mean

  def transform_obj_to_dic(self):
    if self.student_list==[]:
      print('There are not students to export, add some first')
    else:
      list = []
      for student in self.student_list:
        list.append(student.__dict__)
      return list



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