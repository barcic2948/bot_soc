import lightbulb
import hikari
import random

@lightbulb.command("bond6", "Bonusowa kość d6")
@lightbulb.implements(lightbulb.SlashCommand)
async def bond6(ctx: lightbulb.Context) -> None:
    
    embed = (
        hikari.Embed(
        title = "Bonusowe d6:",
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
    roll = [random.randint(1, 6) for _ in range(1)]
    resoult = "**" + " + ".join(f"{r}" for r in roll) + "**"
    return resoult

def load(bot: lightbulb.BotApp):
    bot.command(bond6)

def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("bond6"))