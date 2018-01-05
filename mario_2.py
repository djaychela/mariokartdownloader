import urllib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


data_list = []
with open('kartmp3.txt','r') as file:
    for line in file.readlines():
        data_list.append(line)
print(data_list)

for item in data_list:
    end_index=item.find('>')
    start_index=item.find('<')
    file_title_index = item.find('mario-kart-wii')
    file_title_end_index = item.find('mp3')
    file_title = "mariokartmp3/" + item[file_title_index+15:file_title_end_index] + 'htm'
    file_url = "http://downloads.khinsider.com/" + item[start_index+9:end_index-1]
    print(f"Now getting{file_title} from {file_url}...")
    urllib.request.urlretrieve(file_url, file_title)
