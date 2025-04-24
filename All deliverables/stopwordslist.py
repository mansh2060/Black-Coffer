"""
here i am creating a stopword list from the stopwords .txt file 

"""
def auditor_list():
    with open('StopWords_Auditor.txt','r')  as file:
        auditor=file.read()
    auditor_list=["".join(auditor)]
    auditor_list=auditor_list[0].replace("\n",",").strip(",")
    auditor_list=auditor_list.split(",")
    auditor_list=[word.lower() for word in auditor_list]
    return auditor_list


def currency_list():
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
    return currency_list

def datesandnumbers_list():
    with open('StopWords_DatesandNumbers.txt','r')  as file:
        datesandnumbers=file.read()
    datesandnumbers_list=["".join(datesandnumbers)]
    datesandnumbers_list=datesandnumbers_list[0].replace("\n",",").strip(",")
    datesandnumbers_list=datesandnumbers_list.split(",")
    datesandnumbers_list=[word.lower() for word in datesandnumbers_list]
    return datesandnumbers_list



def generic_list():
    with open('StopWords_Generic.txt','r')  as file:
        generic=file.read()
    generic_list=["".join(generic)]
    generic_list=generic_list[0].replace("\n",",").strip(",")
    generic_list=generic_list.split(",")
    generic_list=[word.lower() for word in generic_list]
    return generic_list

def genericlong_list():
    with open('StopWords_GenericLong.txt','r')  as file:
        genericlong=file.read()
    genericlong_list=["".join(genericlong)]
    genericlong_list=genericlong_list[0].replace("\n",",").strip(",")
    genericlong_list=genericlong_list.split(",")
    genericlong_list=[word.lower() for word in genericlong_list]
    return genericlong_list

def geographic_list():
    with open('StopWords_Geographic.txt','r')  as file:
        geographic=file.read()
    geographic_list=["".join(geographic)]
    geographic_list=geographic_list[0].replace("\n",",").strip(",")
    geographic_list=geographic_list.split(",")
    geographic_list=[word.lower() for word in geographic_list]
    return geographic_list


def positive_words_list():
    with open('positive-words.txt','r') as file:
        positive_words=file.read()
    positive_words_list=["".join(positive_words)]
    positive_words_list=positive_words_list[0].replace("\n",",").strip(",")
    positive_words_list=positive_words_list.split(",")
    positive_words_list=[word.lower() for word in positive_words_list]
    return positive_words_list



def negative_words_list():
    with open('negative-words.txt','r') as file:
        negative_words=file.read()
    negative_words_list=["".join(negative_words)]
    negative_words_list=negative_words_list[0].replace("\n",",").strip(",")
    negative_words_list=negative_words_list.split(",")
    negative_words_list=[word.lower() for word in negative_words_list]
    return negative_words_list

