import lightbulb
import hikari
import random

@lightbulb.option("goalkeeper", "Ilośc rzuconych kości w zależności od siły bramkarza.")
@lightbulb.command("obr", "Rzut na obronę bramkarza")
@lightbulb.implements(lightbulb.SlashCommand)
async def obrona(ctx: lightbulb.Context) -> None:

    number_of_stars  = ctx.options.goalkeeper

    embed = (
        hikari.Embed(
        title = "Rzut na obronę bramkarza:",
        colour=hikari.Colour(0x563275)
        )
        .set_footer(
            text=f"Wysłane przez {ctx.member.display_name}",
            icon=ctx.member.avatar_url,
        )
    )
    
    if number_of_stars.isdigit() and int(number_of_stars) < 5:
        embed.add_field(name="Wynik dla " + f"**{number_of_stars}** gwiazdek", value=fun(int(number_of_stars)), inline=False)
    else:
        embed.add_field(name="Wynik", value="Niepoprawna wartość podana jako argument funkcji: " + f"**{number_of_stars}**", inline=False)

    await ctx.respond(embed)

def fun(number_of_stars):
    roll = [random.randint(1,6) for _ in range(number_of_stars)]
    resoult = "**" + " + ".join(f"{r}" for r in roll) + "**"
    return resoult

def load(bot: lightbulb.BotApp):
    bot.command(obrona)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("obrona"))
    