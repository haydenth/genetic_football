from common.player import Player, PlayerList
from common.simulator import Configuration, DraftDay, DefenseList
import argparse
import copy
import random
import sys

parser = argparse.ArgumentParser(description='Simulate some drafts')
parser.add_argument('--file', type=str, help='file to load', required=True)
parser.add_argument('--defense', type=str, help='defense adj file to load')
parser.add_argument('--override', type=str, help='point override custom file')
parser.add_argument('--injuries', type=int,
                    help='0-4, where 0 is no injuries and 4 is everyone')
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
if args.injuries is not None:
  player_list.adjust_for_injuries(args.injuries)

config = DraftDay().simulate(player_list)
config.print_roster()
