"""
test
"""
import re
import requests
from bs4 import BeautifulSoup as bs

class Test():
    """
    Test
    """
    test = "teset"
    #print(test)
URL = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?rowPerPage=300'
HTML = requests.get(URL).text
SOUP = bs(HTML, 'html.parser')
# find Korean Name
class KrName():
    """
    KrName
    """
    NAMES = []
    MEMBER_IDS = []
    for member_tag in SOUP.select('.memberna_list dl dt a'):
        link = member_tag['href']
        name = member_tag.text
        matched = re.search(r'\d+', link)
        if matched:
            member_id = matched.group(0)
        else:
            member_id = None
        NAMES.append(name)
        MEMBER_IDS.append(member_id)
        print(NAMES, MEMBER_IDS)
class ChiName():
    """
    ChiName
    .memberna_list  dl dt span
    """
    CHI_NAMES = []
    for member_tag in SOUP.select('.memberna_list dl dt span'):
        create_chi_name = member_tag.text
        matched_chi_name = re.search(r'\w+', create_chi_name)
        if matched_chi_name:
            chi_name = matched_chi_name.group(0)
        else:
            chi_name = None
        CHI_NAMES.append(chi_name)
        print(CHI_NAMES)
class EnName():
    """
    EnName
    """
    EN_NAMES = []
    for member_tag in SOUP.select('.memberna_list dl dt'):
        total_name = member_tag.text
        matched_en_name = re.search(r'[A-Z]\w+ [A-Z]\w+', total_name)
        if matched_en_name:
            en_name = matched_en_name.group(0)
        else:
            en_name = None
        EN_NAMES.append(en_name)
        print(EN_NAMES)
