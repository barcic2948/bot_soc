import lightbulb

@lightbulb.command("siu", "Checks that the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand)
async def siu(ctx: lightbulb.Context) -> None:
    await ctx.respond("https://www.youtube.com/watch?v=PcN3RxdMOcg")

def load(bot: lightbulb.BotApp):
    bot.command(siu)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("siu"))