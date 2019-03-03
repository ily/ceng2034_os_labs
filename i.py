import os
#change my directory
path="/home"
os.chdir(path)
#create a new directory
os.system('mkdir -p $HOME/os_lab_0')
username=os.getlogin()
lpath='/home/'+username+'/os_lab_0/'
os.chdir(lpath)
#create a folder
open('1.txt','a').close()
open('2.txt','a').close()
open('0.py','a').close()

#last modified time

lst1 = os.stat('1.txt').st_mtime
lst2 = os.stat('2.txt').st_mtime
lst0 = os.stat('0.py').st_mtime

print("Last modified time for 1.txt:" , lst1)
print("Last modified time for 2.txt:" , lst2)
print("Last modified time for 0.py:" , lst0)

#find only txt file

for i in os.listdir(os.getcwd()):
	if i.endswith(".txt"):
		print(i)
