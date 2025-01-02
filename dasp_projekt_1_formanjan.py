#################### ÚVOD ####################
"""
dasp_projekt_1_formanjan.py: Datový analytik s Pythonem - Projekt 1

author: Jan Forman
email: formanjan@seznam.cz
discord: janforman
"""

import sys

#################### SUPPORTING DATA ####################

# Předpřipravené texty od Engeto pro analýzu (list = pořadí prvků 1,2,3)
TEXTS = [
    """Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet 
    above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, 
    which traverse the valley. """,

    """At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal beds slope gradually upward 
    from the valley floor and steepen abruptly. Overlying them and extending to the top of the 
    butte are the much steeper buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.""",

    """The monument contains 8198 acres and protects a portion of the largest deposit of 
    freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple 
    limestone layers, which lie some 100 feet below the Kairan Plateau. """
    ]



# Slovník registrovaných uživatelů (dict = primary key: value) 
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
    "jan": "987"
}


#################### FUNKCE PŘIHLAŠOVÁNÍ ####################

# Funkce pro přihlášení uživatele
def authenticate_user():
    # Docstringy se používají pro popis funkcí, metod nebo tříd
    # Při použití funkce help() v Pythonu bude docstring zobrazen jako nápověda
    ## Je to vidět když ve VSC najedu na funkci
    
    """
    Vyžádá od uživatele přihlašovací jméno a heslo a ověří, zda je seznamu registrovaných uživatelů.
    Pokud jsou údaje správné, uživatel je přivítán a funkce zobrazí uživateli text pro další úkoly.
    Pokud jsou údaje nesprávné, program informuje uživatele a ukončí se.
    """
    print("-" * 75)
    print(">" * 10, " LOG IN // PŘIHLÁSIT SE ", "<" * 10)
    # Metoda strip() odstraní nadbytečné mezery na začátku a konci zadaného textu. --> omezení lidského faktoru.
    ## Je to jako trim v SQL, nebo v Excelu, když čistím řetězce kvůli zkoumání délky apod.
    username = input("username: ").strip() # Vyzve uživatele k zadání jména
    password = input("password: ").strip() # Vyzve uživatele k zadání hesla

    if registered_users.get(username) == password: #Vložená hodnota se chová jako primární klíč, který hledá ve slovníku
        print("-" * 75)
        print(">" * 10, " WELCOME TO THE APP! // VÍTEJ V APLIKACI! ", "<" * 10)
        print(f"Hi {username}, we have 3 texts to be analyzed. // Ahoj {username}, máme 3 texty k analýze.") #F-string, abych mohl kombinovat text a proměnné
        return True # Print nemůžu dát za return, protože po něm okamžitě končí run
    else:
        print("-" * 75)
        print(">" * 10, " OOPS, ERROR // UPS, CHYBA ", "<" * 10)
        print("It seems you are unregistred user. Terminating the program. // "
              "\nZdá se, že nejsi registrovaným uživatelem. Ukončuji program.") # \n za tímto znakem je text na novém řádku.
        return exit() # Kdybych tu neměl exit(), tak by jel program dál, bez ohledu na to, že je uživatel neregistrovaný

#authenticate_user() # >>>>>>>>>> TESTOVÁNÍ funkce <<<<<<<<<<



#################### FUNKCE PRÁCE S TEXTEM ####################

# Funkce pro výběr textu
def select_text():
    """
    Nechá uživatele vybrat text k analýze zadáním čísla (1, 2, nebo 3).
    Pokud je vstup neplatný (číslo mimo uvedené nebo se nejedná o číslo), program se ukončí.
    Vrátí vybraný text.
    """

    try:
        # Celé číslo bez mezer
        text_choice = int(input("Enter a number (1-3) // Zadej číslo (1-3): ").strip())
        # Když je větší nebo rovno a menší nebo rovno, tak vrátí text
        if 1 <= text_choice <= 3:
            return TEXTS[text_choice - 1] # Seznamy se počítají od nuly, proto musím dát -1
        else:
            print("-" * 75)
            print(">" * 10, " OOPS, ERROR // UPS, CHYBA ", ">" * 10)
            print("Invalid choice, terminating the program. // Neplatná volba, ukončuji program.")
            sys.exit() # Protože tu ukončuji program, tak tu nemusím mít return

    except ValueError:
        print("-" * 75)
        print(">" * 10, " OOPS, ERROR // UPS, CHYBA ", ">" * 10)
        print("Invalid input, terminating the program. // Neplatný vstup, ukončuji program.")
        sys.exit()     
#select_text() # >>>>>>>>>> TESTOVÁNÍ funkce <<<<<<<<<<

# Funkce pro analýzu textu
## Text je argument a Python pozná podle dalších kroků, že jde o string, proto jej nemusím definovat
def analyze_text(text):
    """
    Analyzuje zadaný text a statistiky.
    Dále vygeneruje jednoduchý sloupcový graf zobrazující četnost délek slov.
    """

    import string  # Importuje modul string pro práci s interpunkcí - to využiji níže, při zkoumání délky slov

    # Rozdělení textu na slova
    ## Split rozdělí text podle mezer a vrátí mi seznam (list)
    ## Více mezer mezi slovy vyřeší automaticky (odstraní nadbytečné mezery)
    words = text.split()

    # ********** Výpočet základních statistik **********

    # Celkový počet slov
    num_words = len(words)  # Když funkci len aplikuji na seznam, vrátí mi počet položek

    # Jak to, že mi funguje word bez definování?
    ## Jde o iterátor vytvořený v rámci cyklu for.
    ## V Pythonu platí, že proměnné vytvořené ve smyčkách (např. for, while),
    ### nebo v comprehensions (generátory seznamů, slovníků apod.) nemusí být předem definované.

    # Do každé proměnné se uloží součet jedniček. Každé slovo, které splní danou podmínku dostane přiřazenou jedničku.
    # Je to podobné jako vzorce v Excelu funkce Power Query M
    titlecase_words = sum(1 for word in words if word.istitle())  # Slova začínající velkým písmenem
    uppercase_words = sum(1 for word in words if word.isupper() and word.isalpha())  # Velká písmena
    lowercase_words = sum(1 for word in words if word.islower())  # Malá písmena
    numeric_strings = sum(1 for word in words if word.isdigit())  # Číselné řetězce

    # Pokud je word převedené na celé číslo = true, tak sečte takové hodnoty
    numeric_sum = sum(int(word) for word in words if word.isdigit())  # Součet čísel

    # Výpis základních statistik
    print("-" * 40)
    print("Statistics available only in english.", "Statistika dostupná pouze v angličtině.")
    print("-" * 5)
    print(f"There are {num_words} words in the selected text.")
    print(f"There are {titlecase_words} titlecase words.")
    print(f"There are {uppercase_words} uppercase words.")
    print(f"There are {lowercase_words} lowercase words.")
    print(f"There are {numeric_strings} numeric strings.")
    print(f"The sum of all the numbers is {numeric_sum}.")


    # Vytvoření slovníku pro četnosti délek slov
    # Slovník bude v tomto případě používat délku slova jako klíč a počet výskytů této délky jako hodnotu.
    word_lengths = {}
    for word in words:
        # string = modul = standardní knihovna, která poskytuje užitečné konstanty a funkce pro práci s textem.
        length = len(word.strip(string.punctuation))

        word_lengths[length] = word_lengths.get(length, 0) + 1


    # Zjištění maximálních šířek. Pracuje se se slovník word_lengths
    max_len_length_x = max(len(str(length)) for length in word_lengths)  # Nejdelší délka čísla v prvním sloupci (LEN)
    ## Najde hodnotu četnosti a vynásobí tím hvězdičky, abychom zjistili, jak bude dlouhý ten řetězec
    ### Šlo by asi jednodušeji, protože ta četnost je ta délka = ok
    max_len_occurrence_x = max(len('*' * count) for count in word_lengths.values())  # Nejdelší řetězec hvězdiček
    max_len_count_x = max(len(str(count)) for count in word_lengths.values())  # Nejdelší číslo v posledním sloupci (NR.)

    # Zjištění maximálních šířek pro záhlaví
    ## Max s dvěma argumenty zvolí ten největší
    max_len_length = max(max_len_length_x, len("LEN"))  # Porovnání s délkou záhlaví
    max_len_occurrence = max(max_len_occurrence_x, len("OCCURENCES"))  # Porovnání s délkou záhlaví
    max_len_count = max(max_len_count_x, len("NR."))  # Porovnání s délkou záhlaví

    # Generování sloupcového grafu s dynamickou šířkou + rezerva
    print("-" * (max_len_length + max_len_occurrence + max_len_count + 10))
    ## Dvojtečka odděluje text od formátovacích instrukcí
    ## < zarovnání vlevo a > zarovnání vpravo a ^ zarovnání na střed, za nimi dám číslo (umístění)
    print(f"{'LEN':<{max_len_length}} | {'OCCURENCES':<{max_len_occurrence}} | {'NR.':<{max_len_count}}")
    print("-" * (max_len_length + max_len_occurrence + max_len_count + 10))

    # Výpis dat s dynamickou šířkou a zarovnáním doprava pro sloupce LEN a NR.
    # Vezme slovník a jeho páry, seřadí to podle primary key. Určíme že length je primary key a count je value.
    for length, count in sorted(word_lengths.items()):
        # Zobrazí primary klíč zarovnaný doprava a oddělí svislou čárou
        # Zobrazí počet hvězdiček dle četnosti a zarovná doleva a oddělí svislou čárou
        # Zobrazí hodnoty ze slovníku a zarovná doprava
        print(f"{length:>{max_len_length}} | {'*' * count:<{max_len_occurrence}} | {count:>{max_len_count}}")



#################### HLAVNÍ PROGRAM ####################

# Tohle všechno spustí = Město strojů
if authenticate_user():
    selected_text = select_text()
    analyze_text(selected_text)
else:
    sys.exit()
