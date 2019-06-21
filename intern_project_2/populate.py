import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intern_project_2.settings')
import django

django.setup()

# Writing populating script
import xlrd
from searchapp.models import Transport

loc = '/home/shwetanshu/Desktop/data.xlsx'
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(5)
for i in range(1, sheet.nrows):
    vehiclet = sheet.cell_value(i, 1)
    carriert = sheet.cell_value(i, 2)
    location_not = sheet.cell_value(i, 3)
    mcmut = sheet.cell_value(i, 4)
    locationt = sheet.cell_value(i, 5)
    customer_codet = sheet.cell_value(i, 6)
    zonet = sheet.cell_value(i, 7)
    quantityt = sheet.cell_value(i, 8)
    rtkmt = sheet.cell_value(i, 9)
    klkmt = sheet.cell_value(i, 10)
    amountt = sheet.cell_value(i, 11)
    loadt = sheet.cell_value(i, 12)
    capacityt = sheet.cell_value(i, 13)
    ratet = sheet.cell_value(i, 14)
    costt = sheet.cell_value(i, 15)

    trans= Transport.objects.get_or_create(vehicle=vehiclet, carrier=carriert, location_no=location_not, mcmu=mcmut, location=locationt,
                                           customer_code=customer_codet, zone=zonet, quantity=quantityt, rtkm=rtkmt, klkm=klkmt, amount=amountt,
                                           load=loadt, capacity=capacityt, rate=ratet, cost=costt)[0]
