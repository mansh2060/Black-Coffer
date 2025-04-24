import urllib.request
from bs4 import BeautifulSoup
import re
from nltk.corpus import cmudict
import nltk
nltk.download('cmudict')

urllib.request.urlretrieve("https://www.flipkart.com/okaya-freedum-li-2-booking-ex-showroom-price-with-portable-charger-metallic-silver/p/itmd3ca00d21ef0f?pid=EBKGGYDPVVY5P5NT&lid=LSTEBKGGYDPVVY5P5NTISWF19&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_ee7653b4-0398-45c4-b5f2-9a53f766cc87_2_TJO4NT2UYUIT_MC.EBKGGYDPVVY5P5NT&ppt=None&ppn=None&ssid=h2oxs5tx6o0000001744382890494&otracker=clp_pmu_v2_Low%2BSpeed%2BScooters%2521_2_2.productCard.PMU_V2_OKAYA%2BFreedum%2BLI-2%2BBooking%2Bfor%2BEx-Showroom%2BPrice%2B%2528with%2BPortable%2BCharger%252C%2BMetallic%2BSilver%2529_electric-scooters-store_EBKGGYDPVVY5P5NT_neo%2Fmerchandising_1&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Low%2BSpeed%2BScooters%2521_LIST_productCard_cc_2_NA_view-all&cid=EBKGGYDPVVY5P5NT",
                           r"D:\black Coffer\demo.txt")


url="https://www.flipkart.com/okaya-freedum-li-2-booking-ex-showroom-price-with-portable-charger-metallic-silver/p/itmd3ca00d21ef0f?pid=EBKGGYDPVVY5P5NT&lid=LSTEBKGGYDPVVY5P5NTISWF19&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_ee7653b4-0398-45c4-b5f2-9a53f766cc87_2_TJO4NT2UYUIT_MC.EBKGGYDPVVY5P5NT&ppt=None&ppn=None&ssid=h2oxs5tx6o0000001744382890494&otracker=clp_pmu_v2_Low%2BSpeed%2BScooters%2521_2_2.productCard.PMU_V2_OKAYA%2BFreedum%2BLI-2%2BBooking%2Bfor%2BEx-Showroom%2BPrice%2B%2528with%2BPortable%2BCharger%252C%2BMetallic%2BSilver%2529_electric-scooters-store_EBKGGYDPVVY5P5NT_neo%2Fmerchandising_1&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Low%2BSpeed%2BScooters%2521_LIST_productCard_cc_2_NA_view-all&cid=EBKGGYDPVVY5P5NT"

def get_url_id(url):
    url=url.rstrip('/')
    return(url.split('/')[-1])

id=get_url_id(url)
with open('demo.txt','r') as file:
    content=file.read()
soup=BeautifulSoup(content,'html.parser')
main_content = soup.find('div', class_='main-content')  
text = main_content.get_text() if main_content else soup.get_text()
for tag in soup.find_all(class_=['footer']):
    tag.decompose()
text_list=text.split(" ")

cleaned_list=[word.strip('.,!?;"()[]{}') for word in text_list if word.isalpha()]
print(cleaned_list)
print(len(cleaned_list))
"""
with open('StopWords_Auditor.txt','r')  as file:
    auditor=file.read()
auditor_list=["".join(auditor)]
auditor_list=auditor_list[0].replace("\n",",").strip(",")
auditor_list=auditor_list.split(",")
auditor_list=[word.lower() for word in auditor_list]


currency_list = [
    "AFGHANI", "ARIARY", "BAHT", "BALBOA", "BIRR", "BOLIVAR", "BOLIVIANO",
    "CEDI", "COLON", "CÓRDOBA", "DALASI", "DENAR", "DINAR", "DIRHAM",
    "DOBRA", "DONG", "DRAM", "ESCUDO", "EURO", "FLORIN", "FORINT", "GOURDE",
    "GUARANI", "GULDEN", "HRYVNIA", "KINA", "KIP", "KONVERTIBILNA MARKA",
    "KORUNA", "KRONA", "KRONE", "KROON", "KUNA", "KWACHA", "KWANZA", "KYAT",
    "LARI", "LATS", "LEK", "LEMPIRA", "LEONE", "LEU", "LEV", "LILANGENI",
    "LIRA", "LITAS", "LOTI", "MANAT", "METICAL", "NAIRA", "NAKFA", "NEW LIRA",
    "NEW SHEQEL", "NGULTRUM", "NUEVO SOL", "OUGUIYA", "PATACA", "PESO",
    "POUND", "PULA", "QUETZAL", "RAND", "REAL", "RENMINBI", "RIAL", "RIEL",
    "RINGGIT", "RIYAL", "RUBLE", "RUFIYAA", "RUPEE", "RUPIAH", "SHILLING",
    "SOM", "SOMONI", "SPECIAL DRAWING RIGHTS", "TAKA", "TALA", "TENGE",
    "TUGRIK", "VATU", "WON", "YEN", "ZLOTY"
]
currency_list=[word.lower() for word in currency_list]

with open('StopWords_DatesandNumbers.txt','r')  as file:
    datesandnumbers=file.read()
datesandnumbers_list=["".join(datesandnumbers)]
datesandnumbers_list=datesandnumbers_list[0].replace("\n",",").strip(",")
datesandnumbers_list=datesandnumbers_list.split(",")
datesandnumbers_list=[word.lower() for word in datesandnumbers_list]



with open('StopWords_Generic.txt','r')  as file:
    generic=file.read()
generic_list=["".join(generic)]
generic_list=generic_list[0].replace("\n",",").strip(",")
generic_list=generic_list.split(",")
generic_list=[word.lower() for word in generic_list]



with open('StopWords_GenericLong.txt','r')  as file:
    genericlong=file.read()
genericlong_list=["".join(genericlong)]
genericlong_list=genericlong_list[0].replace("\n",",").strip(",")
genericlong_list=genericlong_list.split(",")
genericlong_list=[word.lower() for word in genericlong_list]



with open('StopWords_Geographic.txt','r')  as file:
    geographic=file.read()
geographic_list=["".join(geographic)]
geographic_list=geographic_list[0].replace("\n",",").strip(",")
geographic_list=geographic_list.split(",")
geographic_list=[word.lower() for word in geographic_list]



with open('positive-words.txt','r') as file:
    positive_words=file.read()
positive_words_list=["".join(positive_words)]
positive_words_list=positive_words_list[0].replace("\n",",").strip(",")
positive_words_list=positive_words_list.split(",")
positive_words_list=[word.lower() for word in positive_words_list]


with open('negative-words.txt','r') as file:
    negative_words=file.read()
negative_words_list=["".join(negative_words)]
negative_words_list=negative_words_list[0].replace("\n",",").strip(",")
negative_words_list=negative_words_list.split(",")
negative_words_list=[word.lower() for word in negative_words_list]

detail_list=[]
filename=f"{id}.txt"
detail_list.append(filename)
with open(filename,'w') as file:
    line=[]
    for word in cleaned_list:
        if word.lower() not in auditor_list and word.lower() not in geographic_list and word.lower() not in currency_list and word.lower() not in genericlong_list and word.lower() not in generic_list and word.lower() not in datesandnumbers_list:
            line.append(word)
            if (len(line)) >= 1:
                file.write(" ".join(line) + "\n")
                line=[]
file.close()

with open(filename,'r') as file:
    data=file.read()
urlid_list=[]
urlid_list.append(data)
urlid_string=urlid_list[0].replace("\n",",").strip(",")
urlid_list=urlid_string.split(",")
urlid_list=[word.lower() for word in urlid_list]



def calculate_positive_negative_polarity_subjectivity_score():
    positive_score=0
    negative_score=0
    for word in urlid_list:
        if word in positive_words_list:
            positive_score+=1
        if word in negative_words_list:
            negative_score+=-1
    detail_list.append(positive_score)
    detail_list.append(negative_score)
    polarity_score=(positive_score-(-1*negative_score))/((positive_score + (-1*negative_score)) + 0.000001)
    detail_list.append(polarity_score)
    subjectivity_score=(positive_score + (-1*negative_score))/((len(urlid_list))+0.000001)
    detail_list.append(subjectivity_score)
    return positive_score,negative_score,polarity_score,subjectivity_score,detail_list
calculate_positive_negative_polarity_subjectivity_score()


def calculate_average_len_sentences(text):
    cleaned_text=re.sub(r"[\n]","",text)
    text_split=re.split(r'[.!?]',cleaned_text)
    sentences=[sentence.strip() for sentence in text_split if sentence.strip()]
    total_words=sum(len(sent.split()) for sent in sentences)
    average_len_sentences=total_words/len(sentences)
    return average_len_sentences,detail_list
calculate_average_len_sentences(text)


def count_syallables():
    dictionary=cmudict.dict()
    for word in urlid_list:
        if word in dictionary:
           return max([len(list(y for y in x if y[-1].isdigit())) for x in dictionary[word]])
        else:
              return len(re.findall(r'[aeiouy]+', word.lower()))

def is_complex(word):
    return (count_syallables() > 2)

complex_words=[word for word in urlid_list if is_complex(word)]

    
        
            



"""