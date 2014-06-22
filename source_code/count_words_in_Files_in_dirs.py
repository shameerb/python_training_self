import os
import glob

#move to the dir you want to check
os.chdir('.')
files_list=[]
#put all the files in the dir to the list
for files in glob.glob('*.*'):
    files_list.append(files)

#dict containing files and their word counts
files_wordCount={}
for files in files_list:
    with open(files) as f:
        content=''.join(f.readlines())
        #print files,(len(content.split(' ')))
        files_wordCount[files]=(len(content.split(' ')))
    f.close()

for f,k in files_wordCount.items():
    print f,k
