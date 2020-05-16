from redbot.core import commands, checks
from .ase import fetch_data
import time

class Stats(commands.Cog):
    """My custom cog"""

    @commands.group()
    async def stats(self, ctx):
        """MTA:SA Stats!"""
        pass

    @stats.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.guild_only()
    async def online(self, ctx):
        """Shows MTA's online players count"""
        total = 0
        start = time.time()
        servers = fetch_data()
        took = time.time() - start
        for server in servers:
            total += server.playersCount 
        await ctx.channel.send("There are currently "+str(total)+" players online! Timing: "+str(took))

    @stats.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.guild_only()
    async def top(self, ctx):
        """Shows the servers with most players."""
        top = ""
        peak = 0
        servers = fetch_data()
        for server in servers:
            if peak < server.playersCount:
                peak = server.playersCount
                top = server.serverName
        await ctx.channel.send("`"+top+"` with "+str(peak)+" players!")