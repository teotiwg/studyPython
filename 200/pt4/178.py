from zipfile import *

def extractZip(zipname):
    with ZipFile(zipname, 'r') as ziph:
        ziph.extractall()
        print('%s 추출 성공' %zipname)

extractZip('files.zip')