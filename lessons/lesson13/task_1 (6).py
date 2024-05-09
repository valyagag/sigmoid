# Aceasta este sarcina pentru lecția despre clase și conceptele de bază ale programării orientate pe obiecte în Python.

from sigmoid_check.python_odyssey.lesson_13.lesson_13 import Lesson13

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.5
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.5

# VERIFICATION PROCESS
session = Lesson13()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE:
Această temă va fi puțin mai diferită decât deobicei, cei de la DARWIN au apelat la serviciile noastre ca să-i ajutăm să organizeze produsele acestora.
Procesul lor de vindere a unui produs durează foarte mult din cauza la sistemul lor învechit de structurare a produselor, iar clienții sunt nemulțumiți.

Din păcate noi suntem ocupați cu procesele de organizare a Python Odyssey Camp și nu reușim la timp să realizăm sistemul nou. Dar în schimb voi puteți, aveți toate cunoștințele necesare.
Și plus la asta noi avem încredere că o să vă desurcați și o să rezolvați problema în timp util.
"""

"""
Pentru început o să ne ocupăm de dirijarea și managementul produselor.
1. Avem nevoie să creezi o clasă `Produs`, aceasta trebuie să accepte 3 parametri: numele, pretul, anul_producerii
Cu ajutorul acestei clase trebuie să fiu capabil să creeze câte obiecte doresc cu orice configurație a numelui, prețului și anul_producerii

Exemplu utilizare:
telefon = Produs("Iphone", 15000, 2020) # Voi putea crea un obiect utilizând anumiți parametri de intrare
print(telefon.numele)                   # Voi putea accesa numele obiectului creat
print(telefon.pretul)                   # Voi putea accesa pretul obiectului creat
print(telefon.anul_producerii)          # Voi putea accesa anul producerii obiectului creat
"""

# CODUL TĂU VINE MAI JOS:
class Produs:
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(Produs))
# VERIFICATION PROCESS

"""
DARWIN de asemenea a mai menționat că unele produse au nevoie de o descriere mai detaliată a parametrilor și informațiilor pe care le dețin.
2. Avem nevoie de trei clase noi care să moștenească clasa `Produs`:
"""

"""
2.1Prima clasă se numește `Telefon` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `baterie_mAh` și `memorie_GB`

De asemenea aceasta va avea o metodă numită `upgrade_memory` care va primi un parametru `new_memory` și va actualiza valoarea memoriei telefonului.
Totodată aceasta va avea o metodă numită `upgrade_battery` care va primi un parametru `new_battery` și va actualiza valoarea bateriei telefonului.
"""

# CODUL TĂU VINE MAI JOS:
class Telefon( ):
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(Telefon, Produs))
# VERIFICATION PROCESS

"""
2.2 A doua clasă se numește `Laptop` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `sistem_de_operare` și `procesor`

De asemenea aceasta va avea o metodă numită `upgrade_processor` care va primi un parametru `new_processor` și va actualiza valoarea procesorului laptopului.
Totodată aceasta va avea o metodă numită `upgrade_os` care va primi un parametru `new_os` și va actualiza valoarea sistemului de operare al laptopului.
"""

# CODUL TĂU VINE MAI JOS:
class Laptop( ):
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(Laptop, Produs))
# VERIFICATION PROCESS

"""
2.3 A treia clasă se numește `trotineta` aceasta va moșteni clasa `Produs` și va avea doi parametri în plus numit `viteza_maxima` și `autonomie_km`

De asemenea aceasta va avea o metodă numită `upgrade_speed` care va primi un parametru `new_speed` și va actualiza valoarea vitezei maxime a trotinetei.
Totodată aceasta va avea o metodă numită `upgrade_autonomy` care va primi un parametru `new_autonomy` și va actualiza valoarea autonomiei trotinetei.
"""

# CODUL TĂU VINE MAI JOS:
class Trotineta( ):
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(Trotineta, Produs))
# VERIFICATION PROCESS

"""
3 DARWIN a mai lăsat o mică notiță după ei, au menționat că mulți cumpărători sunt interesați de produsele apple și adesea acestea le combină între ele.

Avem nevoie de o clasă nouă care să se numească `AppleProduct` care va moșteni clasa `Produs` și va avea un parametru în plus numit `culoare` și `produs_conectat` 
parametrul `produs_conectat` va avea valoarea "nimic" la crearea unui produs astfel încât nu va fi necesar de menționat la crearea unui obiect nou
De asemenea va avea o metodă numită `combine_products` care va primi un parametru `product` ce va reprezenta un alt obiect de tip `AppleProduct` care va fi salvat în parametrul `produs_conectat`
Există o singură condiție, produsul conectat trebuie să fie de tip `AppleProduct` iar culoarea acestuia trebuie să fie aceeași cu a produsului curent.

Exemplu utilizare:
iphone = AppleProduct("Iphone", 15000, 2020, "negru")
airpods = AppleProduct("Airpods", 1000, 2021, "alb")
iphone.combine_products(airpods) # În acest caz se va returna textul "Produsul nu poate fi conectat deoarece culorile nu coincid"

iphone = AppleProduct("Iphone", 15000, 2020, "negru")
airpods = AppleProduct("Airpods", 1000, 2021, "negru")
iphone.combine_products(airpods) # În acest caz se va returna textul "Produsul a fost conectat cu succes" și dacă se va printa iphone.produs_conectat se va returna obiectul airpods
print(iphone.produs_conectat.numele) # Va returna numele produsului conectat
"""

# CODUL TĂU VINE MAI JOS:
class AppleProduct( ):
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(AppleProduct, Produs))
# VERIFICATION PROCESS

"""
4. DARWIN și-a mai adus aminte de o chestie, și-au dat seama că cei de la Google tot au nevoie de posibilitatea de a conecta produsele între ele.

Avem nevoie de o clasă nouă care să se numească `GoogleProduct` care va moșteni clasa `AppleProduct` posibilitățile la ambele sunt aceleași, dar va fi nevoie de o singură schimbare.
Produsul conectat trebuie să fie de tip `GoogleProduct` iar culoarea acestuia poate să fie diferită de a produsului curent.
Asta ar însemna că singurul element care va necesita modificări este metoda `combine_products` care va trebui să accepte orice tip de obiect de tip `GoogleProduct`

Exemplu utilizare:
pixel = GoogleProduct("Pixel", 10000, 2020, "negru")
home = GoogleProduct("Home", 500, 2021, "alb")
pixel.combine_products(home) # În acest caz se va returna textul "Produsul a fost conectat cu succes" și dacă se va printa pixel.produs_conectat se va returna obiectul home
print(pixel.produs_conectat.numele) # Va returna numele produsului conectat

"""

# CODUL TĂU VINE MAI JOS:
class GoogleProduct( ):
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_6(GoogleProduct, AppleProduct))
# VERIFICATION PROCESS

"""
5. Cei de la DARWIN chiar sunt uituci, și-au adus aminte peste 5 zile că vor avea nevoie și de o modalitate prin care să vândă produsele.

Avem nevoie de o clasă nouă pentru aceasta, ea se va numi `Magazin` și va conține doar 2 metode, `vinde_produs` și `returneaza_produs`

Metoda `vinde_produs` va primi un parametru `produs` care va reprezenta un obiect de tip `Produs` și va returna textul "Produsul *numele produsului* a fost vândut cu succes"
Metoda `returneaza_produs` va primi un parametru `produs` care va reprezenta un obiect de tip `Produs` și va returna textul "Produsul *numele produsului* a fost returnat cu succes"

Exemplu utilizare:
iphone = AppleProduct("Iphone", 15000, 2020, "negru")
print(magazin.vinde_produs(iphone)) # Va returna textul "Produsul Iphone a fost vândut cu succes"
print(magazin.returneaza_produs(iphone)) # Va returna textul "Produsul Iphone a fost returnat cu succes"
"""

# CODUL TĂU VINE MAI JOS:
class Magazin:
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_7(Magazin, Produs))
print(session.get_completion_percentage())
# VERIFICATION PROCESS