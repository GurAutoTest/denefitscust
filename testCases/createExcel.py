
#*************************************
 # CREATE EXCEL FILE FUNCTIONS START *
 #*************************************
import openpyxl
class MyObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def create_objects_from_json(json_obj):
    return [MyObject(**json_obj)]

def write_objects_to_excel(file, sheet_name, objects):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name

    # Write headers
    headers = list(objects[0].__dict__.keys())
    sheet.append(headers)

    # Write data from objects
    for obj in objects:
        data = list(obj.__dict__.values())
        sheet.append(data)

    workbook.save(file)


def excelFileCreation(object, filename, sheetname):
    object = create_objects_from_json(object)
    filename = filename + ".xlsx"
    write_objects_to_excel(filename, sheetname, object)