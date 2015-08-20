# @author: Fred Lee

URL = {
	'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
	'summoner_by_name': 'v{version}/summoner/by-name/{summonerNames}',
	# 'obs': ''
}

#this will be the {version}
API_VERSIONS = { 
	'summoner': '1.4'
}

#this will be the {proxy}
REGIONS = { 
	'north_america': 'na',
	'korea': 'kr',
	'brazil': 'br',
	'europe_nordic_east': 'eune',
	'europe_west': 'euw',
	'latin_america_north': 'lan',
	'latin_america_south': 'las',
	'oceania': 'oce',
	'russia': 'ru',
	'turkey': 'tr'
}