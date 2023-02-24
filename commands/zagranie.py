import lightbulb

@lightbulb.command("zagranie", "Rzut na zagranie")
@lightbulb.implements(lightbulb.SlashCommand)
async def zagranie(ctx: lightbulb.Context) -> None:


    
    await ctx.respond("Pong!")

def load(bot: lightbulb.BotApp):
    bot.command(zagranie)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("zagranie"))