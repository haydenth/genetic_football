Draftday.com Genetic Algorithm Optimizer
================


What is this thing?
===============

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
=======================

To run the optimizer, you can download data from Draftday.com. When you're on a game screen, click "EXPORT TO SPREADSHEET" and it will download a CSV file of all the players, estimates, and costs for the week. 
