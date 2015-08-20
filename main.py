# @author: Fred Lee

from RiotAPI import RiotAPI
import API_KEY as API_KEY

def main():
	#this is my Developer API KEY
	api = RiotAPI(API_KEY.key) 
	r = api.get_summoner_by_name('TET Panda')
	print (r)
	print (type(r))
	print (r['tetpanda']['id'])

if __name__ == "__main__":
	main()