"""
Here i am extracting words from all 147 different urls using BeautifulSoup and the words are stored in a filtered_url_id.txt file 
after ectraction and these words are stored after checking the stopwords
"""

from bs4 import BeautifulSoup

import pandas as pd
import os
import requests


from stopwordslist import auditor_list, currency_list, datesandnumbers_list, generic_list, genericlong_list, geographic_list, positive_words_list, negative_words_list


df = pd.read_excel('input.xlsx')


num_urls = df['URL_ID'].count()


for i in range(num_urls):
    url_id = df.loc[i, 'URL_ID']
    url = df.loc[i, 'URL'] 

    
    filename = f"{url_id}.txt"

    
    if not os.path.exists(filename):
        try:
            response = requests.get(url)
            response.raise_for_status()  
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
        
        except Exception as e:
            print(f"Error downloading content from URL {url}: {e}")
            continue

  
    try:
        
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
    
    except UnicodeDecodeError as e:
        print(f"Error reading file {filename}: {e}")
        continue


    soup = BeautifulSoup(contents, 'html.parser')

 
    for tag in soup.find_all(class_=['header', 'footer']):
        tag.decompose()

    
    main_content = soup.find('div', class_='main-content')
    text = main_content.get_text() if main_content else soup.get_text()
    text_list = text.split(" ")
    cleaned_list = [word.strip('.,!?;"()[]{}') for word in text_list if word.isalpha()]

 
    filtered_words = [
        word for word in cleaned_list
        if word.lower() not in auditor_list() and
           word.lower() not in geographic_list() and
           word.lower() not in currency_list() and
           word.lower() not in genericlong_list() and
           word.lower() not in generic_list() and
           word.lower() not in datesandnumbers_list()
    ]

   
    output_filename = f"filtered_{url_id}.txt"
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            for word in filtered_words:
                file.write(word + "\n")  
    
    
    except Exception as e:
        print(f"Error writing to file {output_filename}: {e}")
