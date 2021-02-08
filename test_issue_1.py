#!/usr/bin/python
import beggarmypython

print("Issue #1 - should be 52 plays:")
beggarmypython.play(('--------------------------','--------------------------'), verbose=False)

print("Anderson 2013 - should be 7225 turns (as before fix):")
beggarmypython.play(('--A-Q--J--J---Q--AJ-K---K-','-J-------Q------A--A--QKK-'),verbose=False)

print("Rucklidge 2014 - should be 7959 plays:")
beggarmypython.play(('-J------Q------AAA-----QQ-','K----JA-----------KQ-K-JJK'), verbose=False)