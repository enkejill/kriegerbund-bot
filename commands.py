import discord
import storage
import asyncio
import time
from string_set import *
from dev import *
import dice
import user_settings


def get_command(message, signs):
    args = message.content.split(' ')
    print(args)
    if isinstance(signs, list):
        for sign in signs:
            if message.content.startswith(sign):
                return (args[0])[len(sign):]
    elif isinstance(signs, str):
        if message.content.startswith(signs):
            return (args[0])[len(signs):]
    return None


def get_args(message):
    return message.content.split(' ')[1:]


def handle_commands(message, command, args):
    #if command == 'test':
    #    return cmd_test(message, args)
    if command == 'ping':
        return ping(message)
    if command == 'zitat' or command == 'quote':
        return cmd_quotes(message, args)
    if command == 'roll' or command == 'dice':
        return dice.cmd_roll(message, args)
    if command == 'dev':
        return cmd_dev(message, args)
    if command == 'help': 
        asyncio.ensure_future(cmd_help(message))
        return ''
    if command == 'load' or command == 'loading':
        asyncio.ensure_future(cmd_load(message, 0))
    if command == 'github':
        return 'https://github.com/enkejill/kriegerbund-bot'
    if command == 'user':
        return cmd_user(message, args)
    if command == 'hallo':
        if check_permissions(message):
            return '''\
<:kriegerbund:352935520579616768> **Hallo Kriegerbund!** <:kriegerbund:352935520579616768>

Ich bin der neue, hauseigene Kriegerbund-Bot.
Wenn ihr wissen möchtet, was ich so kann, dann schreibt doch einfach `!help` in einen geeigneten Chat (aber vorsicht, andere Bots streiten sich vielleicht mit mir darum wer antworten darf).

Bisher kann ich leider noch sehr wenig. Wenn ihr Ideen/Vorschläge habt, was für Funktionen ich so bekommen soll, dann benutzt doch bitte das `!dev` Kommando.
Wenn ihr einen Bug entdeckt, könnt ihr diesen mit `!dev` ebenfalls reporten.

Was ihr in der Zwischenzeit schon ausprobieren könnt:
`!zitat`
und
`!dice`

Für die Horde! <:horde:334814213828771850>'''
        else:
            return 'Hi, {0.author.mention}!'


async def cmd_help(message):
    help_msg = '''\
```Kriegerbund Bot Help```
```Commands:

![command] help: Returns help for the specific command

!ping: Pong!

!quote and !zitat: Quote function, default: random quote

!dice and !roll: Rolls dice.

!dev: Development tools for reporting bugs and requesting
features```'''
    if message.author.dm_channel is None:
        await message.author.create_dm()
    await message.author.dm_channel.send(help_msg)


async def cmd_load(message, count, max_count=20):
    msg = '`Loading .'
    if count == 0:
        new_msg = (await message.channel.send(msg + '`'))
        asyncio.ensure_future(cmd_load(new_msg, 1))
        return
    if count >= max_count:
        time.sleep(2)
        await message.edit(content='lul, just kidding, nothing\'s gonna happen')
        return
    time.sleep(0.5)
    for _ in range(count):
        msg += '.'
    msg += '`'
    await message.edit(content=msg)
    asyncio.ensure_future(cmd_load(message, count+1))


def cmd_test(message, args):
    return ''
