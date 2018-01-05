import glob
import re
from bs4 import BeautifulSoup
import urllib

file_list = glob.glob('mariokartmp3/*.htm')
print(file_list)

links = []
for file in file_list:
    with open(file, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'html.parser')
        for link in soup.findAll('a', style="color: #21363f;"):
            link_text = str(link)
            link_start = link_text.find('http:')
            link_end = link_text.find('.mp3')
            divider = re.search(r"/\d-",link_text)
            file_search_string = divider.group()
            file_link_start = link_text.find(file_search_string)
            link_url = link_text[link_start:link_end+4]
            link_filename = link_text[file_link_start+1:link_end+4]
            link_filename = link_filename.replace('%20', ' ')
            link_filename = link_filename.replace('%28', '(')
            link_filename = link_filename.replace('%29', ')')
            link_filename = link_filename.replace('%21', '!')
            link_filename = link_filename.replace('%27', '\'')
            link_filename = 'marioaudio/' + link_filename
            print(f"getting {link_filename} from {link_url}")
            urllib.request.urlretrieve(link_url, link_filename)