import disnake
from disnake.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command(description='| Discord | Comando para checar a lantência do bot!')
    async def ping(inter):
        await inter.response.send_message(f':ping_pong: **Pong!**\n ``{format(round(inter.bot.latency * 1000))}``ms')



def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))