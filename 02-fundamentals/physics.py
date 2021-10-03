'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9,807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1,62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu
WATER_DENSITY = 997 #? hustota vody
''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def freeFallSpeedEarth():
    """
    Funkce která vypočítá volného pádu na Zemi podle času pádu.
    """
    i = float(''.join(map(str, EARTH_GRAVITY)))
    time = int(input("Zadejte čas v sekundách:"))
    speed = time * i
    print(float(speed), "m/s")


def freeFallSpeedMoon():
    """
    Funkce která vypočítá volného pádu na Měsíci podle času pádu.
    """
    i = float(''.join(map(str, MOON_GRAVITY)))
    time = int(input("Zadejte čas v sekundách:"))
    speed = time * i
    print(float(speed), "m/s")


def Echo():
    """
    Funkce která vypočítá vzdálenost předmětupomocí
    """
    time = int(input("Zadejte dobu za kterou se vrátila ozvěna(v sekundách):"))
    i = SPEED_OF_SOUND
    s = i * time
    print(s,"m")



def Volume():
    """
    Funkce která vypočítá objem předmětu pomocí hmotnosti(s hustotou vody)
    """
    p = WATER_DENSITY
    m = int(input("Zadejte hmotnost předmětu v kg:"))
    V = m/p
    print(V,"m\u00b3")