<p align="center">
        <a href="https://discord.gg/Em2ZwkVbfE">
            <img alt="Discord Server"
                 src="https://discord.com/api/guilds/776230580941619251/embed.png" />
        </a>
        <a href="https://opensource.org/licenses/MIT">
            <img alt="License"
                 src="https://img.shields.io/badge/License-MIT-yellow.svg" />
        </a>
        <a href="https://pypi.org/project/discord-ext-dashboard/">
                <img alt="Version"
                     src="https://img.shields.io/pypi/v/discord-ext-dashboard.svg?text=version" />
        </a>
        <a href="https://pypi.org/project/discord-ext-dashboard/">
                <img alt="Downloads"
                     src="https://img.shields.io/pypi/dm/discord-ext-dashboard.svg" />
        </a>
        <a href="https://pypi.org/project/discord-ext-dashboard/">
                <img alt="Supported Versions"
                     src="https://img.shields.io/pypi/pyversions/discord-ext-dashboard.svg" />
        </a>
</p>

<h1 align=center>discord-ext-dashboard</h1>
<p align=center>A webhook and request based discord.py extension for making a bot dashboard.</p>

## Installation
```py
pip install --upgrade discord-ext-dashboard

# If that doesn't work
python3 -m pip install --upgrade discord-ext-dashboard
```

## Usage
### Prerequisites
Before you get started, you will need a few things:
 - A webhook in secret channel (if anyone has access, they will be able to mess things up).
 - A properly hosted [**discord.py**](https://github.com/Rapptz/discord.py) bot
 
 And then you're ready to get started!

### Examples
#### Bot
```py
import discord
from discord.ext import commands
from discord.ext.dashboard import Dashboard

bot = commands.Bot(command_prefix="!")
bot_dashboard = Dashboard(bot,
	"secret_key", 
	"https://your-bot-website.com/dashboard"
)

@bot.event
async def on_ready():
	print(f"Bot is online as {bot.user}")

@bot.event
async def on_message(message):
	await bot_dashboard.process_request(message)

@bot_dashboard.route
async def guild_count(data):
	return len(bot.guilds)

@bot_dashboard.route
async def member_count(data):
	return await bot.fetch_guild(data["guild_id"]).member_count

bot.run("your-token-here")
```


#### Webserver
```py
from quart import Quart, request
from discord.ext.dashboard import Server

app = Quart(__name__)
app_dashboard = Server(
	app,
	"secret_key", 
	webhook_url="https://your-private-discord-webhook.com"
)

@app.route("/")
async def index():
	guild_count = await app_dashboard.request("guild_count")
	member_count = await app_dashboard.request("member_count", guild_id=776230580941619251)

	return f"Guild count: {guild_count}, Server member count: {member_count}"

@app.route("/dashboard", methods=["POST"])
async def dashboard():
	# Don't worry about authorization, the bot will handle it
	await app_dashboard.process_request(request)
        
        
if __name__ == "__main__":
        app.run()
```


Please note that cogs are not currently supported.
<br>
You will also need to use Quart as your webserver. Switching from another library isn't hard, so ask me and I'll gladly help you out.
<br><br>
For support join [**CRYO OFFICIΛL**](https://discord.gg/Em2ZwkVbfE)
