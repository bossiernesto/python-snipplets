import openpyxl
from os.path import isfile, splitext
import csv

splitFileExtension = lambda aFile: (splitext(aFile))
getFileExtension = lambda aFile: (splitFileExtension(aFile)[1])
getFileName = lambda aFile: (splitFileExtension(aFile)[0])
changeFileExtension = lambda aFile, newExtension: ('.'.join([getFileName(aFile), newExtension]))


def convertXExcel2CSV(file):
    if not isfile(file):
        raise Exception('Not a file path')
    workbook = openpyxl.load_workbook(file, use_iterators=True)
    names = workbook.get_sheet_names()
    sheet = workbook.get_sheet_by_name(name=names[0])

    line = []

    with open(changeFileExtension(file, 'csv'), 'a+') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        for row in sheet.iter_rows():
            for k in row:
                line.append(k.internal_value)
            writer.writerow(line)
            line = []

