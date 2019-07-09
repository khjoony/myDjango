"""
assembly_member_profile
"""
import re
import requests
from bs4 import BeautifulSoup as bs
#listArea > table > tbody > tr:nth-child(2) > td:nth-child(2) > 눔

## start를 기준으로 둘로 나눔
URL1 = 'https://www.google.com/search?q=사드&newwindow=1'\
    '&rlz=1C1CHBD_koKR845KR845&ei=g7YkXbGJN_SNr7wP5bio4AI&start='
URL2 = '&sa=N&ved=0ahUKEwjx1tiPl6jjAhX0xosBHWUcCiw4FBDy0wMIcw'\
    '&biw=1910&bih=956'
def join_url(URL1, URL2):
    URLS = []
    for num in range(0,5):
        URLS.append(URL1 + str(num*10) + URL2)
        print(URLS[num])
    return URLS

"""
def get_text(URLS):
    r = re.compile(r"(http://[^ ]+)")
    for url in URLS:
        print(url)
        response = requests.get(url)
        soup = bs(response, 'html.parser').text
        results_response = soup.select('a[href*=url]')

        response_text = []
        for item in results_response:
            response_text.append(item.text)
            print(response_text)
"""
def main():
    URLS = join_url(URL1, URL2)
    ## get_text(URLS)


if __name__ =='__main__':
    main()