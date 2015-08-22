# @author: Fred Lee

from RiotAPI import RiotAPI
import API_KEY as API_KEY
import time

def main():
	api = RiotAPI(API_KEY.key) 
	r = api.get_featured_game()

	static = RiotAPI(API_KEY.key, 'global')
	s = static.get_champion_to_id()

	id_to_champs = {}
 	for champ in s['data']:
 		id_to_champs[s['data'][champ]['id']] = str(s['data'][champ]['name'])

	summoners = {}
	spells = {}
	banned_Champions = {}
	picked_Champions = {}
	id_to_spells = {
		11 : "Smite", 12 : "Teleport", 14 : "Ignite", 3 : "Exhaust", 4 : "Flash", 7 : "Heal", 
		21 : "Barrier", 1 : "Cleanse", 6 : "Ghost", 32 : "Mark", 13 : "Clarity", 2 : "Clairvoyance"
	}
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



	# run for 24 hours
	# t_end = time.time() + 60 * 24
	# bannedChampions = {}
	# pickedChampions = {}
	# summoners = {}
	# spells = {}
	# while time.time() , t_end:
	# 	s = api.get_featured_game()
	# 	time.sleep(60)
	
	# f = open("summonerData.txt", 'w')
	# f.write(summoners)
	# f.close()
	# f = open("bannedData.txt", 'w')
	# f.write(bannedChampions)
	# f.close()
	# f = open("pickedData.txt", 'w')
	# f.write(pickedChampions)
	# f.close()
	# f = open("spellData.txt", 'w')
	# f.write(spells)
	# f.close()

if __name__ == "__main__":
	main()