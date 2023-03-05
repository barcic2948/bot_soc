import random
import hikari
import lightbulb

@lightbulb.command("strzal", "Rzut na strzal")
@lightbulb.implements(lightbulb.SlashCommand)
async def strzal(ctx: lightbulb.Context) -> None:
    #1d12
    embed = (
        hikari.Embed(
        title = "Rzut na strzał:",
        colour=hikari.Colour(0x563275)
        )
        .set_footer(
            text=f"Wysłane przez {ctx.member.display_name}",
            icon=ctx.member.avatar_url,
        )
    )
    embed.add_field(name="Wynik", value=fun(), inline=False)
    
    await ctx.respond(embed)

def fun():
    roll = [random.randint(1, 12)]
    resoult = "**" + " + ".join(f"{r}" for r in roll) + "**"
    return resoult

def load(bot: lightbulb.BotApp):
    bot.command(strzal)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("strzal"))