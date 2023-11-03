import sys 
import random
import shutil
import os


from_dir = "C:/Users/Lenovo/Downloads"
to_dir= "Document_Files"

list_of_files= os.listdir(from_dir)
print(list_of_files)


#forin loop for moving from one file to other 

for file_name in list_of_files:
    name,extension= os.path.splitText(file_name)
    print(name)
    print(extension)


if extension == '':
    continue
if extension in [".txt",".doc",".docx",".pdf"]:


path1 = from_dir+'/'+file_name
path2 = from_dir+ '/' + "Document_Files"
path3 = from_dir+ '/' +"Document_Files"+ file_name



#checking if folder path already exists 
#or else make a new folder
if os.path.exists(path2):
    print("moving" +file_name "....")

#move from path1 => path 3
shutil.move(path1,path3)

else:
  os.makedirs(path2)
  print("moving" +file_name "....")
  shutil.move(path1,path3)