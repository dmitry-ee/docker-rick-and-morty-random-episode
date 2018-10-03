import random

# episodes came from https://en.wikipedia.org/wiki/List_of_Rick_and_Morty_episodes
# with replaced \[\w+\] -> 

f = open("episodes.txt", "r").read()
eps_raw = [ l.split("\t") for l in f.split("\n") if l != "" ]
eps = [ { "episode_overall": e[0], "episode_in_season": e[1], "title": e[2].replace('"', '') } for e in eps_raw ]

s = 0
for i, x in enumerate(eps):
    if int(x["episode_in_season"]) == 1: s+= 1
    eps[i]["season"] = s

selected_ep = eps[random.randint(0, len(eps))]

print("Selected Episode: s%se%s -- %s" % ( selected_ep["season"], selected_ep["episode_in_season"], selected_ep["title"] ))
