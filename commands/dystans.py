import random

import hikari
import lightbulb

@lightbulb.command("dystans", "Rzut na dystans")
@lightbulb.implements(lightbulb.SlashCommand)
async def dystans(ctx: lightbulb.Context) -> None:
    #3d2
    embed = (
        hikari.Embed(
        title = "Rzut na dystans:",
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
    roll = [random.randint(1, 2) for _ in range(3)]
    resoult = "**" + " + ".join(f"{r}" for r in roll) + "**"
    return resoult

def load(bot: lightbulb.BotApp):
    bot.command(dystans)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("dystans"))