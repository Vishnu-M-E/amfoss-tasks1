import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_data():
    # Send an HTTP request to the ESPN website
    url = 'https://www.espncricinfo.com/live-cricket-score'
    response = requests.get(url)
    
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the team names, scores, and summary of the match
    all=soup.find("div",class_="ds-text-compact-xxs").text
    team1 = soup.find("p",class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate").text    
    team2 = soup.find_all("p",class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")[1].text
    score1 = soup.find('strong').text
    score2 = soup.find_all('strong')[1].text
    over1=soup.find('span',class_="ds-text-compact-xs ds-mr-0.5").text
    over2=soup.find_all('span',class_="ds-text-compact-xs ds-mr-0.5")[1].text
    if over1 not in all or over2 not in all:
        over1='-'
        over2='-'

    result=soup.find("p",class_="class=ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
    


    
#    if team1_elem and score1_elem and team2_elem and score2_elem and summary_elem:
#        team1 = team1_elem.text.strip()
#        score1 = score1_elem.text.strip()
#        team2 = team2_elem[1].text.strip()
#        score2 = score2_elem[1].text.strip()
#        summary = summary_elem.text.strip()
        
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    # Append the scraped data and the timestamp to a CSV file
    with open('scores.csv', 'a') as file:
        file.write(f'{team1},{over1},{score1},{team2},{over2},{score2},{result} {timestamp}\n')


