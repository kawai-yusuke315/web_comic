import os
import urllib.request

MAX_PAGE = 1000

class WebComicDownloader:
    '''
    Webコミックをダウンロード
    '''

    def __init__(self,comic_base_url,download_dir):
        self.url = comic_base_url
        self.download_dir = download_dir
        
    def get_comic(self,comic_name,chapter,start_page = 1):
        '''
        想定しているサイトの構成
        URL:baseurl/'話数'/'ページNo'

        戻り値：最終読み込みページ（１ページも読み込めなかった場合はstart_page - 1)
        '''
        readed_page = start_page - 1

        chapter_url = self.url + comic_name + '/' + str(chapter) + "/"

        pages = range(start_page,MAX_PAGE + 1)

        for page in pages:
            
            url = chapter_url + str(page) + ".jpg"

            page_file = self.get_page(url)
            if page_file is None:
                break;
            
            self.save_page(page_file,comic_name,chapter,page)
            readed_page += 1

        return readed_page
    
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
    url = 'http://hogehoge/manga/'
    obj = WebComicDownloader(url, '/Users/momiji/tmp/')
    for i in range(1,5):
        obj.get_comic('comic_name',i)

