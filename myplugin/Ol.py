import asyncio
from telethon import events

hunt_active = False
ultimate = True
@hell_cmd(pattern="explore$")
async def hunt_start(event):
    global hunt_active
    global ultimate 
    if hunt_active:
        await event.edit("explore is already active.")
        return
    hunt_active = True
    ultimate = True
    await event.edit("explore is active")
    await event.client.send_message(5364964725, "/explore")

@bot.on(events.NewMessage(chats=5364964725, from_users="@OrdinalLegacybot"))
async def hunt_handler(event):
    global hunt_active
    global ultimate 
    if not hunt_active:
        return
    if "Pick" in event.raw_text or "pick" in event.raw_text:
        if event.message.reply_markup:
            if ultimate:
                ultimate = False
                await asyncio.sleep(2)
                await event.click(2)
            else :
                await asyncio.sleep(2)
                await event.click(0)
    elif "identified" in event.raw_text or "next?" in event.raw_text:
        if event.message.reply_markup:
            ultimate = True
            await asyncio.sleep(2)
            await event.click(0)
    elif "grant" in event.raw_text or "Common" in event.raw_text or "While" in event.raw_text or "rare" in event.raw_text or "while" in event.raw_text:
        ultimate = True
        await event.respond("/explore")

@bot.on(events.MessageEdited(chats=5364964725, from_users="@OrdinalLegacybot"))
async def edited_hunt_handler(event):
    global hunt_active
    global ultimate 
    if not hunt_active:
        return
    if "Pick" in event.raw_text or "pick" in event.raw_text:
        if event.message.reply_markup:
            if ultimate :
                ultimate = False
                await asyncio.sleep(2)
                await event.click(2)
            else :
                await asyncio.sleep(2)
                await event.click(0)
    elif "identified" in event.raw_text or "next?" in event.raw_text :
        if event.message.reply_markup:
            ultimate = True
            await asyncio.sleep(2)
            await event.click(0)
    elif "enough" in event.raw_text :
        ultimate = True
        await event.respond("/explore")
        
@hell_cmd(pattern="stopexplore$")
async def hunt_stop(event):
    global hunt_active
    if hunt_active:
        hunt_active = False
        await event.edit("explore stopped.")
    else:
        await event.edit("explore is not active in this chat.")

CmdHelp("hunt").add_command(
    "explore", None, "Starts sending /explore in the specified chat and clicks on the first inline button repeatedly if message contains 'identified' or your full name (Telegram username)."
).add_command(
    "stopexplore", None, "Stops sending /explore in the specified chat."
).add()
