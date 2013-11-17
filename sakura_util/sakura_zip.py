import os
import zipfile

def list_to_zip(file_list,zip_path,files_dir=None):
    '''
    target_listで指定されたファイルをzipにまとめる
    '''
    #zip_file = zipfile.zipFile(zip_path,'w')

    with zipfile.ZipFile(zip_path,'w') as zip_file:
        for f in file_list:
            file_path = f
            if files_dir is not None:
                file_path = files_dir + f
            zip_file.write(file_path,'/' + f)

  
    zip_file.close()

