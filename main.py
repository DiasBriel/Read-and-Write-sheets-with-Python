from os.path import split
from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '' #your sheet ID

def get_total_of_class():
    total_of_class = read_sheets('example!A2:H2')
    text_split = total_of_class[0][0].split()
    total_class = text_split.pop()
    return round(int(total_class))

total_of_class = get_total_of_class()

def check_faults(faults):
    faults = int(faults)
    percentage_faults = faults * 100 / total_of_class
    return(round(percentage_faults))

def sum_grades_and_return_average(*args):
    values = args[0][1:]
    soma = 0
    for value in values:
        soma += int(value)
        result = soma / 3
        return round(result)

def calculate_result_students(list_with_grades = []):
    possible_results = ("Reprovado por Nota", "Exame Final", "Aprovado", "Reprovado por Falta")
    final_results = []

    for grades in list_with_grades:

        average = sum_grades_and_return_average(grades)
        percentage_faults = check_faults(grades[0])

        if percentage_faults > 25:
            final_results.append([possible_results[3], possible_results[3]])
        
        if percentage_faults <= 25:
            if average < 50:
                final_results.append([possible_results[0], average])
            if  average >= 50 and average < 70:
                final_results.append([possible_results[1], average])
            if average >= 70:
                final_results.append([possible_results[2], '0'])
    return final_results

where_read = "example!C4:F27" #The range of column and row that will be read
grades_of_students = read_sheets(where_read)
final_results_text = calculate_result_students(grades_of_students)
print(final_results_text)

write_final_result(final_results_text)
          

