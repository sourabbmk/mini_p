from bs4 import BeautifulSoup
import requests
import csv

source=requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

csv_file = open('site_scrape.csv','w')

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video link'])

for article in soup.find_all('article'):

    try:
        headline=article.a.text
        
    except:
        headline=None
    
    print(headline)

    try:
        summary=article.find('div',class_='entry-content').p.text

    except:
        summary=None
    
    print(summary)

    try:
        vid_src=article.find('iframe',class_='youtube-player')['src']

        vid_id=vid_src.split('/')[4]
        vid_id=vid_id.split('?')[0]

        yt_link=f'https://youtube.com/watch?v={vid_id}'

    except:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()