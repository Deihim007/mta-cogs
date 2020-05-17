from .mod import ModReq


async def setup(bot):
    cog = ModReq(bot)
    bot.add_cog(cog)
    await cog.initialize()