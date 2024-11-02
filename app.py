import nextcord
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
# Initialize the client
intents = nextcord.Intents.default()
intents.message_content = True
client = nextcord.Client(intents=intents)

# Replace with your bot's token
TOKEN = os.getenv('TOKEN')

# Function to send reminder message every 30 minutes
async def water_reminder(user):
    while True:
        await user.send("💧 Time to drink some water! Stay hydrated! 💧")
        await asyncio.sleep(1800)  # Wait for 30 minutes (1800 seconds)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    for guild in client.guilds:
        for member in guild.members:
            if not member.bot:  # Only message non-bot members
                await water_reminder(member)  # Start the reminder loop for each member

@client.event
async def on_message(message):
    if message.content.lower() == "!startwaterreminder":
        await message.author.send("Starting your water reminder every 30 minutes!")
        await water_reminder(message.author)

client.run(TOKEN)
