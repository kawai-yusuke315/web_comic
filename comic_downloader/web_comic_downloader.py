import time
import os
import shutil
import urllib.request

MAX_PAGE = 100
DEFAULT_PATH = 0.1

class WebComicDownloader:
    '''
    Webコミックをダウンロードするスクリプト
    '''

    def __init__(self,comic_base_url,download_dir):
        path = DEFAULT_PATH
        self.url = comic_base_url
        self.download_dir = download_dir
        
    def get_comic(self,comic_name,chapter):
        '''
        想定しているサイトの構成
        URL:baseurl/'話数'/'ページNo'
        '''
        page_count = 0

        chapter_url = self.url + comic_name + '/' + str(chapter) + "/"

        pages = range(1,MAX_PAGE + 1)

        for page in pages:
            
            url = chapter_url + str(page) + ".jpg"

            page_file = self.get_page(url)
            if page_file is None:
                break;
            
            self.save_page(page_file,comic_name,chapter,page)
            page_count += 1

        return page_count
    
    def get_page(self,url):
        result = None
        try:
            print(url)
            res  = urllib.request.urlopen(url)
            result = res.read()
        except urllib.error.HTTPError:
            print('http_error')

        except urllib.error.URLError:
            print('url_error')

        return result

    def save_page(self,image,comic_name,chapter,page):

        dl_dir = self.download_dir + comic_name + '/'
        if os.path.exists(dl_dir) == False:
            os.makedirs(dl_dir) 

        dl_file = dl_dir +  str(chapter).zfill(4) + '-' + str(page).zfill(3) + '.jpg'
        print (dl_file)
        mkfile = open(dl_file,'wb')
        mkfile.write(image)
        mkfile.close()

if __name__ == '__main__':
    url = 'http://hogehoge.hogehoge/'
    obj = WebComicDownloader(url, '/Users/momiji/tmp/')
    for i in range(2,6):
        obj.get_comic('tree',i)

