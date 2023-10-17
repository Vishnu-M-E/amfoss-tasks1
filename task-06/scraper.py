import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_data():
    url = 'https://www.espncricinfo.com/live-cricket-score'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    all=soup.find("div",class_="ds-text-compact-xxs").text
    team1 = soup.find("p",class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate").text    
    team2 = soup.find("p",class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate").text
    score1 = soup.find('strong').text
    score2 = soup.find('strong').text
    over1=soup.find('span',class_="ds-text-compact-xs ds-mr-0.5").text
    over2=soup.find('span',class_="ds-text-compact-xs ds-mr-0.5").text
    if over1 not in all or over2 not in all:
        over1='-'
        over2='-'

    result=soup.find("p",class_="class=ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
   
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    with open('scores.csv', 'a') as file:
        file.write(f'{team1},{over1},{score1},{team2},{over2},{score2},{result},{timestamp}\n')


