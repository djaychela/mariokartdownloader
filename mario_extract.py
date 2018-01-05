import requests
from bs4 import BeautifulSoup, SoupStrainer

content = requests.get("https://downloads.khinsider.com/game-soundtracks/album/mario-kart-wii")
content = content.text


soup = BeautifulSoup(content, 'html.parser')

output_text=''
for link in soup.findAll('a',style=None):
    output_text+= str(link) + '\n'

with open('kartmp3.txt','w') as file:
    file.write(output_text)

