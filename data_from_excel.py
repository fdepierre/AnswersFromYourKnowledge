
import openpyxl

""" 
Read each line of the first tab of an Excel file 
and store cullumn 1 as questions and cullumn 2 as response
"""
def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    questions = []
    answers = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        questions.append(row[0])
        answers.append(row[1])
    return questions, answers


