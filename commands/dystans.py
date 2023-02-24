import lightbulb

@lightbulb.command("dystans", "Rzut na dystans")
@lightbulb.implements(lightbulb.SlashCommand)
async def dystans(ctx: lightbulb.Context) -> None:


    
    await ctx.respond("Pong!")

def load(bot: lightbulb.BotApp):
    bot.command(dystans)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("dystans"))