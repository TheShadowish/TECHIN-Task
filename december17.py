"""
Santa's Magic Juice Bottling Challenge Solution

Užduotis: Apskaičiuoti, kiek talpyklų reikia kiekvienam elfui, kad supiltų
magišką šventinį sultis.

Talpyklos:
- 5 litrų šventiniai statiniai
- 2 litrų elfų ąsočiai
- 1 litro elnių buteliai

Taisyklė:
1. Pildome kuo daugiau 5L statinių
2. Tada pildome 2L ąsočius
3. Likusį sultis pilame į 1L butelius

Sprendimas:
- Naudojame sveikųjų skaičių dalybą ir liekaną
- Pirmiausia skaičiuojame 5L statinius
- Tada iš likusio skaičiuojame 2L ąsočius
- Galiausiai likusį skaičių pilame į 1L butelius
"""

from typing import List, Union, Dict, Tuple


def calculate_containers(liters):
    """
    Apskaičiuoja, kiek talpyklų reikia nurodytam sulties kiekiui.
    
    Algoritmas:
    1. Skaičiuojame 5L statinius: liters // 5
    2. Skaičiuojame likusį kiekį: liters % 5
    3. Skaičiuojame 2L ąsočius: remainder // 2
    4. Skaičiuojame likusį kiekį: remainder % 2
    5. Likęs kiekis = 1L butelių skaičius
    
    Args:
        liters (float/int): Sulties kiekis litrais
    
    Returns:
        tuple: (five_liter, two_liter, one_liter)
            - five_liter: 5L statinių skaičius
            - two_liter: 2L ąsočių skaičius
            - one_liter: 1L butelių skaičius
    
    Raises:
        ValueError: Jei sulties kiekis neigiamas arba netinkamas
    """
    # Validacija
    try:
        liters = float(liters)
    except (TypeError, ValueError):
        raise ValueError(f"Sulties kiekis turi būti skaičius, gauta: {type(liters)}")
    
    if liters < 0:
        raise ValueError(f"Sulties kiekis negali būti neigiamas, gauta: {liters}")
    
    # Konvertuojame į sveikąjį skaičių (negalime naudoti dalinių talpyklų)
    liters = int(liters)
    
    # Skaičiuojame 5L statinius
    five_liter = liters // 5
    
    # Skaičiuojame likusį kiekį po 5L statinių
    remainder = liters % 5
    
    # Skaičiuojame 2L ąsočius
    two_liter = remainder // 2
    
    # Skaičiuojame likusį kiekį po 2L ąsočių (tai bus 1L butelių skaičius)
    one_liter = remainder % 2
    
    return five_liter, two_liter, one_liter


def validate_juice_data(data):
    """
    Validuoja sulties duomenis.
    
    Palaiko du formatus:
    1. Sąrašas skaičių: [45, 92, 33]
    2. Sąrašas objektų: [{"name": "Sparkle", "liters": 45}, ...]
    
    Args:
        data: Sulties duomenys
    
    Returns:
        list: Sulties kiekiai litrais
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    if not isinstance(data, (list, tuple)):
        raise ValueError(f"Duomenys turi būti sąrašas (list) arba tuple, gauta: {type(data)}")
    
    if len(data) == 0:
        raise ValueError("Duomenų sąrašas negali būti tuščias")
    
    juice_amounts = []
    
    for i, item in enumerate(data):
        if isinstance(item, (int, float)):
            # Formatas 1: tiesiog skaičiai
            juice_amounts.append(float(item))
        elif isinstance(item, dict):
            # Formatas 2: objektai su 'liters' arba 'juice' lauku
            if 'liters' in item:
                juice_amounts.append(float(item['liters']))
            elif 'juice' in item:
                juice_amounts.append(float(item['juice']))
            else:
                raise ValueError(f"Elementas {i+1}: objektas turi turėti 'liters' arba 'juice' lauką")
        else:
            raise ValueError(f"Elementas {i+1}: netinkamas tipas {type(item)}")
    
    return juice_amounts


def bottle_juice(juice_data):
    """
    Apskaičiuoja talpyklų skaičių kiekvienam elfui.
    
    Args:
        juice_data: Sulties duomenys (sąrašas skaičių arba objektų)
    
    Returns:
        list: Talpyklų skaičių sąrašas [(five_liter, two_liter, one_liter), ...]
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    # Validuojame ir konvertuojame duomenis
    juice_amounts = validate_juice_data(juice_data)
    
    results = []
    
    for liters in juice_amounts:
        containers = calculate_containers(liters)
        results.append(containers)
    
    return results


def format_output(results):
    """
    Formatuoja išvestį pagal užduoties reikalavimus.
    
    Formatas: viena eilutė kiekvienam elfui
    "fiveLiter twoLiter oneLiter"
    
    Args:
        results (list): Talpyklų skaičių sąrašas
    
    Returns:
        str: Suformatuota išvestis
    """
    lines = []
    for five_liter, two_liter, one_liter in results:
        lines.append(f"{five_liter} {two_liter} {one_liter}")
    
    return "\n".join(lines)


def display_results(juice_data, results, detailed=False):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        juice_data: Pradiniai sulties duomenys
        results (list): Talpyklų skaičių sąrašas
        detailed (bool): Ar rodyti detalią informaciją
    """
    print("\n" + "=" * 60)
    print("🍎 SANTA'S MAGIC JUICE BOTTLING RESULTS")
    print("=" * 60)
    
    # Konvertuojame į kiekius, jei reikia
    juice_amounts = validate_juice_data(juice_data)
    
    if detailed:
        print("\n📋 Detali informacija:")
        for i, (liters, (five_liter, two_liter, one_liter)) in enumerate(zip(juice_amounts, results), 1):
            total_containers = five_liter + two_liter + one_liter
            total_capacity = five_liter * 5 + two_liter * 2 + one_liter * 1
            
            print(f"\nElfas {i}:")
            print(f"  Sulties kiekis: {liters} litrų")
            print(f"  5L statiniai: {five_liter}")
            print(f"  2L ąsočiai: {two_liter}")
            print(f"  1L buteliai: {one_liter}")
            print(f"  Iš viso talpyklų: {total_containers}")
            print(f"  Talpyklų talpa: {total_capacity} litrų")
            
            if total_capacity != liters:
                print(f"  ⚠️  Pastaba: Talpyklų talpa ({total_capacity}) nesutampa su sulties kiekiu ({liters})")
    
    print("\n" + "=" * 60)
    print("📋 IŠVESTIS (pagal užduoties formatą):")
    print("=" * 60)
    print(format_output(results))
    print("=" * 60)
    
    print("\n💡 Paaiškinimas:")
    print("   Kiekviena eilutė rodo: [5L statiniai] [2L ąsočiai] [1L buteliai]")
    print("   Algoritmas:")
    print("   1. Pildome kuo daugiau 5L statinių")
    print("   2. Tada pildome 2L ąsočius")
    print("   3. Likusį sultis pilame į 1L butelius")


def get_juice_input():
    """
    Gauna sulties duomenis iš vartotojo.
    
    Returns:
        list: Sulties duomenys
    """
    print("\n🍎 Įveskite sulties kiekius:")
    print("   Formatas 1: '45 92 33' (atskirti tarpais)")
    print("   Formatas 2: '45,92,33' (atskirti kableliais)")
    print("   Arba įveskite 'default', kad naudotumėte pavyzdinius duomenis")
    
    user_input = input("Sulties kiekiai: ").strip()
    
    if user_input.lower() == 'default':
        return [45, 92, 33]
    
    # Skirstome pagal tarpus arba kablelius
    if ',' in user_input:
        parts = [p.strip() for p in user_input.split(',')]
    else:
        parts = user_input.split()
    
    if not parts:
        raise ValueError("Nepavyko nuskaityti sulties kiekių.")
    
    try:
        juice_data = [float(x) for x in parts]
    except ValueError as e:
        raise ValueError(f"Nepavyko konvertuoti į skaičius: {e}")
    
    return juice_data


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas - užduoties pavyzdys",
            "input": [45, 92, 33],
            "expected": [(9, 0, 0), (18, 1, 0), (6, 1, 1)],
            "description": "Standartinis užduoties pavyzdys"
        },
        {
            "name": "Vienas elfas",
            "input": [10],
            "expected": [(2, 0, 0)],
            "description": "Tik vienas elfas"
        },
        {
            "name": "Tiksliai 5L kartotiniai",
            "input": [5, 10, 15],
            "expected": [(1, 0, 0), (2, 0, 0), (3, 0, 0)],
            "description": "Sulties kiekiai, kurie tiksliai dalijasi iš 5"
        },
        {
            "name": "Nelyginis kiekis",
            "input": [1, 3, 7],
            "expected": [(0, 0, 1), (0, 1, 1), (1, 1, 0)],
            "description": "Nelyginiai sulties kiekiai"
        },
        {
            "name": "Tik 1L buteliai",
            "input": [1, 2],
            "expected": [(0, 0, 1), (0, 1, 0)],
            "description": "Maži kiekiai, kurie netelpa į didesnes talpyklas"
        },
        {
            "name": "Daug sulties",
            "input": [100, 250],
            "expected": [(20, 0, 0), (50, 0, 0)],
            "description": "Dideli sulties kiekiai"
        },
        {
            "name": "Objektų formatas",
            "input": [
                {"name": "Sparkle", "liters": 45},
                {"name": "Twinkle", "liters": 92},
                {"name": "Jingle", "liters": 33}
            ],
            "expected": [(9, 0, 0), (18, 1, 0), (6, 1, 1)],
            "description": "Duomenys objektų formate"
        },
        {
            "name": "Mišrūs kiekiai",
            "input": [13, 27, 41],
            "expected": [(2, 1, 1), (5, 1, 0), (8, 0, 1)],
            "description": "Įvairūs sulties kiekiai"
        },
        {
            "name": "Nulis litrų",
            "input": [0],
            "expected": [(0, 0, 0)],
            "description": "Nulis litrų sulties"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    
    for test in test_cases:
        try:
            juice_data = test["input"]
            results = bottle_juice(juice_data)
            expected = test["expected"]
            
            passed = results == expected
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            print(f"      Įvestis: {juice_data}")
            print(f"      Gauta: {results}")
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
    print("🍎 SANTA'S MAGIC JUICE BOTTLING CHALLENGE")
    print("=" * 60)
    print("\nŠi programa apskaičiuoja, kiek talpyklų reikia kiekvienam")
    print("elfui, kad supiltų magišką šventinį sultis.")
    print("\nTalpyklos:")
    print("  • 5L šventiniai statiniai")
    print("  • 2L elfų ąsočiai")
    print("  • 1L elnių buteliai")
    print("\nTaisyklė:")
    print("  1. Pildome kuo daugiau 5L statinių")
    print("  2. Tada pildome 2L ąsočius")
    print("  3. Likusį sultis pilame į 1L butelius\n")
    
    try:
        # Gauname sulties duomenis
        juice_data = get_juice_input()
        
        if not juice_data:
            print("❌ Klaida: Nepavyko nuskaityti sulties duomenų.")
            return False
        
        # Apskaičiuojame talpyklų skaičių
        results = bottle_juice(juice_data)
        
        # Atvaizduojame rezultatus
        display_results(juice_data, results, detailed=True)
        
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