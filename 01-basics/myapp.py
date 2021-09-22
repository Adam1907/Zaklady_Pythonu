jmeno = input("Zadejte libovolné jméno:")
pridavne_jmeno = input("Zadejte přídavné jméno (jaké):")
cislo = input("Zadejte libovolne cislo")
zvire = input("Zadejte libovolné zvíře (4. pád):")
jidlo = input("Zadejte libovolné jídlo (7. pád):")
barva = input("Zadejte barvu (jaký)")

print("Ahoj! Jmenuji se {jmeno}, bydlím se svými rodiči v domě na ulici {pridavne_jmeno}."
      "Mám {cislo} bratrů ale ani jednu sestru. Máme také domácího mazlíčka: {zvire}."
      "Našeho mazlíčka krmíme {jidlo} a proto je tak {barva}.".format(jmeno = jmeno, pridavne_jmeno = pridavne_jmeno, cislo = cislo, zvire = zvire, jidlo = jidlo, barva = barva))
