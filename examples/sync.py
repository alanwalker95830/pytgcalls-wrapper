from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls_wrapper import SyncWrapper

client = Client(
    "user",
    api_id=0,
    api_hash=""
)
pytgcalls = PyTgCalls(client)
wrapper = SyncWrapper(pytgcalls, "raw")


@client.on_message(filters.me & filters.command("stream", ";"))
def stream(_, m):
    wrapper.stream(m.chat.id, "https://www.youtube.com/watch?v=9KAQaKydqA0")


@client.on_message(filters.me & filters.command("pause", ";"))
def pause(_, m):
    wrapper.pause(m.chat.id)


@client.on_message(filters.me & filters.command("resume", ";"))
def resume(_, m):
    wrapper.resume(m.chat.id)


pytgcalls.run()
