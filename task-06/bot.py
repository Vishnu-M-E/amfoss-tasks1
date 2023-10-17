import discord
import scraper
import os
from dotenv import load_dotenv
from scraper import scrape_data

load_dotenv()


intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/livescore'):
        scraper.scrape_data()
        
        with open('scores.csv', 'r') as file:
            rows = file.readlines()
            if len(rows) == 0:
                await message.channel.send('No live scores available! Try again later.')
            else:
                last_row = rows[-1]        
                team1, over1, score1, team2, over2, score2, result, timestamp = last_row.split(',')
                response = f'Team 1: {team1} {over1} {score1}\nTeam 2: {team2} {over2} {score2}\n{result} {timestamp}'

                await message.channel.send(response)

    elif message.content.startswith('/generate'):
        with open('scores.csv', 'r') as file:
            csv_contents = file.read()

            if csv_contents:
                csv_file = discord.File('scores.csv')
                await message.channel.send(file=csv_file)
            else:
                await message.channel.send('Error generating the CSV file.')

        
    elif message.content.startswith('/help'):
        response = 'Commands:\n/livescore - Get the live score of the match.\n/generate - Get the CSV file that contains the list of all the live scores that have been fetched.\n/help - Get a list of the commands along with their description.'
        await message.channel.send(response)

TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
