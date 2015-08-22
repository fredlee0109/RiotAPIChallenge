# @author: Fred Lee

from RiotAPI import RiotAPI
from imported import imported
import API_KEY as API_KEY
import time
import json
from pprint import pprint

def main():

	importe = imported()
	summoners = importe.request_summoners()
	spells = importe.request_spells()
	banned_Champions = importe.request_banned_Champions()
	picked_Champions = importe.request_picked_Champions()


	static = RiotAPI(API_KEY.key, 'global')
	s = static.get_champion_to_id()

	id_to_champs = {}
 	for champ in s['data']:
 		id_to_champs[s['data'][champ]['id']] = str(s['data'][champ]['name'])

	# summoners = {}
	# spells = {}
	# banned_Champions = {}
	# picked_Champions = {}
	id_to_spells = {
		11 : "Smite", 12 : "Teleport", 14 : "Ignite", 3 : "Exhaust", 4 : "Flash", 7 : "Heal", 
		21 : "Barrier", 1 : "Cleanse", 6 : "Ghost", 32 : "Mark", 13 : "Clarity", 2 : "Clairvoyance"
	}
	# # seconds * # minutes * # hours
	t_end = time.time() + 60 * 60 * 8
	while time.time() < t_end:
		api = RiotAPI(API_KEY.key) 
		r = api.get_featured_game()
		if (r.has_key('status')):
			print r
		else:
			for game in r['gameList']:
				for player in game['participants']:
					if summoners.has_key(player['summonerName']):
						summoners[player['summonerName']] += 1
					else:
						summoners[player['summonerName']] = 1
					if spells.has_key(id_to_spells[player['spell1Id']]):
						spells[id_to_spells[player['spell1Id']]] += 1
					else:
						spells[id_to_spells[player['spell1Id']]] = 1
					if spells.has_key(id_to_spells[player['spell2Id']]):
						spells[id_to_spells[player['spell2Id']]] += 1
					else:
						spells[id_to_spells[player['spell2Id']]] = 1
					if picked_Champions.has_key(id_to_champs[player['championId']]):
						picked_Champions[id_to_champs[player['championId']]] += 1
					else:
							picked_Champions[id_to_champs[player['championId']]] = 1
				for bannedChamps in game['bannedChampions']:
					if banned_Champions.has_key(id_to_champs[bannedChamps['championId']]):
						banned_Champions[id_to_champs[bannedChamps['championId']]] += 1
					else:
						banned_Champions[id_to_champs[bannedChamps['championId']]] = 1
		time.sleep(60)


	with open('Data/summonerData.txt', 'w') as outfile:
		json.dump(sorted(summoners.items(), key=lambda x: x[1], reverse=True), outfile)
	with open('Data/bannedData.txt', 'w') as outfile:
		json.dump(sorted(banned_Champions.items(), key=lambda x: x[1], reverse=True), outfile)
	with open('Data/pickedData.txt', 'w') as outfile:
		json.dump(sorted(picked_Champions.items(), key=lambda x: x[1], reverse=True), outfile)
	with open('Data/spellData.txt', 'w') as outfile:
		json.dump(sorted(spells.items(), key=lambda x: x[1], reverse=True), outfile)

if __name__ == "__main__":
	main()