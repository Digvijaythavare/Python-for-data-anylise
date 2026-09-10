from openpyxl import workbook

stu = [
    ["Digvijay", 20,"Python"],
    ["Vijay",21,"Java"]
]

wb = workbook()
sheet = wb.active

for item in stu:
    sheet.append(item)

wb.save("student.xlsx")    