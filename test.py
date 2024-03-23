#!/usr/bin/python
import beggarmypython
print("Carmicia (smaller deck)")
beggarmypython.play(('--Q------QJ----JK---', '---Q---J-Q-KJ--K-K--'))

print("Paulhus 1999:")
beggarmypython.play(('------------KAQ----J------',
                    '-JQQK---K----JK--QA-A-JA--'), verbose=False)

print("Kleber 1999:")
beggarmypython.play(('---JQ---K-A----A-J-K---QK-',
                    '-J-----------AJQA----K---Q'), verbose=False)

print("Collins 2006:")
beggarmypython.play(('A-QK------Q----KA-----J---',
                    '-JAK----A--Q----J---QJ--K-'), verbose=False)

print("Mann and Wu 2007:")
beggarmypython.play(('K-KK----K-A-----JAA--Q--J-',
                    '---Q---Q-J-----J------AQ--'), verbose=False)

print("Nessler 2012:")
beggarmypython.play(('----Q------A--K--A-A--QJK-',
                    '-Q--J--J---QK---K----JA---'), verbose=False)

print("Anderson 2013:")
beggarmypython.play(('--A-Q--J--J---Q--AJ-K---K-',
                    '-J-------Q------A--A--QKK-'), verbose=False)

print("Rucklidge 2014:")
beggarmypython.play(('-J------Q------AAA-----QQ-',
                    'K----JA-----------KQ-K-JJK'), verbose=False)

print("Nessler 2021:")
beggarmypython.play(('----K---A--Q-A--JJA------J',
                    '-----KK---------A-JK-Q-Q-Q'), verbose=False)

print("Nessler 2022:")
beggarmypython.play(('---AJ--Q---------QAKQJJ-QK',
                    '-----A----KJ-K--------A---'), verbose=False)

print("Brayden Casella 2024:")
beggarmypython.play(('---K---Q-KQAJ-----AAJ--J--',
                    '----------Q----KQ-J-----KA'), verbose=False)

print("\nIncluding unique non-court cards:")
beggarmypython.play(('---K---Q-KQAJ-----AAJ--J--',
                    '----------Q----KQ-J-----KA'), verbose=False, substituteValuesForNonCourtCards=True)
