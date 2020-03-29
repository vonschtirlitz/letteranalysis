import requests
from bs4 import BeautifulSoup
import pandas as pd

linkpage=requests.get('https://www.masshist.org/digitaladams/archive/browse/letters_AA.php')
linksoup = BeautifulSoup(linkpage.content,'html.parser')
urls = []
for link in linksoup.find(class_='browseContent').findAll('a', href=True):
    #print("https://www.masshist.org"+ link['href'])
    urls.append("https://www.masshist.org"+ link['href'])
#print(newurls)
result = pd.DataFrame({'Dateline': [], 'Text': []})
#print(result)

#print("length=",len(urls))
#smallurls = urls[]
manualurls = ['https://www.masshist.org/digitaladams/archive/doc?id=L17790220ja']
for url in urls:
    print(url)
    page=requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    if soup.find(class_='dateline'):
        dateline = soup.find(class_='dateline').getText()
    else:
        dateline = "NA"
    print(dateline)
    paragraphs=soup.find(class_='letter').findAll('p')
    text = ""
    int = 0
    #print("processing paragraphs")
    #print(paragraphs[1])
    for para in paragraphs:
        #print(int)
        #print(para)
        if para.span:
            #print(tag)
            #if(tag.has_attr('class')):
            #    if tag['class'][0]=='note':
            #        tag.decompose()
            para.span.decompose()
        for tag in para.findAll('a'):
            tag.decompose()
        if para.div:
            para.div.decompose()

        temp = para.getText()
        text = text + temp + " "
        int = int + 1
    print(text)
    d = {'Dateline': dateline, 'Text': text}
    temp = pd.DataFrame(data = d, index = [0])
    #print(temp)
    result = result.append(temp, ignore_index=True)
    #print("adding text")
#print(result)
result.to_csv('bigletters2.csv',index=False, encoding='utf-8')
print("done")
