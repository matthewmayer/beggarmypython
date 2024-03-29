Does an infinite game of [Beggar-My-Neighbour](http://en.wikipedia.org/wiki/Beggar-My-Neighbour) exist? 

Yes!

This question has definitely not plagued scientists for millennia. However, in the event that you think you have found a very long game of Beggar My Neighbour, you might wish to run it through a Beggar My Neighbour simulator written in Python. You can see a full list of record holders here: http://richardpmann.weebly.com/beggar-my-neighbour-records.html 

In 2024, Brayden Casella finally found an infinite game. You can read about his methodology in [this paper](https://arxiv.org/abs/2403.13855).

Usage:

````
python test.py
````

Output:

````
Paulhus 1999:
Starting hands: ------------KAQ----J------/-JQQK---K----JK--QA-A-JA--
There were 4791 turns
There were 670 tricks

Kleber 1999:
Starting hands: ---JQ---K-A----A-J-K---QK-/-J-----------AJQA----K---Q
There were 5790 turns
There were 805 tricks

Collins 2006:
Starting hands: A-QK------Q----KA-----J---/-JAK----A--Q----J---QJ--K-
There were 6913 turns
There were 960 tricks

Mann and Wu 2007:
Starting hands: K-KK----K-A-----JAA--Q--J-/---Q---Q-J-----J------AQ--
There were 7157 turns
There were 1007 tricks

Nessler 2012:
Starting hands: ----Q------A--K--A-A--QJK-/-Q--J--J---QK---K----JA---
There were 7207 turns
There were 1015 tricks

Anderson 2013:
Starting hands: --A-Q--J--J---Q--AJ-K---K-/-J-------Q------A--A--QKK-
There were 7225 turns
There were 1016 tricks

Rucklidge 2014:
Starting hands: -J------Q------AAA-----QQ-/K----JA-----------KQ-K-JJK
There were 7959 turns
There were 1122 tricks

Nessler 2021:
Starting hands: ----K---A--Q-A--JJA------J/-----KK---------A-JK-Q-Q-Q
There were 7972 turns
There were 1106 tricks

Nessler 2022:
Starting hands: ---AJ--Q---------QAKQJJ-QK/-----A----KJ-K--------A---
There were 8344 turns
There were 1164 tricks

Brayden Casella 2024:
Starting hands: ---K---Q-KQAJ-----AAJ--J--/----------Q----KQ-J-----KA
Game appears to be infinite, loop detected after 474 turns and 66 tricks
````

If you care about the non-court cards then you have to wait longer for the loop to occur. Passing the `substituteValuesForNonCourtCards` flag lets you quickly test this by replacing the - with greek and cyrillic letters.
````
Including unique non-court cards:
Starting hands: αβγKδεζQηKQAJθιλμνAAJξοJπρ/αβγδεζηθιλQμνξοKQπJρστυφKA
Game appears to be infinite, loop detected after 33034 turns and 4654 tricks
````

We already knew about [alternate versions of the game](https://github.com/matthewmayer/beggarmypython/pull/5) that do not terminate, entering an infinite loop. For example the Italian game of Camicia uses a 40-card deck and no draw-4 cards (aces).
```
Carmicia
Starting hands: --Q------QJ----JK---/---Q---J-Q-KJ--K-K--
Game appears to be infinite, loop detected after 197 turns and 37 tricks
```

While this Python code is fine for verifying a single game, if you wish to test large numbers of games to beat the current records, you almost certainly want to use a faster compiled language. 
* https://github.com/LeoDog896/beggar-my-neighbour (uses Rust)
