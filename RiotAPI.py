# @author: Fred Lee

import requests
import RiotConst as Consts

class RiotAPI(object):

	def __init__(self, api_key, region=Consts.REGIONS['north_america']):
		self.api_key = api_key
		self.region = region

	def _request(self, api_url, params=()):
		args = {'api_key': self.api_key}
		for key, value in params:
			if key not in args:
				args[key] = value
		response = requests.get(
			Consts.URL['base'].format(
				proxy=self.region,
				region=self.region,
				url=api_url),
			params=args
			)
		return response.json()

	def get_summoner_by_name(self, name):
		api_url = Consts.URL['summoner_by_name'].format(
			version=Consts.API_VERSIONS['summoner'],
			summonerNames=name
			)
		return self._request(api_url)

class LolException(Exception):
	def __init__(self, error, response):
		self.error = error
		self.headers = response.headers

	def __str__(self):
		return self.error

error_400 = "Bad request"
error_401 = "Unauthorized"
error_404 = "Game data not found"
error_429 = "Too many requests"
error_500 = "Internal server error"
error_503 = "Service unavailable"

def raise_status(response):
    if response.status_code == 400:
        raise LoLException(error_400, response)
    elif response.status_code == 401:
        raise LoLException(error_401, response)
    elif response.status_code == 404:
        raise LoLException(error_404, response)
    elif response.status_code == 429:
        raise LoLException(error_429, response)
    elif response.status_code == 500:
        raise LoLException(error_500, response)
    elif response.status_code == 503:
        raise LoLException(error_503, response)
    else:
        response.raise_for_status()