# Glories of Featured Games

Ever wondered what it takes to be featured by Riot Games? Ever wondered how featured games differ from non-featured games? This is an entry for Riot's League of Legends API challenge that generates a visualisation of statistics of champions banned and selected, spells selected, and summoner names in featured games

## Workings

API_KEY.py contained the api key as:
key = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'


retrieve.py was executed every minute, with imported time methods. This populated the directory with the matches from the bucket list.

parse_matches.py was then executed to produce a winmap file.

The winmap file could be hosted separately, or copied into supermegacountertable.html to render the visualisation.

## Disclaimer

Super Mega Counter Table isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.