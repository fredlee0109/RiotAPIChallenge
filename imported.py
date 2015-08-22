# @author: Fred Lee

from RiotAPI import RiotAPI
import API_KEY as API_KEY
from pprint import pprint
import json

class imported(object):

	def __init__(self):
		summoners = {}
		spells = {}
		banned_Champions = {}
		picked_Champions = {}

		with open('Data/summonerData.txt') as data_file:
			summoners = dict(json.load(data_file))
		
		with open('Data/bannedData.txt') as data_file:
			banned_Champions = dict(json.load(data_file))

		with open('Data/pickedData.txt') as data_file:
			picked_Champions = dict(json.load(data_file))

		with open('Data/spellData.txt') as data_file:
			spells = dict(json.load(data_file))

		self.summoners = summoners
		self.spells = spells
		self.banned_Champions = banned_Champions
		self.picked_Champions = picked_Champions

	def request_summoners(self):
		return self.summoners

	def request_spells(self):
		return self.spells

	def request_banned_Champions(self):
		return self.banned_Champions

	def request_picked_Champions(self):
		return self.picked_Champions