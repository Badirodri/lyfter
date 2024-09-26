from menu import menu
from actions import add_new_student, show_top_3_students, print_list, calculate_general_mean,write_csv_file, read_csv_file

headers = (
	'full_name',
	'section',
	'spanish',
	'english',
  'social',
  'science',
  'mean'
)

def main():
    students = []
    general_mean=0
    exit = False
    try:
        while exit != True:
          option = int(menu())
          if option == 1:
              students_to_add = int(input('How many students would you like to add: '))
              for student in range(students_to_add):
                  new_student = add_new_student()
                  students.append(new_student)
          elif option == 2:
              if students== []:
                print('There are not any students added')
              else:
                print('The list of existing students is the following: ')
                print_list(students)
          elif option == 3:
            if students == []:
              print('There are not any students to show')
            else:
              show_top_3_students(students)
          elif option == 4:
            calculate_general_mean(students)
          elif option==5:
            if students == []:
              print('There are not students to export, add some first')
            else:
              write_csv_file('data.csv',students,headers)
          elif option==6:
            file =read_csv_file('/Users/juanmiguel.badilla/lyfter/semana_10/data.csv')
            if file == []:
              print ('There is no data to be imported in the data.csv file')
            else:
              students=file
              print ('The CSV has been imported')
          elif option==7:
            break
          else:
            print('Not a valid option in the Menu')

    except ValueError as ex:
        print(f"Option not valid, try again: {ex}")
        main()

main()