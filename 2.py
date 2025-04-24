import urllib.request
from bs4 import BeautifulSoup

url="https://insights.blackcoffer.com/enhancing-front-end-features-and-functionality-for-improved-user-experience-and-dashboard-accuracy-in-partner-hospital-application/"

filename='151.txt'

urllib.request.urlretrieve(url,filename)

try:
    with open('151.txt','r') as file:
        content=file.read()
    soup=BeautifulSoup(content,'html.parser')

    for tag in soup.find_all(class_=(['header','footer'])):
        tag.decompose()

    text=soup.get_text()
    text_list=text.split()
    clean_list=[word.strip('.,!?;"()[]{}') for word in text_list if word.isalpha()]
    print(clean_list)
except  UnicodeDecodeError as e:
    print(f"Error reading a {filename} : {e}")


