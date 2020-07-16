import random
import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--offline", default=False, help="use offline storage instead of web-request")
args = parser.parse_args()

def online_parser():
    wiki_url = "https://en.wikipedia.org/wiki/List_of_Rick_and_Morty_episodes"
    wiki_html = requests.get(wiki_url).text

    soup = BeautifulSoup(wiki_html, "html.parser")
    seasons = { i+1: { "season_header": x } for i, x in enumerate([x for x in soup.find_all('span', {'class': 'mw-headline'}) if "Season" in x.text ]) }

    episodes = []
    for season_number, season in seasons.items():
        season_table = season["season_header"].parent.findNext('table', {'class': 'wikitable'})
        season_table_rows = season_table.find_all('tr', {'class': 'vevent'})
        for tr in season_table_rows:
            tds = [x.text for x in tr.find_all('td')]
            season["season_contents"] = tds
            episodes.append({ "season": season_number, "episode_in_season": tds[0], "title": tds[1] })

    for i, e in enumerate(episodes):
        e["episode_overall"] = i

    return episodes

def offline_parser():
    # episodes came from https://en.wikipedia.org/wiki/List_of_Rick_and_Morty_episodes
    # with replaced \[\w+\] ->

    f = open("episodes.txt", "r").read()
    eps_raw = [ l.split("\t") for l in f.split("\n") if l != "" ]
    eps = [ { "episode_overall": e[0], "episode_in_season": e[1], "title": e[2].replace('"', '') } for e in eps_raw ]

    s = 0
    for i, x in enumerate(eps):
        if int(x["episode_in_season"]) == 1: s+= 1
        eps[i]["season"] = s
    
    return eps

def show_me_what_you_got():
    print("        ___")
    print("    . -^   `--,")
    print("   /# =========`-_")
    print("  /# (--====___====\\")
    print(" /#   .- --.  . --.|")
    print("/##   |  * ) (   * ),")
    print("|##   \    /\ \   / |  ┌─┐┬ ┬┌─┐┬ ┬  ┌┬┐┌─┐")
    print("|###   ---   \ ---  |  └─┐├─┤│ ││││  │││├┤ ")
    print("|####      ___)    #|  └─┘┴ ┴└─┘└┴┘  ┴ ┴└─┘")
    print("|######           ##|  ┬ ┬┬ ┬┌─┐┌┬┐  ┬ ┬┌─┐┬ ┬  ┌─┐┌─┐┌┬┐")
    print(" \\##### ---------- /   │││├─┤├─┤ │   └┬┘│ ││ │  │ ┬│ │ │ ")
    print("  \\####           (    └┴┘┴ ┴┴ ┴ ┴    ┴ └─┘└─┘  └─┘└─┘ ┴ ")
    print("   `\\###          |")
    print("     \\###         |")
    print("      \\##        |")
    print("       \\###.    .)")
    print("        `======/")
    print("")

if __name__ == "__main__":
    episodes = offline_parser() if args.offline else online_parser()

    selected_ep = episodes[random.randint(0, len(episodes)-1)]
    
    show_me_what_you_got()
    print(f'Selected Episode: s{selected_ep["season"]}e{selected_ep["episode_in_season"]} -- {selected_ep["title"]}')
