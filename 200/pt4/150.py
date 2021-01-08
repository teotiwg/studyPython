import os, glob

folder = 'pt4'
file_list = os.listdir(folder)
print(file_list)

files = '*,txt'
file_list = glob.glob(files)
print(file_list)