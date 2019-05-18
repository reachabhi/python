users = [{"name":"chess","player":"Topalava","matches":73, "country":"Russia"}, 
		 {"name":"football", "player":"Ronaldo", "matches":98}, 
		 {"name":"basketball", "player":"Michael","matches":110}, 
		 {"name":"tennis","player":"Nadal","matches":90,"court":"clay","wins":50},
		 {"name":"cricket","player":"dhoni","matches":300}]

print(sorted(users, key=len)) #sorts the dictionary based on length of items i.e. number of k:v pairs
print(sorted(users, key = lambda x : x['name'])) #sorts the dictionary based on the name key 
print(sorted(users, key = lambda x : x['matches'], reverse = True)) #reverses 

print(min(users, key = lambda m:m['matches'])) #min method to find the minimum number of matches
print(max(users, key = lambda m:m['matches'])['player']) #prints the player with max matches