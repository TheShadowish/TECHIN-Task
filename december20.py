"""
Santa's Christmas Call Center - Billing Task Solution

Užduotis: Apskaičiuoti, kiek kiekvienas elfas turi sumokėti už skambučius
ir paruošti sąskaitų ataskaitą.

Duomenys:
- Elfų sąrašas su vardais ir skambučių sąrašu
- Kiekvienas skambutis turi miestą ir minučių skaičių
- Kainų sąrašas: kiekvienam miestui kaina per minutę

Užduotis:
1. Apskaičiuoti bendrą kiekvieno elfo skambučių kainą
2. Surūšiuoti elfus pagal pavardę abėcėlės tvarka
3. Išvesti ataskaitą: vardas, pavardė, bendra kaina
4. Išvesti bendrą sumą iš visų elfų

Sprendimas:
- Kiekvienam elfui skaičiuojame skambučių kainą pagal miestą ir minučių skaičių
- Surūšiuojame elfus pagal pavardę
- Suapvaliname sumas iki 2 skaitmenų po kablelio
"""

from typing import List, Dict, Tuple


def validate_elf_data(elf):
    """
    Validuoja elfo duomenis.
    
    Args:
        elf (dict): Elfo duomenys
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    if not isinstance(elf, dict):
        raise ValueError(f"Elfo duomenys turi būti žodynas (dict), gauta: {type(elf)}")
    
    required_fields = ['firstName', 'lastName', 'calls']
    for field in required_fields:
        if field not in elf:
            raise ValueError(f"Elfo duomenys turi turėti '{field}' lauką")
    
    if not isinstance(elf['firstName'], str) or not isinstance(elf['lastName'], str):
        raise ValueError("Elfo vardas ir pavardė turi būti eilutės (string)")
    
    if not isinstance(elf['calls'], (list, tuple)):
        raise ValueError(f"Elfo skambučių sąrašas turi būti list arba tuple, gauta: {type(elf['calls'])}")
    
    for i, call in enumerate(elf['calls']):
        if not isinstance(call, dict):
            raise ValueError(f"Skambutis {i+1} turi būti žodynas (dict), gauta: {type(call)}")
        
        if 'city' not in call or 'minutes' not in call:
            raise ValueError(f"Skambutis {i+1} turi turėti 'city' ir 'minutes' laukus")
        
        try:
            minutes = float(call['minutes'])
            if minutes < 0:
                raise ValueError(f"Skambutis {i+1}: minučių skaičius negali būti neigiamas, gauta: {minutes}")
        except (TypeError, ValueError) as e:
            if isinstance(e, ValueError) and "neigiamas" in str(e):
                raise
            raise ValueError(f"Skambutis {i+1}: minučių skaičius turi būti skaičius, gauta: {type(call['minutes'])}")


def validate_price_list(price_list):
    """
    Validuoja kainų sąrašą.
    
    Args:
        price_list (dict): Kainų sąrašas {miestas: kaina_per_minutę}
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    if not isinstance(price_list, dict):
        raise ValueError(f"Kainų sąrašas turi būti žodynas (dict), gauta: {type(price_list)}")
    
    for city, price in price_list.items():
        try:
            price = float(price)
            if price < 0:
                raise ValueError(f"Miestas '{city}': kaina negali būti neigiama, gauta: {price}")
        except (TypeError, ValueError) as e:
            if isinstance(e, ValueError) and "neigiama" in str(e):
                raise
            raise ValueError(f"Miestas '{city}': kaina turi būti skaičius, gauta: {type(price)}")


def calculate_elf_cost(elf, price_list):
    """
    Apskaičiuoja elfo skambučių bendrą kainą.
    
    Algoritmas:
    - Kiekvienam skambučiui: miestas * minučių_skaičius * kaina_per_minutę
    - Sumuojame visas skambučių kainas
    
    Args:
        elf (dict): Elfo duomenys
        price_list (dict): Kainų sąrašas
    
    Returns:
        float: Bendras elfo skambučių kiekis (suapvalintas iki 2 skaitmenų)
    
    Raises:
        ValueError: Jei miestas nerastas kainų sąraše
    """
    validate_elf_data(elf)
    validate_price_list(price_list)
    
    total_cost = 0.0
    
    for call in elf['calls']:
        city = call['city']
        minutes = float(call['minutes'])
        
        if city not in price_list:
            raise ValueError(f"Miestas '{city}' nerastas kainų sąraše")
        
        price_per_minute = float(price_list[city])
        call_cost = minutes * price_per_minute
        total_cost += call_cost
    
    # Suapvaliname iki 2 skaitmenų po kablelio
    return round(total_cost, 2)


def process_billing(elves, price_list):
    """
    Apdoroja sąskaitų faktūravimą visiems elfams.
    
    Algoritmas:
    1. Kiekvienam elfui apskaičiuojame skambučių kainą
    2. Surūšiuojame elfus pagal pavardę abėcėlės tvarka
    3. Sumuojame visas sumas
    
    Args:
        elves (list): Elfų sąrašas
        price_list (dict): Kainų sąrašas
    
    Returns:
        tuple: (billing_results, grand_total)
            - billing_results: sąrašas (last_name, first_name, total_cost) surūšiuotas pagal pavardę
            - grand_total: bendra suma visų elfų
    
    Raises:
        ValueError: Jei duomenys netinkami
    """
    if not isinstance(elves, (list, tuple)):
        raise ValueError(f"Elfų sąrašas turi būti list arba tuple, gauta: {type(elves)}")
    
    if len(elves) == 0:
        raise ValueError("Elfų sąrašas negali būti tuščias")
    
    validate_price_list(price_list)
    
    billing_results = []
    
    # Kiekvienam elfui apskaičiuojame kainą
    for elf in elves:
        validate_elf_data(elf)
        total_cost = calculate_elf_cost(elf, price_list)
        
        billing_results.append({
            'firstName': elf['firstName'],
            'lastName': elf['lastName'],
            'totalCost': total_cost
        })
    
    # Surūšiuojame pagal pavardę abėcėlės tvarka
    billing_results.sort(key=lambda x: x['lastName'])
    
    # Skaičiuojame bendrą sumą
    grand_total = sum(result['totalCost'] for result in billing_results)
    grand_total = round(grand_total, 2)
    
    return billing_results, grand_total


def format_output(billing_results, grand_total):
    """
    Formatuoja išvestį pagal užduoties reikalavimus.
    
    Formatas:
    - Kiekvienam elfui: "lastName firstName totalCost"
    - Po visų elfų: "Total: grandTotal"
    
    Args:
        billing_results (list): Sąskaitų rezultatų sąrašas
        grand_total (float): Bendras kiekis
    
    Returns:
        str: Suformatuota išvestis
    """
    lines = []
    
    # Kiekvienam elfui
    for result in billing_results:
        lines.append(f"{result['lastName']} {result['firstName']} {result['totalCost']:.2f}")
    
    # Bendras kiekis
    lines.append(f"Total: {grand_total:.2f}")
    
    return "\n".join(lines)


def display_results(elves, price_list, billing_results, grand_total, detailed=False):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        elves (list): Elfų duomenys
        price_list (dict): Kainų sąrašas
        billing_results (list): Sąskaitų rezultatų sąrašas
        grand_total (float): Bendras kiekis
        detailed (bool): Ar rodyti detalią informaciją
    """
    print("\n" + "=" * 60)
    print("📞 SANTA'S CHRISTMAS CALL CENTER - BILLING REPORT")
    print("=" * 60)
    
    if detailed:
        print("\n📋 Detali informacija:")
        print(f"  Elfų skaičius: {len(elves)}")
        print(f"  Miestų skaičius kainų sąraše: {len(price_list)}")
        
        print("\n  Kainų sąrašas:")
        for city, price in sorted(price_list.items()):
            print(f"    {city}: {price:.2f} per minutę")
        
        print("\n  Elfų skambučiai:")
        for i, elf in enumerate(elves, 1):
            print(f"\n  Elfas {i}: {elf['firstName']} {elf['lastName']}")
            total_cost = calculate_elf_cost(elf, price_list)
            print(f"    Skambučių skaičius: {len(elf['calls'])}")
            for call in elf['calls']:
                city = call['city']
                minutes = call['minutes']
                price = price_list.get(city, 0)
                call_cost = minutes * price
                print(f"      {city}: {minutes} min. × {price:.2f} = {call_cost:.2f}")
            print(f"    Bendras kiekis: {total_cost:.2f}")
    
    print("\n" + "=" * 60)
    print("📋 IŠVESTIS (pagal užduoties formatą):")
    print("=" * 60)
    print(format_output(billing_results, grand_total))
    print("=" * 60)
    
    print("\n💡 Paaiškinimas:")
    print("   Elfai surūšiuoti pagal pavardę abėcėlės tvarka.")
    print("   Kiekvienam elfui rodoma: pavardė, vardas, bendras skambučių kiekis.")


def get_default_data():
    """
    Grąžina pavyzdinius duomenis iš užduoties.
    
    Returns:
        tuple: (elves, price_list)
    """
    elves = [
        {
            "firstName": "Jingle",
            "lastName": "Sparkfoot",
            "calls": [
                {"city": "London", "minutes": 12},
                {"city": "Paris", "minutes": 7}
            ]
        },
        {
            "firstName": "Twinkle",
            "lastName": "Icicletoes",
            "calls": [
                {"city": "NewYork", "minutes": 20},
                {"city": "London", "minutes": 5}
            ]
        },
        {
            "firstName": "Pudding",
            "lastName": "Gumdrops",
            "calls": [
                {"city": "Paris", "minutes": 15}
            ]
        }
    ]
    
    price_list = {
        "London": 0.50,
        "Paris": 0.40,
        "NewYork": 0.70
    }
    
    return elves, price_list


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas - užduoties pavyzdys",
            "elves": [
                {
                    "firstName": "Jingle",
                    "lastName": "Sparkfoot",
                    "calls": [
                        {"city": "London", "minutes": 12},
                        {"city": "Paris", "minutes": 7}
                    ]
                },
                {
                    "firstName": "Twinkle",
                    "lastName": "Icicletoes",
                    "calls": [
                        {"city": "NewYork", "minutes": 20},
                        {"city": "London", "minutes": 5}
                    ]
                },
                {
                    "firstName": "Pudding",
                    "lastName": "Gumdrops",
                    "calls": [
                        {"city": "Paris", "minutes": 15}
                    ]
                }
            ],
            "price_list": {
                "London": 0.50,
                "Paris": 0.40,
                "NewYork": 0.70
            },
            "expected": [
                ("Gumdrops", "Pudding", 6.00),
                ("Icicletoes", "Twinkle", 16.50),
                ("Sparkfoot", "Jingle", 9.50)
            ],
            "expected_total": 32.00,
            "description": "Standartinis užduoties pavyzdys"
        },
        {
            "name": "Vienas elfas",
            "elves": [
                {
                    "firstName": "Test",
                    "lastName": "Elf",
                    "calls": [
                        {"city": "London", "minutes": 10}
                    ]
                }
            ],
            "price_list": {
                "London": 0.50
            },
            "expected": [
                ("Elf", "Test", 5.00)
            ],
            "expected_total": 5.00,
            "description": "Tik vienas elfas"
        },
        {
            "name": "Jokių skambučių",
            "elves": [
                {
                    "firstName": "Test",
                    "lastName": "Elf",
                    "calls": []
                }
            ],
            "price_list": {
                "London": 0.50
            },
            "expected": [
                ("Elf", "Test", 0.00)
            ],
            "expected_total": 0.00,
            "description": "Elfas be skambučių"
        },
        {
            "name": "Daug skambučių",
            "elves": [
                {
                    "firstName": "Test",
                    "lastName": "Elf",
                    "calls": [
                        {"city": "London", "minutes": 1},
                        {"city": "Paris", "minutes": 2},
                        {"city": "NewYork", "minutes": 3}
                    ]
                }
            ],
            "price_list": {
                "London": 0.50,
                "Paris": 0.40,
                "NewYork": 0.70
            },
            "expected": [
                ("Elf", "Test", 3.40)
            ],
            "expected_total": 3.40,
            "description": "Elfas su daug skambučių"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    tolerance = 0.01  # Tolerancija slankiojo kablelio palyginimui
    
    for test in test_cases:
        try:
            elves = test["elves"]
            price_list = test["price_list"]
            expected = test["expected"]
            expected_total = test["expected_total"]
            
            billing_results, grand_total = process_billing(elves, price_list)
            
            # Palyginimas rezultatų
            results_match = len(billing_results) == len(expected)
            if results_match:
                for i, (result, exp) in enumerate(zip(billing_results, expected)):
                    exp_last, exp_first, exp_cost = exp
                    if (result['lastName'] != exp_last or
                        result['firstName'] != exp_first or
                        abs(result['totalCost'] - exp_cost) >= tolerance):
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
            print(f"      Elfų skaičius: {len(elves)}")
            print(f"      Rezultatai: {[(r['lastName'], r['firstName'], r['totalCost']) for r in billing_results]}")
            print(f"      Tikėtasi: {expected}")
            print(f"      Bendras kiekis: {grand_total:.2f} (tikėtasi: {expected_total:.2f})")
            
            if not passed:
                if not results_match:
                    print(f"      ❌ Neteisingi sąskaitų rezultatai!")
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
    print("📞 SANTA'S CHRISTMAS CALL CENTER - BILLING TASK")
    print("=" * 60)
    print("\nŠi programa apskaičiuoja, kiek kiekvienas elfas turi")
    print("sumokėti už skambučius ir paruošia sąskaitų ataskaitą.")
    print("\nElfai surūšiuojami pagal pavardę abėcėlės tvarka.\n")
    
    try:
        # Naudojame pavyzdinius duomenis
        elves, price_list = get_default_data()
        
        print("Naudojami pavyzdiniai duomenys iš užduoties.")
        print("(Norėdami naudoti kitus duomenis, redaguokite kodą)")
        
        # Apdorojame duomenis
        billing_results, grand_total = process_billing(elves, price_list)
        
        # Atvaizduojame rezultatus
        display_results(elves, price_list, billing_results, grand_total, detailed=True)
        
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