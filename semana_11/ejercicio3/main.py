from menu import menu
from actions import Student, StudentUtilities, write_csv_file,read_csv_file


headers = (
	'name',
	'section',
	'spanish',
	'english',
  'social',
  'science',
  'mean'
)

def main():
    utilities = StudentUtilities()

    try:
        while exit != True:
          option = int(menu())
          if option == 1:
              students_to_add = int(input('How many students would you like to add: '))
              for student in range(students_to_add):
                  utilities.create_new_student()
          elif option == 2:
              utilities.display_students()
          elif option == 3:
            utilities.show_top_3_students()
          elif option == 4:
            utilities.calculate_general_mean()
          elif option==5:
              data = utilities.transform_obj_to_dic()
              write_csv_file('data.csv',data,headers)
          elif option==6:
            file =read_csv_file('/Users/juanmiguel.badilla/lyfter/semana_10/data.csv')
            if file == []:
              print ('There is no data to be imported in the data.csv file')
            else:
              for student_dict in file:
                student_obj = Student.transform_dic_to_obj(student_dict)
                utilities.add_student(student_obj)
              print ('The CSV has been imported')
          elif option==7:
            break
          else:
            print('Not a valid option in the Menu')

    except ValueError as ex:
        print(f"Option not valid, try again: {ex}")
        main()

main()