from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls_wrapper import Wrapper

client = Client(
    "user",
    api_id=0,
    api_hash=""
)
pytgcalls = PyTgCalls(client)
wrapper = Wrapper(pytgcalls, "raw")


@client.on_message(filters.me & filters.command("stream", ";"))
async def stream(_, m):
    await wrapper.stream(m.chat.id, "https://www.youtube.com/watch?v=9KAQaKydqA0")


@client.on_message(filters.me & filters.command("pause", ";"))
async def pause(_, m):
    wrapper.pause(m.chat.id)


@client.on_message(filters.me & filters.command("resume", ";"))
async def resume(_, m):
    wrapper.resume(m.chat.id)


pytgcalls.run()
