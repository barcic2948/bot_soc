import random

import hikari
import lightbulb

@lightbulb.command("kartka", "Czy gracz otrzymuje kartkę")
@lightbulb.implements(lightbulb.SlashCommand)
async def kartka(ctx: lightbulb.Context) -> None:
    #2d2
    embed = (
        hikari.Embed(
        title = "Czy gracz otrzymał kartkę:",
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
    roll = [random.randint(1, 2) for _ in range(2)]
    resoult = "**" + " + ".join(f"{r}" for r in roll) + "**"
    return resoult

def load(bot: lightbulb.BotApp):
    bot.command(kartka)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("kartka"))