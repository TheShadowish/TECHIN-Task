"""
Santa's Gift Audit Solution

Užduotis: Suskaičiuoti dovanas iš visų dirbtuvių naudojant įdėtus ciklus.

Struktūra:
- W dirbtuvių
- Kiekvienoje dirbtuvėje E elfų
- Kiekvienas elfas pagamino G dovanų (skaičius skiriasi)

Duomenys: 2D struktūra (masyvas masyvų)
- Kiekviena eilutė = dirbtuvė
- Kiekvienas stulpelis = elfas
- Skaičius = kiek dovanų pagamino tas elfas

Sprendimas:
1. Išorinis ciklas: eina per dirbtuves
2. Vidinį ciklas: eina per elfus kiekvienoje dirbtuvėje
3. Sumuojame dovanas kiekvienai dirbtuvei
4. Sumuojame visas dovanas iš visų dirbtuvių
"""

from typing import List, List


def validate_workshops(workshops):
    """
    Validuoja dirbtuvių duomenis.
    
    Args:
        workshops: Dirbtuvių duomenys (2D masyvas)
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    if not isinstance(workshops, (list, tuple)):
        raise ValueError(f"Dirbtuvių duomenys turi būti sąrašas (list) arba tuple, gauta: {type(workshops)}")
    
    if len(workshops) == 0:
        raise ValueError("Dirbtuvių sąrašas negali būti tuščias")
    
    for i, workshop in enumerate(workshops):
        if not isinstance(workshop, (list, tuple)):
            raise ValueError(f"Dirbtuvė {i+1} turi būti sąrašas, gauta: {type(workshop)}")
        
        if len(workshop) == 0:
            raise ValueError(f"Dirbtuvė {i+1} negali būti tuščia (turi būti bent vienas elfas)")
        
        for j, gifts in enumerate(workshop):
            try:
                gifts = int(gifts)
                if gifts < 0:
                    raise ValueError(f"Dirbtuvė {i+1}, elfas {j+1}: dovanų skaičius negali būti neigiamas, gauta: {gifts}")
            except (TypeError, ValueError) as e:
                if isinstance(e, ValueError) and "neigiamas" in str(e):
                    raise
                raise ValueError(f"Dirbtuvė {i+1}, elfas {j+1}: dovanų skaičius turi būti sveikasis skaičius, gauta: {type(gifts)}")


def calculate_workshop_gifts(workshop):
    """
    Apskaičiuoja dovanų skaičių vienoje dirbtuvėje.
    
    Args:
        workshop (list): Dirbtuvės duomenys (elfų dovanų sąrašas)
    
    Returns:
        int: Bendras dovanų skaičius dirbtuvėje
    """
    total = 0
    for gifts in workshop:
        total += int(gifts)
    return total


def audit_gifts(workshops):
    """
    Atlieka dovanų auditą visoms dirbtuvėms naudojant įdėtus ciklus.
    
    Algoritmas:
    1. Išorinis ciklas: eina per kiekvieną dirbtuvę
    2. Vidinį ciklas: eina per kiekvieną elfą dirbtuvėje
    3. Sumuojame dovanas kiekvienai dirbtuvei
    4. Sumuojame visas dovanas
    
    Args:
        workshops (list): 2D masyvas, kur kiekviena eilutė yra dirbtuvė
    
    Returns:
        tuple: (workshop_totals, grand_total)
            - workshop_totals: sąrašas dovanų skaičių kiekvienai dirbtuvei
            - grand_total: bendras dovanų skaičius visose dirbtuvėse
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    # Validuojame duomenis
    validate_workshops(workshops)
    
    workshop_totals = []
    grand_total = 0
    
    # Išorinis ciklas: eina per kiekvieną dirbtuvę
    for workshop_index in range(len(workshops)):
        workshop = workshops[workshop_index]
        workshop_total = 0
        
        # Vidinį ciklas: eina per kiekvieną elfą dirbtuvėje
        for elf_index in range(len(workshop)):
            gifts = int(workshop[elf_index])
            workshop_total += gifts
        
        workshop_totals.append(workshop_total)
        grand_total += workshop_total
    
    return workshop_totals, grand_total


def format_output(workshop_totals, grand_total):
    """
    Formatuoja išvestį pagal užduoties reikalavimus.
    
    Args:
        workshop_totals (list): Dovanų skaičiai kiekvienai dirbtuvei
        grand_total (int): Bendras dovanų skaičius
    
    Returns:
        str: Suformatuota išvestis
    """
    lines = []
    for i, total in enumerate(workshop_totals, 1):
        lines.append(f"Workshop {i} made {total} gifts")
    
    lines.append(f"Santa's total gift count is {grand_total}")
    
    return "\n".join(lines)


def display_results(workshops, workshop_totals, grand_total, detailed=False):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        workshops (list): Dirbtuvių duomenys
        workshop_totals (list): Dovanų skaičiai kiekvienai dirbtuvei
        grand_total (int): Bendras dovanų skaičius
        detailed (bool): Ar rodyti detalią informaciją
    """
    print("\n" + "=" * 60)
    print("📊 DOVANŲ AUDITO REZULTATAI")
    print("=" * 60)
    
    if detailed:
        print("\n📋 Detali informacija:")
        for i, (workshop, total) in enumerate(zip(workshops, workshop_totals), 1):
            print(f"\nDirbtuvė {i}:")
            print(f"  Elfų skaičius: {len(workshop)}")
            print(f"  Dovanų skaičiai: {workshop}")
            print(f"  Bendras dovanų skaičius: {total}")
    
    print("\n" + "=" * 60)
    print("📋 IŠVESTIS (pagal užduoties formatą):")
    print("=" * 60)
    print(format_output(workshop_totals, grand_total))
    print("=" * 60)
    
    print("\n💡 Paaiškinimas:")
    print("   Programa naudoja įdėtus ciklus:")
    print("   - Išorinis ciklas: eina per kiekvieną dirbtuvę")
    print("   - Vidinį ciklas: eina per kiekvieną elfą dirbtuvėje")
    print("   - Sumuojamos visos dovanos")


def get_workshops_input():
    """
    Gauna dirbtuvių duomenis iš vartotojo.
    
    Returns:
        list: Dirbtuvių duomenys (2D masyvas)
    """
    print("\n📝 Įveskite dirbtuvių duomenis:")
    print("   Formatas: kiekviena dirbtuvė atskiroje eilutėje")
    print("   Elfų dovanų skaičiai atskirti tarpais arba kableliais")
    print("   Pavyzdys:")
    print("     5 7 3")
    print("     6 4 4 5")
    print("     10 2")
    print("   Arba įveskite 'default', kad naudotumėte pavyzdinius duomenis")
    
    user_input = input("Dirbtuvės (tuščia eilutė baigia įvedimą): ").strip()
    
    if user_input.lower() == 'default':
        return [
            [5, 7, 3],
            [6, 4, 4, 5],
            [10, 2]
        ]
    
    workshops = []
    
    if user_input:
        # Jei vartotojas įvedė pirmą eilutę
        while user_input:
            # Skirstome pagal tarpus arba kablelius
            if ',' in user_input:
                parts = [p.strip() for p in user_input.split(',')]
            else:
                parts = user_input.split()
            
            try:
                workshop = [int(x) for x in parts if x]
                if workshop:
                    workshops.append(workshop)
            except ValueError as e:
                raise ValueError(f"Nepavyko konvertuoti į skaičius: {e}")
            
            user_input = input("Kita dirbtuvė (tuščia eilutė baigia): ").strip()
    
    if not workshops:
        raise ValueError("Nepavyko nuskaityti dirbtuvių duomenų.")
    
    return workshops


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas - užduoties pavyzdys",
            "workshops": [
                [5, 7, 3],
                [6, 4, 4, 5],
                [10, 2]
            ],
            "expected_totals": [15, 19, 12],
            "expected_grand": 46,
            "description": "Standartinis užduoties pavyzdys"
        },
        {
            "name": "Viena dirbtuvė",
            "workshops": [
                [10, 20, 30]
            ],
            "expected_totals": [60],
            "expected_grand": 60,
            "description": "Tik viena dirbtuvė"
        },
        {
            "name": "Vienas elfas kiekvienoje dirbtuvėje",
            "workshops": [
                [5],
                [10],
                [15]
            ],
            "expected_totals": [5, 10, 15],
            "expected_grand": 30,
            "description": "Kiekvienoje dirbtuvėje po vieną elfą"
        },
        {
            "name": "Daug dirbtuvių",
            "workshops": [
                [1, 2, 3],
                [4, 5],
                [6, 7, 8],
                [9, 10, 11, 12]
            ],
            "expected_totals": [6, 9, 21, 42],
            "expected_grand": 78,
            "description": "Keturių dirbtuvių testas"
        },
        {
            "name": "Nulinės dovanos",
            "workshops": [
                [0, 5, 0],
                [10, 0]
            ],
            "expected_totals": [5, 10],
            "expected_grand": 15,
            "description": "Kai kai kurie elfai pagamino 0 dovanų"
        },
        {
            "name": "Didelės reikšmės",
            "workshops": [
                [100, 200, 300],
                [400, 500]
            ],
            "expected_totals": [600, 900],
            "expected_grand": 1500,
            "description": "Didelės dovanų reikšmės"
        },
        {
            "name": "Skirtingas elfų skaičius",
            "workshops": [
                [1],
                [2, 3],
                [4, 5, 6],
                [7, 8, 9, 10]
            ],
            "expected_totals": [1, 5, 15, 34],
            "expected_grand": 55,
            "description": "Kiekvienoje dirbtuvėje skirtingas elfų skaičius"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    
    for test in test_cases:
        try:
            workshops = test["workshops"]
            workshop_totals, grand_total = audit_gifts(workshops)
            
            expected_totals = test["expected_totals"]
            expected_grand = test["expected_grand"]
            
            passed = (
                workshop_totals == expected_totals and
                grand_total == expected_grand
            )
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            print(f"      Dirbtuvių skaičius: {len(workshops)}")
            print(f"      Dovanų skaičiai: {workshop_totals} (tikėtasi: {expected_totals})")
            print(f"      Bendras skaičius: {grand_total} (tikėtasi: {expected_grand})")
            
            if not passed:
                if workshop_totals != expected_totals:
                    print(f"      ❌ Neteisingi dirbtuvių dovanų skaičiai!")
                if grand_total != expected_grand:
                    print(f"      ❌ Neteisingas bendras dovanų skaičius!")
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
    print("🎅 SANTA'S GIFT AUDIT")
    print("=" * 60)
    print("\nŠi programa suskaičiuoja dovanas iš visų dirbtuvių")
    print("naudojant įdėtus ciklus:")
    print("  • Išorinis ciklas: eina per kiekvieną dirbtuvę")
    print("  • Vidinį ciklas: eina per kiekvieną elfą dirbtuvėje\n")
    
    try:
        # Gauname dirbtuvių duomenis
        workshops = get_workshops_input()
        
        if not workshops:
            print("❌ Klaida: Nepavyko nuskaityti dirbtuvių duomenų.")
            return False
        
        # Atliekame auditą
        workshop_totals, grand_total = audit_gifts(workshops)
        
        # Atvaizduojame rezultatus
        display_results(workshops, workshop_totals, grand_total, detailed=True)
        
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

