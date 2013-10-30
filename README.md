Draftday.com Optimizer
================


What is this thing?
-------------------

For the unfamiliar, draftday.com is a psuedo-maybe-gambling website. Each week, you select a configuration of NFL players with a buy-in. The games happen and you get fantasy style points. Different games have different payouts but, in general, the more points you score, the better.

What makes draftday unique (and computationally interesting) is that, for each player, there is a *cost constraint*. You're given a salary of usually $100,000 and you have to divvy it up among your team. For example, for a given week, the players will cost:

```
Position,PlayerName,Team,Opponent,Salary,PPG
QB,Matt Ryan,Falcons,Cardinals,15550,24.5
QB,Andy Dalton,Bengals,Jets,14250,19.2
QB,Carson Palmer,Cardinals,Falcons,11150,12.9
QB,Tony Romo,Cowboys,Lions,16300,23.3
QB,Matthew Stafford,Lions,Cowboys,18100,24.4
QB,Matt Flynn,Bills,Saints,7400,5.1
QB,Aaron Rodgers,Packers,Vikings,19450,25.6
QB,Peyton Manning,Broncos,Redskins,23500,34.9
```

Running the Optimizer
-----------------------

To run the optimizer, you can download data from Draftday.com. When you're on a game screen, click "EXPORT TO SPREADSHEET" and it will download a CSV file of all the players, estimates, and costs for the week. Once you've downloaded it, pull up a terminal and run simulate.py with the --file flag. Here's what it should look like:
```
python simulate.py --file csv/sample_week8.csv
```

As it runs the optimizer, it will find various local maximums before it will probably settle on something that is hopefully a global maximum. Here's an example of the output:
```
========== new max!! 34777 ======= 
[FLEX] Justin Blackmon FLEX (23.100000, 12450, SF)
[D] Chiefs D (17.900000, 8200, CLE)
[K] Matt Prater K (12.200000, 6000, WAS)
[RB2] Joique Bell RB (12.800000, 5000, DAL)
[RB1] Fred Jackson RB (16.400000, 8800, NO)
[QB] Peyton Manning QB (34.900000, 23500, WAS)
[WR2] DeSean Jackson WR (18.300000, 13150, NYG)
[WR1] Antonio Brown WR (19.400000, 12300, OAK)
[TE] Jordan Cameron TE (18.900000, 10250, KC)
Total Cost = 99650 Total Value = 173.900000
```

Removing Injuries
----------------------

The simulator has the ability to automatically removed injured players (by scraping CBS's injury report). There are four different levels of injures to consider:

```
0 = remove ALL injured players
1 = remove only Doubtful, Out, Questionable, Prob
2 = remove only Doubtful, Out, Questionable
3 = remove only Doubtful, Out
4 = remove nobody (default)
```

To do this, just include the --injuries flag
```
python simulate.py --file csv/sample_week8.csv --injuries 1
```

Requirements
----------------------
To run this, you need:
* python 2.7 
* urllib2 module (should be installed)

Caveats
----------------------
Some caveats:
* The Draftday PPG estimates suck. It helps if you can go out and get better estimates. Better input = better output.
