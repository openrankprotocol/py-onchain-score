
def main():
    import asyncio, sys
    sys.exit(asyncio.run(_main()))


async def _main():
    print("Hello, world!")