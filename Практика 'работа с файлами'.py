import zipfile


zip_file_name = 'voina_i_mir.zip'

zfile = zipfile.ZipFile(zip_file_name, 'r')
for filename in zfile.namelist():
    zfile.extract(filename)