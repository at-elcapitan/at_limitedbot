# AT PROJECT Limited 2022 - 2024; AT_nEXT-v3.6
import discord

def default():
    embed = discord.Embed(title="ENTIRE command list", description="List of ALL system commands", color=0xa31eff)
    embed.add_field(name="Global COMMANDS", value="`sc.inspect`", inline=False)
    embed.add_field(name="Music", value="`/youtube`, `/soundcloud`, `/spotify`, `/resend_control`, `/seek`, `/clear`")
    embed.add_field(name="User list [Music]", value="`/list add`, `/list display`, `/list remove`, `/list play`")
    return embed


# Error embed
def error_embed(error_num: str, name: str, text: str):
    embed = discord.Embed(title=f"System Alert: Code {error_num}", color=0xFF0000)
    embed.add_field(name=name, value=text, inline=False)
  
    return embed


def event_embed(title = None, text = None, name = ""):
    embed = discord.Embed(title=title, color=0x915AF2)
    embed.add_field(name=name, value=text, inline=False)
    return embed