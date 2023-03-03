import random

import hikari
import lightbulb

@lightbulb.command("zagranie", "Rzut na zagranie")
@lightbulb.implements(lightbulb.SlashCommand)
async def zagranie(ctx: lightbulb.Context) -> None:
    #1d4
    embed = (
        hikari.Embed(
        title = "Rzut na zagranie:",
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
    roll = [random.randint(1, 4)]
    resoult = "**" + " + ".join(f"{r}" for r in roll) + "**"
    return resoult

def load(bot: lightbulb.BotApp):
    bot.command(zagranie)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("zagranie"))