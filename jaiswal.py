def countPlayers(player_class_object_list, country_name):
	count = 0
	for i in player_class_object_list:
		if i.countryFrom == country_name:
			count += 1
	return count

def getPlayerPlayedForMaxCountry(player_class_object_list):
	maxi = -1
	max_player = player_class_object_list[0].playerName
	for i in range(len(player_class_object_list)):
		curr_length = len(player_class_object_list[i].playedCountry)
		if  curr_length > maxi:
			max_player = player_class_object_list[i].playerName
			maxi = curr_length
	return max_player



class Player:

	def __init__(self, playerName, playedCountry, playerAge, countryFrom):
		self.playerName = playerName
		self.playedCountry = playedCountry
		self.playerAge = playerAge
		self.countryFrom = countryFrom


if __name__ == '__main__':
	player_list = []
	n_players = int(input())
	for i in range(n_players):
		playerName = input().strip()
		n_played_country = int(input())
		played_country = []
		for i in range(n_played_country):
			z = input().strip()
			played_country.append(z)

		playerAge = int(input())
		countryFrom = input().strip()
		player = Player(playerName, played_country, playerAge, countryFrom)
		player_list.append(player)
	last_line = input().strip()
	ans1 = countPlayers(player_list, last_line)
	ans2 = getPlayerPlayedForMaxCountry(player_list)
	print(ans1)
	print(ans2)
