# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number=2
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number>0 :
    print ('numărul este pozitiv')
else :
    print('numărul este negativ')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number %2==0:
    print ('number este par')
else : 
    print ('number nu este par')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number %2!=0:
    print('number nu este par')
else :
    print ('number este par')
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = 'I not like homework!'
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
print(text)
# CODUL TĂU VINE MAI JOS:
if "python" in text :
    print ('textul conține cuvântul "Python"')
else :
    print('textul nu conține cuvântul "Python"')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "java" in text :
    print ('textul conține cuvântul "Java"')
else :
    print('textul nu conține cuvântul "Java"')
# CODUL TĂU VINE MAI SUS:


# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "python" in text:
    print('Textul conține cuvântul "Python"')
elif "java" in text:
    print('Textul conține cuvântul "Java"')
else:
    print('Textul nu conține cuvântul "Python" sau "Java"')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "python" in text and "java" in text:
    print('Textul conține atât cuvântul "Python" și cuvântul "Java"')
elif "python" in text or "java" in text:
    print('Textul conține unul dintre cuvintele "Python" sau "Java"')
else:
    print('Textul nu conține niciunul dintre cuvintele "Python" sau "Java".')

# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
number = int(input('intoduceti un numar de la 1 la 5'))
print (number)

if number==1:
    print('unu')
elif number==2:
    print('doi')
elif number==3:
    print('trei')
elif number==4:
    print('patru')
elif number==5:
    print('cinci')
else :
    print ('numar nu este dintre 1 pina la 5')

# CODUL TĂU VINE MAI SUS:


