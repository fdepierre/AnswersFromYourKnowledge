import openpyxl

class DataFromExcel:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_excel(self):
        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook.active
        questions = []
        answers = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            questions.append(row[0])
            answers.append(row[1])
        return questions, answers