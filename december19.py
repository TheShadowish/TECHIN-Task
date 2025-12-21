"""
Santa's Toy Collection - Trading Duplicates Solution

Užduotis: Rasti, kurias dovanų numerius Binky Frostynose gali iškeisti,
nes jis turi dublikatų.

Santa turi 100 skirtingų Kalėdų dovanų, sunumeruotų nuo 1 iki 100.
Binky Frostynose turi savo dovanų dėžę, kurioje kai kurie numeriai
gali pasikartoti - tai dublikatai.

Užduotis:
1. Nuskaityti, kiek dovanų turi Binky Frostynose
2. Nuskaityti visus dovanų numerius
3. Rasti visus numerius, kurie pasirodo daugiau nei vieną kartą
4. Išvesti šiuos numerius didėjimo tvarka

Sprendimas:
- Naudojame žodyną, kad suskaičiuotume kiekvieno numerio pasikartojimus
- Rastus dublikatus surūšiuojame didėjimo tvarka
"""

from typing import List, Set
from collections import Counter


def validate_input(n, toys):
    """
    Validuoja įvesties duomenis.
    
    Args:
        n (int): Dovanų skaičius
        toys (list): Dovanų numerių sąrašas
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    if not isinstance(n, int):
        raise ValueError(f"Dovanų skaičius turi būti sveikasis skaičius, gauta: {type(n)}")
    
    if n < 0:
        raise ValueError(f"Dovanų skaičius negali būti neigiamas, gauta: {n}")
    
    if not isinstance(toys, (list, tuple)):
        raise ValueError(f"Dovanų numerių sąrašas turi būti list arba tuple, gauta: {type(toys)}")
    
    if len(toys) != n:
        raise ValueError(f"Dovanų skaičius ({n}) nesutampa su sąrašo ilgiu ({len(toys)})")
    
    for i, toy in enumerate(toys):
        try:
            toy_num = int(toy)
            if not (1 <= toy_num <= 100):
                raise ValueError(f"Dovana {i+1}: numeris turi būti tarp 1 ir 100, gauta: {toy_num}")
        except (TypeError, ValueError) as e:
            if isinstance(e, ValueError) and "tarp 1 ir 100" in str(e):
                raise
            raise ValueError(f"Dovana {i+1}: numeris turi būti sveikasis skaičius, gauta: {type(toy)}")


def find_duplicates(n, toys):
    """
    Randa visus dublikatus (dovanų numerius, kurie pasirodo daugiau nei vieną kartą).
    
    Algoritmas:
    1. Suskaičiuojame kiekvieno numerio pasikartojimus
    2. Filtruojame tuos, kurie pasirodo daugiau nei vieną kartą
    3. Surūšiuojame didėjimo tvarka
    
    Args:
        n (int): Dovanų skaičius
        toys (list): Dovanų numerių sąrašas
    
    Returns:
        list: Dublikatų numerių sąrašas (surūšiuotas didėjimo tvarka)
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    # Validuojame įvestį
    validate_input(n, toys)
    
    # Konvertuojame į sveikuosius skaičius
    toy_numbers = [int(toy) for toy in toys]
    
    # Suskaičiuojame kiekvieno numerio pasikartojimus
    counter = Counter(toy_numbers)
    
    # Randame dublikatus (numerius, kurie pasirodo daugiau nei vieną kartą)
    duplicates = [toy_num for toy_num, count in counter.items() if count > 1]
    
    # Surūšiuojame didėjimo tvarka
    duplicates.sort()
    
    return duplicates


def format_output(duplicates):
    """
    Formatuoja išvestį pagal užduoties reikalavimus.
    
    Formatas: visi numeriai vienoje eilutėje, atskirti tarpais
    
    Args:
        duplicates (list): Dublikatų numerių sąrašas
    
    Returns:
        str: Suformatuota išvestis
    """
    if not duplicates:
        return ""
    
    return " ".join(str(toy_num) for toy_num in duplicates)


def display_results(n, toys, duplicates, detailed=False):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        n (int): Dovanų skaičius
        toys (list): Dovanų numerių sąrašas
        duplicates (list): Dublikatų numerių sąrašas
        detailed (bool): Ar rodyti detalią informaciją
    """
    print("\n" + "=" * 60)
    print("🎁 SANTA'S TOY COLLECTION - TRADING DUPLICATES")
    print("=" * 60)
    
    if detailed:
        from collections import Counter
        counter = Counter([int(toy) for toy in toys])
        
        print(f"\n📋 Detali informacija:")
        print(f"  Binky Frostynose turi {n} dovanų")
        print(f"  Unikalių numerių: {len(counter)}")
        print(f"  Dublikatų numerių: {len(duplicates)}")
        
        print(f"\n  Dovanų pasikartojimai:")
        for toy_num in sorted(counter.keys()):
            count = counter[toy_num]
            if count > 1:
                print(f"    Numeris {toy_num}: {count} kartai {'(dublikatas)' if count > 1 else ''}")
        
        print(f"\n  Dovanų numeriai: {toys}")
    
    print("\n" + "=" * 60)
    print("📋 IŠVESTIS (pagal užduoties formatą):")
    print("=" * 60)
    
    output = format_output(duplicates)
    if output:
        print(output)
    else:
        print("(Nėra dublikatų - visi numeriai unikalūs)")
    
    print("=" * 60)
    
    print("\n💡 Paaiškinimas:")
    print("   Programa randa visus dovanų numerius, kurie pasirodo")
    print("   daugiau nei vieną kartą Binky Frostynose dėžėje.")
    print("   Šie numeriai gali būti iškeisti už trūkstamus dovanų numerius.")


def get_input():
    """
    Gauna įvesties duomenis iš vartotojo.
    
    Returns:
        tuple: (n, toys)
            - n: Dovanų skaičius
            - toys: Dovanų numerių sąrašas
    """
    print("\n🎁 Įveskite Binky Frostynose dovanų duomenis:")
    print("   Pirmoje eilutėje: dovanų skaičius")
    print("   Antroje eilutėje: dovanų numeriai (atskirti tarpais)")
    print("   Pavyzdys:")
    print("     17")
    print("     5 12 6 7 13 7 9 10 12 17 5 16 2 2 5 4 6")
    print("   Arba įveskite 'default', kad naudotumėte pavyzdinius duomenis")
    
    user_input = input("Įvestis: ").strip()
    
    if user_input.lower() == 'default':
        return 17, [5, 12, 6, 7, 13, 7, 9, 10, 12, 17, 5, 16, 2, 2, 5, 4, 6]
    
    # Nuskaitome pirmą eilutę (dovanų skaičių)
    try:
        n = int(user_input)
    except ValueError:
        raise ValueError(f"Nepavyko konvertuoti dovanų skaičiaus į sveikąjį skaičių: {user_input}")
    
    # Nuskaitome antrą eilutę (dovanų numerius)
    toys_input = input("Dovanų numeriai: ").strip()
    
    if not toys_input:
        raise ValueError("Dovanų numerių sąrašas negali būti tuščias")
    
    toys = toys_input.split()
    
    if len(toys) != n:
        raise ValueError(f"Dovanų skaičius ({n}) nesutampa su įvestų numerių skaičiumi ({len(toys)})")
    
    return n, toys


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas - užduoties pavyzdys",
            "n": 17,
            "toys": [5, 12, 6, 7, 13, 7, 9, 10, 12, 17, 5, 16, 2, 2, 5, 4, 6],
            "expected": [2, 5, 6, 7, 12],
            "description": "Standartinis užduoties pavyzdys"
        },
        {
            "name": "Visi numeriai unikalūs",
            "n": 5,
            "toys": [1, 2, 3, 4, 5],
            "expected": [],
            "description": "Jokių dublikatų"
        },
        {
            "name": "Visi numeriai vienodi",
            "n": 5,
            "toys": [10, 10, 10, 10, 10],
            "expected": [10],
            "description": "Visi numeriai vienodi"
        },
        {
            "name": "Vienas dublikatas",
            "n": 4,
            "toys": [1, 2, 3, 2],
            "expected": [2],
            "description": "Tik vienas dublikatas"
        },
        {
            "name": "Keli dublikatai",
            "n": 8,
            "toys": [1, 1, 2, 2, 3, 3, 4, 5],
            "expected": [1, 2, 3],
            "description": "Keli skirtingi dublikatai"
        },
        {
            "name": "Tris kartus pasikartojantys numeriai",
            "n": 7,
            "toys": [5, 5, 5, 10, 10, 20, 20],
            "expected": [5, 10, 20],
            "description": "Kai kurie numeriai pasirodo tris kartus"
        },
        {
            "name": "Didelės reikšmės",
            "n": 6,
            "toys": [100, 99, 100, 98, 99, 97],
            "expected": [99, 100],
            "description": "Dublikatai su didelėmis reikšmėmis"
        },
        {
            "name": "Tuščias sąrašas",
            "n": 0,
            "toys": [],
            "expected": [],
            "description": "Tuščias dovanų sąrašas"
        },
        {
            "name": "Vienas elementas",
            "n": 1,
            "toys": [50],
            "expected": [],
            "description": "Tik viena dovana"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    
    for test in test_cases:
        try:
            n = test["n"]
            toys = test["toys"]
            expected = test["expected"]
            
            duplicates = find_duplicates(n, toys)
            
            passed = duplicates == expected
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            print(f"      Įvestis: n={n}, toys={toys}")
            print(f"      Gauta: {duplicates}")
            print(f"      Tikėtasi: {expected}")
            
            if not passed:
                print(f"      ❌ Rezultatai nesutampa!")
            print()
            
        except Exception as e:
            print(f"❌ ERROR | {test['name']}")
            print(f"      Klaida: {e}")
            failed_count += 1
            print()
    
    print("=" * 70)
    print(f"📈 Rezultatai: {passed_count} sėkmingi, {failed_count} nesėkmingi iš {len(test_cases)} testų")
    
    if failed_count == 0:
        print("🎉 Visi testai praėjo sėkmingai!")
        return True
    else:
        print("⚠️  Kai kurie testai nepavyko. Patikrinkite kodą.")
        return False


def main():
    """
    Pagrindinė programa - interaktyvus režimas su vartotojo įvestimi.
    """
    print("=" * 60)
    print("🎁 SANTA'S TOY COLLECTION - TRADING DUPLICATES")
    print("=" * 60)
    print("\nBinky Frostynose turi dovanų dėžę su kai kuriomis")
    print("dublikatais. Programa randa, kurias dovanų numerius")
    print("jis gali iškeisti už trūkstamus numerius.\n")
    
    try:
        # Gauname įvesties duomenis
        n, toys = get_input()
        
        # Randame dublikatus
        duplicates = find_duplicates(n, toys)
        
        # Atvaizduojame rezultatus
        display_results(n, toys, duplicates, detailed=True)
        
    except (ValueError, KeyboardInterrupt) as e:
        if isinstance(e, KeyboardInterrupt):
            print("\n\n⚠️  Programa nutraukta vartotojo.")
        else:
            print(f"\n❌ Programa negali tęsti dėl klaidos: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Netikėta klaida: {e}")
        print("Prašome pranešti apie šią klaidą sistemos administratoriui.")
        return False
    
    return True


if __name__ == "__main__":
    import sys
    
    # Jei programa paleista su argumentu "test", vykdomi testai
    if len(sys.argv) > 1 and sys.argv[1].lower() == "test":
        success = run_tests()
        sys.exit(0 if success else 1)
    else:
        # Kitu atveju - interaktyvus režimas
        success = main()
        sys.exit(0 if success else 1)

