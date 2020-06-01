# import xlrd
# import csv
#
# def csv_from_excel(excel_path, sheet_name, csv_path):
#     wb = xlrd.open_workbook(excel_path)
#     sh = wb.sheet_by_name(sheet_name or "Sheet1")
#     your_csv_file = open(csv_path, 'w')
#     wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
#
#     for rownum in range(sh.nrows)[1:]:
#         wr.writerow(sh.row_values(rownum))
#
#     your_csv_file.close()
#
# # runs the csv_from_excel function:
# # excel_path = "../../datas/Danh sách cấp tỉnh kèm theo quận huyện, phường xã ___23_04_2020.xls"
# # sheet_name = "Sheet1"
# # csv_path = "../../data/dvhc.csv"
# # csv_from_excel(excel_path, sheet_name, csv_path)