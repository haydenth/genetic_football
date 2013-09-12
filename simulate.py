from common import Player, PlayerList, Configuration, DraftDay
import argparse
import copy
import random
import sys

parser = argparse.ArgumentParser(description='Simulate some drafts')
parser.add_argument('--file', type=str, help='file to load', required=True)
args = parser.parse_args()

player_list = PlayerList(PlayerList.POSITIONS)
player_list.read_from_draftday_csv(args.file)

config = DraftDay().simulate(player_list, 50000)
config.print_roster()
