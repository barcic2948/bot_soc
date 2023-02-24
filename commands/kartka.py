import lightbulb
import hikari
import random

@lightbulb.command("kartka", "Czy gracz otrzymuje kartkę")
@lightbulb.implements(lightbulb.SlashCommand)
async def kartka(ctx: lightbulb.Context) -> None:

    
    await ctx.respond("Pong!")

def load(bot: lightbulb.BotApp):
    bot.command(kartka)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("kartka"))