import lightbulb

@lightbulb.command("strzal", "Rzut na strzal")
@lightbulb.implements(lightbulb.SlashCommand)
async def strzal(ctx: lightbulb.Context) -> None:


    
    await ctx.respond("Pong!")

def load(bot: lightbulb.BotApp):
    bot.command(strzal)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("strzal"))