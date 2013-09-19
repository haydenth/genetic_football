from common import Player, PlayerList, Configuration, DraftDay, DefenseList
import argparse
import copy
import random
import sys

parser = argparse.ArgumentParser(description='Simulate some drafts')
parser.add_argument('--file', type=str, help='file to load', required=True)
parser.add_argument('--defense', type=str, help='defense adj file to load')
parser.add_argument('--override', type=str, help='point override custom file')
args = parser.parse_args()

player_list = PlayerList(PlayerList.POSITIONS)
player_list.read_from_draftday_csv(args.file)

if args.override:
  override_list = PlayerList(PlayerList.POSITIONS)
  override_list.read_from_custom_csv_simple(args.override)
  player_list.override_values(override_list)

if args.defense:
    def_list = DefenseList()
    def_list.read_from_custom(args.defense)
    player_list.adjust_for_defenses(def_list)

config = DraftDay().simulate(player_list, 50000)
config.print_roster()
