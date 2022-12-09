A = Rock, 
B = Paper,
C = Scissors

X = Rock,
Y = Paper,
Z = Scissors

Total score = sum of scores for each round

Round score = score for shape played( rock= **1**, paper= **2**, scissors= **3**) + score of round result( loss= **0**, draw= **3**, win= **6**)

## Part two
Turns out the key is actually X = lose, Y = draw, Z = win.

Wish I'd written this note before attempting solution, my initial attempt would have been correct but I had X and Z swapped and it took a lot of print debugging to catch that.