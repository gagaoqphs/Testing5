from telethon import events
from tg_bot import from telethon import events
from tg_bot import oko

"""Triggers start command in pm and in groupchats"""
def luffybot(**args):
    """New message."""
    pattern = args.get('pattern', None)
    r_pattern = r'^[/!]'
    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern
    args['pattern'] = pattern.replace('^/', r_pattern, 1)

    def decorator(func):
        oko.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def inlinequery(**args):
    """Inline query."""
    pattern = args.get('pattern', None)
    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern

    def decorator(func):
        oko.add_event_handler(func, events.InlineQuery(**args))
        return func

    return decorator


def userupdate(**args):
    """User updates."""

    def decorator(func):
        oko.add_event_handler(func, events.UserUpdate(**args))
        return func

    return decorator


def callbackquery(**args):
    """Callback query."""

    def decorator(func):
        oko.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator


def chataction(**args):
    """Chat actions."""

    def decorator(func):
        oko.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


"""Triggers start command in pm and in groupchats"""
def luffybot(**args):
    """New message."""
    pattern = args.get('pattern', None)
    r_pattern = r'^[/!]'
    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern
    args['pattern'] = pattern.replace('^/', r_pattern, 1)

    def decorator(func):
        oko.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def inlinequery(**args):
    """Inline query."""
    pattern = args.get('pattern', None)
    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern

    def decorator(func):
        oko.add_event_handler(func, events.InlineQuery(**args))
        return func

    return decorator


def userupdate(**args):
    """User updates."""

    def decorator(func):
        oko.add_event_handler(func, events.UserUpdate(**args))
        return func

    return decorator


def callbackquery(**args):
    """Callback query."""

    def decorator(func):
        oko.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator


def chataction(**args):
    """Chat actions."""

    def decorator(func):
        oko.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator
