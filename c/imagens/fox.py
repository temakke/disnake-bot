import disnake
from aiohttp import request
from disnake.ext import commands

class FoxCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    

    @commands.slash_command(description='| Imagens | Gera uma imagem aléatoria de uma raposa!')
    async def fox(inter):
        r = ('https://randomfox.ca/floof/') 

        async with request("GET", r, headers={}) as response:
            if response.status == 200:
                data = await response.json()
            else:
                await inter.response.send_message('Ocorreu algum erro. Espere alguns minutos para executar esse comando novamente...', ephemeral=True)
                pass
        
        url= data["image"]

        fEmbed = disnake.Embed(
            description=f'** :fox: | [rrrrrrr...]({url})**',
            color= disnake.Colour.random()
        )

        fEmbed.set_footer(text="credits: https://randomfox.ca", icon_url=None)
        fEmbed.set_image(url)

        await inter.response.send_message(embed=fEmbed)



def setup(bot: commands.Bot):
    bot.add_cog(FoxCommand(bot))
