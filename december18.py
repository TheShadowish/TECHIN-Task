"""
Santa's Shopping Trip Solution

Užduotis: Apskaičiuoti, kiek pinigų Santa išleido kiekvienoje parduotuvėje
ir iš viso visose parduotuvėse.

Duomenys:
- n skirtingų parduotuvių
- Kiekvienoje parduotuvėje Santa nusipirko m magiškų prekių
- Kiekvienai prekei nurodyta kaina

Užduotis:
- Kiekvienai parduotuvei: parduotuvės numeris, prekių skaičius, išleista suma
- Iš viso: bendra suma visose parduotuvėse

Sprendimas:
1. Eina per kiekvieną parduotuvę
2. Skaičiuoja prekių skaičių ir sumą kiekvienoje parduotuvėje
3. Sumuojame visas sumas iš visų parduotuvių
4. Suapvaliname iki dviejų skaitmenų po kablelio
"""

from typing import List, Tuple


def validate_stores_data(stores):
    """
    Validuoja parduotuvių duomenis.
    
    Args:
        stores: Parduotuvių duomenys (2D masyvas)
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    if not isinstance(stores, (list, tuple)):
        raise ValueError(f"Parduotuvių duomenys turi būti sąrašas (list) arba tuple, gauta: {type(stores)}")
    
    if len(stores) == 0:
        raise ValueError("Parduotuvių sąrašas negali būti tuščias")
    
    for i, store in enumerate(stores):
        if not isinstance(store, (list, tuple)):
            raise ValueError(f"Parduotuvė {i+1} turi būti sąrašas, gauta: {type(store)}")
        
        if len(store) == 0:
            raise ValueError(f"Parduotuvė {i+1} negali būti tuščia (turi būti bent viena prekė)")
        
        for j, price in enumerate(store):
            try:
                price = float(price)
                if price < 0:
                    raise ValueError(f"Parduotuvė {i+1}, prekė {j+1}: kaina negali būti neigiama, gauta: {price}")
            except (TypeError, ValueError) as e:
                if isinstance(e, ValueError) and "neigiama" in str(e):
                    raise
                raise ValueError(f"Parduotuvė {i+1}, prekė {j+1}: kaina turi būti skaičius, gauta: {type(price)}")


def calculate_store_total(store):
    """
    Apskaičiuoja parduotuvės sumą ir prekių skaičių.
    
    Args:
        store (list): Parduotuvės prekių kainų sąrašas
    
    Returns:
        tuple: (item_count, total_spent)
            - item_count: Prekių skaičius
            - total_spent: Bendras išleistas kiekis (suapvalintas iki 2 skaitmenų)
    """
    item_count = len(store)
    total_spent = sum(float(price) for price in store)
    
    # Suapvaliname iki 2 skaitmenų po kablelio
    total_spent = round(total_spent, 2)
    
    return item_count, total_spent


def process_shopping_trip(stores):
    """
    Apdoroja Santa's Shopping Trip duomenis.
    
    Algoritmas:
    1. Eina per kiekvieną parduotuvę
    2. Skaičiuoja prekių skaičių ir sumą kiekvienoje parduotuvėje
    3. Sumuojame visas sumas iš visų parduotuvių
    
    Args:
        stores (list): 2D masyvas, kur kiekviena eilutė yra parduotuvė
    
    Returns:
        tuple: (store_results, grand_total)
            - store_results: sąrašas (store_number, item_count, total_spent) kiekvienai parduotuvei
            - grand_total: bendra suma visose parduotuvėse
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    # Validuojame duomenis
    validate_stores_data(stores)
    
    store_results = []
    grand_total = 0.0
    
    # Eina per kiekvieną parduotuvę
    for store_index in range(len(stores)):
        store = stores[store_index]
        store_number = store_index + 1  # Parduotuvės numeris prasideda nuo 1
        
        # Skaičiuojame prekių skaičių ir sumą
        item_count, total_spent = calculate_store_total(store)
        
        store_results.append((store_number, item_count, total_spent))
        grand_total += total_spent
    
    # Suapvaliname bendrą sumą iki 2 skaitmenų po kablelio
    grand_total = round(grand_total, 2)
    
    return store_results, grand_total


def format_output(store_results, grand_total):
    """
    Formatuoja išvestį pagal užduoties reikalavimus.
    
    Formatas:
    - Kiekvienai parduotuvei: "storeNumber itemCount totalSpent"
    - Po visų parduotuvių: "totalSpentInAllStores"
    
    Args:
        store_results (list): Parduotuvių rezultatų sąrašas
        grand_total (float): Bendras kiekis
    
    Returns:
        str: Suformatuota išvestis
    """
    lines = []
    
    # Kiekvienai parduotuvei
    for store_number, item_count, total_spent in store_results:
        lines.append(f"{store_number} {item_count} {total_spent:.2f}")
    
    # Bendras kiekis
    lines.append(f"{grand_total:.2f}")
    
    return "\n".join(lines)


def display_results(stores, store_results, grand_total, detailed=False):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        stores (list): Parduotuvių duomenys
        store_results (list): Parduotuvių rezultatų sąrašas
        grand_total (float): Bendras kiekis
        detailed (bool): Ar rodyti detalią informaciją
    """
    print("\n" + "=" * 60)
    print("🛒 SANTA'S SHOPPING TRIP RESULTS")
    print("=" * 60)
    
    if detailed:
        print("\n📋 Detali informacija:")
        for store_number, item_count, total_spent in store_results:
            store_index = store_number - 1
            store = stores[store_index]
            
            print(f"\nParduotuvė {store_number}:")
            print(f"  Prekių skaičius: {item_count}")
            print(f"  Prekių kainos: {store}")
            print(f"  Išleista suma: {total_spent:.2f} eurų")
    
    print("\n" + "=" * 60)
    print("📋 IŠVESTIS (pagal užduoties formatą):")
    print("=" * 60)
    print(format_output(store_results, grand_total))
    print("=" * 60)
    
    print("\n💡 Paaiškinimas:")
    print("   Kiekviena eilutė rodo: [parduotuvės numeris] [prekių skaičius] [išleista suma]")
    print("   Paskutinė eilutė rodo bendrą sumą visose parduotuvėse")


def get_stores_input():
    """
    Gauna parduotuvių duomenis iš vartotojo.
    
    Returns:
        list: Parduotuvių duomenys (2D masyvas)
    """
    print("\n🛒 Įveskite parduotuvių duomenis:")
    print("   Formatas: kiekviena parduotuvė atskiroje eilutėje")
    print("   Prekių kainos atskirtos tarpais arba kableliais")
    print("   Pavyzdys:")
    print("     1.07 2.92 3.45 1.09 0.89")
    print("     1.08 2.35 3.75 1.12 0.69")
    print("     0.98 2.48 3.62 1.10 0.72")
    print("   Arba įveskite 'default', kad naudotumėte pavyzdinius duomenis")
    
    user_input = input("Parduotuvė 1 (tuščia eilutė baigia įvedimą): ").strip()
    
    if user_input.lower() == 'default':
        return [
            [1.07, 2.92, 3.45, 1.09, 0.89],
            [1.08, 2.35, 3.75, 1.12, 0.69],
            [0.98, 2.48, 3.62, 1.10, 0.72]
        ]
    
    stores = []
    store_number = 1
    
    while user_input:
        # Skirstome pagal tarpus arba kablelius
        if ',' in user_input:
            parts = [p.strip() for p in user_input.split(',')]
        else:
            parts = user_input.split()
        
        try:
            store = [float(x) for x in parts if x]
            if store:
                stores.append(store)
        except ValueError as e:
            raise ValueError(f"Nepavyko konvertuoti į skaičius: {e}")
        
        store_number += 1
        user_input = input(f"Parduotuvė {store_number} (tuščia eilutė baigia): ").strip()
    
    if not stores:
        raise ValueError("Nepavyko nuskaityti parduotuvių duomenų.")
    
    return stores


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas - užduoties pavyzdys",
            "stores": [
                [1.07, 2.92, 3.45, 1.09, 0.89],
                [1.08, 2.35, 3.75, 1.12, 0.69],
                [0.98, 2.48, 3.62, 1.10, 0.72]
            ],
            "expected_results": [
                (1, 5, 9.42),
                (2, 5, 8.99),
                (3, 5, 8.90)
            ],
            "expected_total": 27.31,
            "description": "Standartinis užduoties pavyzdys"
        },
        {
            "name": "Viena parduotuvė",
            "stores": [
                [10.50, 20.75, 5.25]
            ],
            "expected_results": [
                (1, 3, 36.50)
            ],
            "expected_total": 36.50,
            "description": "Tik viena parduotuvė"
        },
        {
            "name": "Viena prekė kiekvienoje parduotuvėje",
            "stores": [
                [10.00],
                [20.00],
                [30.00]
            ],
            "expected_results": [
                (1, 1, 10.00),
                (2, 1, 20.00),
                (3, 1, 30.00)
            ],
            "expected_total": 60.00,
            "description": "Kiekvienoje parduotuvėje po vieną prekę"
        },
        {
            "name": "Suapvalinimo testas",
            "stores": [
                [1.111, 2.222],
                [3.333, 4.444]
            ],
            "expected_results": [
                (1, 2, 3.33),
                (2, 2, 7.78)
            ],
            "expected_total": 11.11,
            "description": "Tikrinimas suapvalinimo iki 2 skaitmenų"
        },
        {
            "name": "Daug parduotuvių",
            "stores": [
                [1.00, 2.00],
                [3.00, 4.00],
                [5.00, 6.00],
                [7.00, 8.00]
            ],
            "expected_results": [
                (1, 2, 3.00),
                (2, 2, 7.00),
                (3, 2, 11.00),
                (4, 2, 15.00)
            ],
            "expected_total": 36.00,
            "description": "Keturių parduotuvių testas"
        },
        {
            "name": "Skirtingas prekių skaičius",
            "stores": [
                [1.00],
                [2.00, 3.00],
                [4.00, 5.00, 6.00]
            ],
            "expected_results": [
                (1, 1, 1.00),
                (2, 2, 5.00),
                (3, 3, 15.00)
            ],
            "expected_total": 21.00,
            "description": "Kiekvienoje parduotuvėje skirtingas prekių skaičius"
        },
        {
            "name": "Mažos kainos",
            "stores": [
                [0.01, 0.02, 0.03],
                [0.04, 0.05]
            ],
            "expected_results": [
                (1, 3, 0.06),
                (2, 2, 0.09)
            ],
            "expected_total": 0.15,
            "description": "Labai mažos kainos"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    tolerance = 0.01  # Tolerancija slankiojo kablelio palyginimui
    
    for test in test_cases:
        try:
            stores = test["stores"]
            store_results, grand_total = process_shopping_trip(stores)
            
            expected_results = test["expected_results"]
            expected_total = test["expected_total"]
            
            # Palyginimas rezultatų
            results_match = len(store_results) == len(expected_results)
            if results_match:
                for i, (result, expected) in enumerate(zip(store_results, expected_results)):
                    store_num, item_count, total = result
                    exp_store_num, exp_item_count, exp_total = expected
                    
                    if (store_num != exp_store_num or 
                        item_count != exp_item_count or 
                        abs(total - exp_total) >= tolerance):
                        results_match = False
                        break
            
            total_match = abs(grand_total - expected_total) < tolerance
            
            passed = results_match and total_match
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            print(f"      Parduotuvių skaičius: {len(stores)}")
            print(f"      Rezultatai: {store_results}")
            print(f"      Tikėtasi: {expected_results}")
            print(f"      Bendras kiekis: {grand_total:.2f} (tikėtasi: {expected_total:.2f})")
            
            if not passed:
                if not results_match:
                    print(f"      ❌ Neteisingi parduotuvių rezultatai!")
                if not total_match:
                    print(f"      ❌ Neteisingas bendras kiekis!")
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
    print("🛒 SANTA'S SHOPPING TRIP")
    print("=" * 60)
    print("\nŠi programa apskaičiuoja, kiek pinigų Santa išleido")
    print("kiekvienoje parduotuvėje ir iš viso visose parduotuvėse.")
    print("\nKiekvienai parduotuvei skaičiuojama:")
    print("  • Parduotuvės numeris")
    print("  • Prekių skaičius")
    print("  • Išleista suma (suapvalinta iki 2 skaitmenų)\n")
    
    try:
        # Gauname parduotuvių duomenis
        stores = get_stores_input()
        
        if not stores:
            print("❌ Klaida: Nepavyko nuskaityti parduotuvių duomenų.")
            return False
        
        # Apdorojame duomenis
        store_results, grand_total = process_shopping_trip(stores)
        
        # Atvaizduojame rezultatus
        display_results(stores, store_results, grand_total, detailed=True)
        
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

