#script to clean data and transfer training images to separate folder
#tutorial source: https://www.youtube.com/watch?v=p0DNcTnreuY
import xlrd #to install,command: "pip install xlrd"
file_location="C:/Users/itsab/Downloads/Compressed/training.xlsx"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
file_name_list=[]
for row in range(1,sheet.nrows): #check tab spacing according to urself
	file_name_list.append(sheet.cell_value(row,0))
