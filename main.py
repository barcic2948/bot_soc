import lightbulb

with open("./secrets/token.txt") as f:
    token = f.read().strip()

bot = lightbulb.BotApp(token)

bot.load_extensions_from("./commands")

bot.run()