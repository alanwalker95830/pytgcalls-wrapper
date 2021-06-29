import re


def is_youtube_link(s: str) -> bool:
    return bool(re.match(f"^(http|https)://((youtu\.be/.+)|(youtube\.com/watch\?v=.+))$", s))
