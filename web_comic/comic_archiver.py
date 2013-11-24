import os
from sakura_util import sakura_zip
class ComicArchiver:

    def __init__(self,file_dir):
        self.file_dir = file_dir
    def archive(self,comic_name,start_chapter = 1,chapter_count = 1,delete_flg = False):
               
        self.start = start_chapter
        self.count = chapter_count
        comic_dir = self.file_dir + comic_name + '/'   

        file_list = None
        for s,ds,fs in os.walk(comic_dir) :
            file_list = fs
            break

        target_files = self.get_target_files(file_list)

        zip_path = self.file_dir + comic_name + '_' + str(start_chapter) + '-' + str(start_chapter + chapter_count - 1) + '.zip'
        sakura_zip.list_to_zip(target_files,zip_path,comic_dir)

    def get_target_files(self,file_list):
        file_list.sort()
        first = self.get_first_file(file_list)
        if first is None:
            return
        fl = file_list[first:]

        result = []
        for file_name in fl:
            if self.is_target_file(file_name):
                result.append(file_name)
            else:
              break

        return result

    def get_first_file(self,fs):
        result = None
        for i in range(self.start,self.start + self.count + 1):
            try:
                tmp_name = str(i).zfill(4) + '-001.jpg'
                result = fs.index(tmp_name)
                break

            except ValueError:
                pass

        return result

    def is_target_file(self,file_name):
        file_chapter = int(file_name[0:4])
        if file_chapter >= self.start and file_chapter <= self.start + self.count -1:
            return True
        else:
            return False


if __name__ == '__main__':
    hoge = ComicArchiver('/Users/momiji/tmp/')
    hoge.archive('tree',729)
