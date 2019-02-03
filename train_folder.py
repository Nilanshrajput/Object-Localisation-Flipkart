#script to clean data and transfer training images to separate folder
#tutorial source: https://www.youtube.com/watch?v=p0DNcTnreuY,
#https://stackabuse.com/creating-and-deleting-directories-with-python/
import xlrd #to install,command: "pip install xlrd"
import os
import shutil
file_location="C:/Users/itsab/Downloads/Compressed/training.xlsx"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
path="Compressed/new_folder_try"
#try:
#	os.mkdir(path)
#except OSError:
#	print("Successful")
#else:
#	print("Unsuccessful")
file_name_list=[]
for row in range(1,sheet.nrows): #check tab spacing according to urself
	file_name_list.append(sheet.cell_value(row,0))
#files=['text1.txt']
dest_folder="C:/Users/itsab/Downloads/Compressed/image_mirror5/images/train"
for f in file_name_list:
        shutil.move(f,dest_folder)
