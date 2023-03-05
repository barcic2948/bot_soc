import random
import hikari
import lightbulb

@lightbulb.option("player_with_the_ball", "Wybór jakie kości mają być rzucone przez bota dla zawodnika z piłką.")
@lightbulb.option("player_without_the_ball", "Wybór jakie kości mają być rzucone przez bota dla zawodnika bez piłki.")
@lightbulb.command("r", "Wykonaj odpowiedni pojedynek.")
@lightbulb.implements(lightbulb.SlashCommand)
async def battle(ctx: lightbulb.context.Context) -> None:

    player_1  = ctx.options.player_without_the_ball
    player_2 = ctx.options.player_with_the_ball

    embed = (
        hikari.Embed(
        title = "Wyniki:",
        colour=hikari.Colour(0x563275)
        )
        .set_footer(
            text=f"Wysłane przez {ctx.member.display_name}",
            icon=ctx.member.avatar_url,
        )
    )

    embed.add_field(name="Gracz bez piłki", value=f"Gwiazdki: **{player_1}** | Wynik: {throw(player_1, False)}", inline=False)
    embed.add_field(name="Gracz z piłką", value=f"Gwiazdki: **{player_2}** | Wynik: {throw(player_2, True)}", inline=False)

    await ctx.respond(embed)

def throw(value, ball):
    trick = ""
    roll = []
    if value == "1":
        roll = [random.randint(1,8) for _ in range(2)]
    elif value == "2":
        roll = [random.randint(1,4), random.randint(1,6), random.randint(1,8)]
    elif value == "3":
        roll = [random.randint(1,6) for _ in range(3)]
        roll.append(random.randint(1,3))
    elif value == "4":
        roll =[random.randint(1,3), random.randint(1,3), random.randint(1,4), random.randint(1,6), random.randint(1,8)]
    elif value == "5":
        roll = [random.randint(1,3), random.randint(1,4), random.randint(1,6), random.randint(1,8), random.randint(1,8)]
    else:
        resoult = " Zła ilość gwiazdek/złe polecenie -> nie liczba"
        return resoult

    if ball and roll.count(1) == 2:
        trick = "**trick!"

    resoult = " + ".join(f"{r}" for r in roll) + f" = **{sum(roll)}** | {trick}"
    return resoult

def load(bot: lightbulb.BotApp) -> None:
    bot.command(battle)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_command(bot.get_slash_command("r"))