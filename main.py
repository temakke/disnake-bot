import disnake
import os
from disnake.ext import commands

from dotenv import load_dotenv

load_dotenv()

intents=disnake.Intents.all()
intents.message_content = True 
                    
class NameClass(commands.Bot):

        async def on_ready(self) -> None:
                print(self.user)
                await self.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name="Status Name"))


token = os.getenv('TOKEN')
bot = NameClass(intents=intents, command_prefix='!')

# COGS

for filename in os.listdir('./c/discord'):
        file = filename[:-3]
        if filename.endswith('.py'):
                bot.load_extension(f'c.discord.{file}')

for filename in os.listdir('./c/imagens'):
        file = filename[:-3]
        if filename.endswith('.py'):
                bot.load_extension(f'c.imagens.{file}')

for filename in os.listdir('./c/admin'):
        file = filename[:-3]
        if filename.endswith('.py'):
                bot.load_extension(f'c.admin.{file}')


bot.run(token)
