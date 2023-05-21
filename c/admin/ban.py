import disnake
from disnake.ui import Button, View
from disnake.ext import commands

class AdminCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command(description='| Moderação | O nome é bem auto explicativo.')
    @commands.has_permissions(ban_members=True)
    async def ban(inter, user: disnake.Member, reason = "Não especificado."):

        if user == inter.author or user.id == inter.bot.application_id:
            await inter.response.send_message('Não foi possivel banir esse user!', ephemeral=True)


        b = Button(label="Confirm!", style=disnake.ButtonStyle.danger)
        v = View()
        v.add_item(b)

        bEmbed1 = disnake.Embed(
            description=f':bell: **| Notificação**\n{user.mention} foi punido com sucesso! Por {inter.author.mention}. Motivo: {reason} \n Não será enviada nenhuma mensagem ao usuário punido.'
        )
        bEmbed2 = disnake.Embed(
            description=f':hammer_pick: **| Atenção**\nVocê está prestes a banir {user.mention} pelo motivo `{reason}` deseja prosseguir?'
        )

        async def button_callback(interaction):
            await user.ban(reason=reason)
            v.remove_item(b)
            await interaction.response.send_message(embed=bEmbed1, ephemeral=True)
            
        
        b.callback = button_callback
        
        await inter.response.send_message(embed=bEmbed2, view=v, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(AdminCommands(bot))
