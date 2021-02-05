import json
import requests

from .errors import *


class Dashboard:	
	def __init__(self, bot, key, url, *args, **kwargs):
		"""Initialize the dashboard"""
		self.bot = bot
		self.key = key
		self.url = url
		self.routes = {}
		
		
	def route(self, func):
		if func.__name__ in self.routes.keys():
			raise DuplicateRoute("that route already exists")
		self.routes[func.__name__] = func
		
		
	async def process_request(self, message):
		if not message.author.bot:
			return
		
		try:
			r = json.loads(message.content)
		
		except:
			return
			
		if r.get("Authorization") != self.key:
			return
			
		
		if r.get("route") not in self.routes.keys():
			raise RouteNotFound("the requested route does not exist")
			
		
		else:
			result = await self.routes[r["route"]](r.get("data"))
			
			requests.post(self.url, headers={"Authorization": self.key}, json={"data": result})
			
		return {"error": False, "message": "Request processed successfully"}
