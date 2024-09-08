# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def type_cases(text):
    lower_cases=0
    upper_cases=0
    for letter in text:
      if letter.isupper():
         upper_cases+= 1
      elif letter.isspace():
         continue
      else:
         lower_cases+=1

    return(print(f"There’s {upper_cases} upper cases and {lower_cases} lower cases"))


type_cases("I love Nación Sushi")