import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import json
import asyncio

from .errors import *

class Server:
	def __init__(self, server, key, *args, **kwargs):
		"""Initialize the server"""
		if not kwargs.get("webhook_url"):
			raise TypeError("__init__() missing one required positional argument: 'webhook_url'")
		
		self.server = server	
		self.key = key
		self.webhook_url = kwargs.get("webhook_url")
		self.data = {}
		
		
	async def request(self, route, *args, **kwargs):
		"""Send a request to the bot"""
		request_data = {"Authorization": self.key, "route": route, "data": kwargs}
		
		request = json.dumps(request_data)
		
		async with aiohttp.ClientSession() as session:
			webhook = Webhook.from_url(self.webhook_url, adapter=AsyncWebhookAdapter(session))
			await webhook.send(request)
			
		await asyncio.sleep(.4)
		
		data = self.data.pop(name, None) or self.data.pop(route, None)

		return data

	
	async def process_request(self, request):
		"""Processes the returned data from the bot"""
		r = await request.json
		
		if request.headers.get("Authorization") != self.key:
			raise InvalidAuthorization("invalid key provided")
			
		if r.get("name"):
			self.data[r["name"]] = r["data"]
