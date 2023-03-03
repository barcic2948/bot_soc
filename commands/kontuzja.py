import random

import hikari
import lightbulb

@lightbulb.command("kontuzja", "Rzut na kontuzje")
@lightbulb.implements(lightbulb.SlashCommand)
async def kontuzja(ctx: lightbulb.Context) -> None:
    #2d3
    embed = (
        hikari.Embed(
        title = "Rzut na kontuzje:",
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
    roll = [random.randint(1, 3) for _ in range(2)]
    resoult = "**" + " + ".join(f"{r}" for r in roll) + "**"
    return resoult

def load(bot: lightbulb.BotApp):
    bot.command(kontuzja)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("kontuzja"))