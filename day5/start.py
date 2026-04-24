# import kl4
#
# print(kl4.kur2)  # Kura zielononóżka, 0
import pakiet

print(50 * "-")
# AttributeError: module 'pakiet' has no attribute 'powitanie'
# pakiet.powitanie()
pakiet.info()
# v3.456.90.0000

from pakiet import fun

fun.powitanie()
# --------------------------------------------------
# Jestem pakietem

import pakiet.fun as pk  # alias

pk.powitanie()  # Jestem pakietem
