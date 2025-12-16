"""
Peter's Christmas Shopping Dilemma Solution

Užduotis: Nustatyti, kiek pinigų Peter išleis, jei jis visada perka pigiausią
iš trijų prekių:
- Knyga: x eurų
- Muzikos CD: y eurų
- USB atmintinė: z eurų

Sprendimas: Rasti mažiausią iš trijų kainų.

Algoritmas:
1. Gauname tris kainas
2. Randame mažiausią naudojant min() funkciją
3. Atvaizduojame rezultatą su dviem skaitmenimis po kablelio
"""

from typing import List, Tuple


def validate_price(price, name):
    """
    Validuoja kainą.
    
    Args:
        price: Kaina (turi būti skaičius)
        name (str): Kainos pavadinimas (naudojamas klaidų pranešimuose)
    
    Returns:
        float: Validuota kaina
    
    Raises:
        ValueError: Jei kaina netinkama
    """
    try:
        price = float(price)
    except (TypeError, ValueError):
        raise ValueError(f"{name} turi būti skaičius, gauta: {type(price)}")
    
    if price < 0:
        raise ValueError(f"{name} negali būti neigiama, gauta: {price}")
    
    return price


def find_minimum_price(book_price, cd_price, usb_price):
    """
    Randa mažiausią kainą iš trijų prekių.
    
    Args:
        book_price (float): Knygos kaina eurais
        cd_price (float): Muzikos CD kaina eurais
        usb_price (float): USB atmintinės kaina eurais
    
    Returns:
        float: Mažiausia kaina
    
    Raises:
        ValueError: Jei bet kuri kaina netinkama
    """
    # Validuojame visas kainas
    book_price = validate_price(book_price, "Knygos kaina")
    cd_price = validate_price(cd_price, "CD kaina")
    usb_price = validate_price(usb_price, "USB atmintinės kaina")
    
    # Randame mažiausią kainą
    min_price = min(book_price, cd_price, usb_price)
    
    return min_price


def parse_input(user_input):
    """
    Parsina vartotojo įvestį į tris kainas.
    
    Palaiko įvairius formatus:
    - "x y z" (atskirti tarpais)
    - "x,y,z" (atskirti kableliais)
    - Po vieną eilutėje
    
    Args:
        user_input (str): Vartotojo įvestis
    
    Returns:
        tuple: (book_price, cd_price, usb_price)
    
    Raises:
        ValueError: Jei nepavyko nuskaityti trijų kainų
    """
    if not user_input or not user_input.strip():
        raise ValueError("Įvestis negali būti tuščia")
    
    # Skirstome pagal tarpus arba kablelius
    if ',' in user_input:
        parts = [p.strip() for p in user_input.split(',')]
    else:
        parts = user_input.split()
    
    if len(parts) != 3:
        raise ValueError(
            f"Tikėtasi trijų kainų, gauta {len(parts)}. "
            f"Įveskite kainas formatu: 'x y z' arba 'x,y,z'"
        )
    
    try:
        book_price = float(parts[0])
        cd_price = float(parts[1])
        usb_price = float(parts[2])
    except ValueError as e:
        raise ValueError(f"Nepavyko konvertuoti kainų į skaičius: {e}")
    
    return book_price, cd_price, usb_price


def format_output(min_price, detailed=False):
    """
    Formatuoja išvestį pagal užduoties reikalavimus.
    
    Args:
        min_price (float): Mažiausia kaina
        detailed (bool): Ar rodyti detalią informaciją
    
    Returns:
        str: Suformatuota išvestis
    """
    if detailed:
        return f"Peter will spend {min_price:.2f} euros."
    else:
        return f"{min_price:.2f}"


def display_results(book_price, cd_price, usb_price, min_price):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        book_price (float): Knygos kaina
        cd_price (float): CD kaina
        usb_price (float): USB atmintinės kaina
        min_price (float): Mažiausia kaina
    """
    print("\n" + "=" * 60)
    print("📊 REZULTATAI")
    print("=" * 60)
    print(f"Knygos kaina:        {book_price:.2f} eurų")
    print(f"Muzikos CD kaina:    {cd_price:.2f} eurų")
    print(f"USB atmintinės kaina: {usb_price:.2f} eurų")
    print("-" * 60)
    
    # Nustatome, kuri prekė yra pigiausia
    cheapest_items = []
    if book_price == min_price:
        cheapest_items.append("Knyga")
    if cd_price == min_price:
        cheapest_items.append("Muzikos CD")
    if usb_price == min_price:
        cheapest_items.append("USB atmintinė")
    
    if len(cheapest_items) == 1:
        print(f"Pigiausia prekė:     {cheapest_items[0]}")
    else:
        print(f"Pigiausios prekės:   {', '.join(cheapest_items)} (lygios kainos)")
    
    print("=" * 60)
    print("\n📋 IŠVESTIS (pagal užduoties formatą):")
    print("=" * 60)
    print(format_output(min_price))
    print("\n💬 Su tekstu:")
    print(format_output(min_price, detailed=True))
    print("=" * 60)


def get_prices_input():
    """
    Gauna tris kainas iš vartotojo su validacija.
    
    Returns:
        tuple: (book_price, cd_price, usb_price)
    """
    print("\n💰 Įveskite trijų prekių kainas:")
    print("   Formatas: 'x y z' (atskirti tarpais)")
    print("   Arba: 'x,y,z' (atskirti kableliais)")
    print("   Pavyzdys: '15.50 12.30 18.75'")
    print("   Arba įveskite 'default', kad naudotumėte pavyzdinius duomenis")
    
    user_input = input("Kainos: ").strip()
    
    if user_input.lower() == 'default':
        return 15.50, 12.30, 18.75
    
    return parse_input(user_input)


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas",
            "book": 15.50,
            "cd": 12.30,
            "usb": 18.75,
            "expected": 12.30,
            "description": "CD yra pigiausias"
        },
        {
            "name": "Knyga pigiausia",
            "book": 10.00,
            "cd": 15.50,
            "usb": 20.00,
            "expected": 10.00,
            "description": "Knyga yra pigiausia"
        },
        {
            "name": "USB pigiausia",
            "book": 25.00,
            "cd": 20.00,
            "usb": 15.00,
            "expected": 15.00,
            "description": "USB yra pigiausia"
        },
        {
            "name": "Visos vienodos kainos",
            "book": 10.00,
            "cd": 10.00,
            "usb": 10.00,
            "expected": 10.00,
            "description": "Visos prekės vienodos kainos"
        },
        {
            "name": "Dvi vienodos, viena skirtinga",
            "book": 10.00,
            "cd": 10.00,
            "usb": 15.00,
            "expected": 10.00,
            "description": "Dvi prekės vienodos, trečia brangesnė"
        },
        {
            "name": "Su kableliais",
            "book": 7.24,
            "cd": 8.50,
            "usb": 6.99,
            "expected": 6.99,
            "description": "USB pigiausia su kableliais"
        },
        {
            "name": "Didelės kainos",
            "book": 100.00,
            "cd": 50.00,
            "usb": 75.00,
            "expected": 50.00,
            "description": "CD pigiausia tarp didelių kainų"
        },
        {
            "name": "Mažos kainos",
            "book": 1.50,
            "cd": 2.00,
            "usb": 1.25,
            "expected": 1.25,
            "description": "USB pigiausia tarp mažų kainų"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    tolerance = 0.01  # Tolerancija slankiojo kablelio palyginimui
    
    for test in test_cases:
        try:
            book_price = test["book"]
            cd_price = test["cd"]
            usb_price = test["usb"]
            expected = test["expected"]
            
            min_price = find_minimum_price(book_price, cd_price, usb_price)
            
            passed = abs(min_price - expected) < tolerance
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            print(f"      Įvestis: knyga={book_price}, CD={cd_price}, USB={usb_price}")
            print(f"      Tikėtasi: {expected:.2f}, Gauta: {min_price:.2f}")
            
            if not passed:
                print(f"      ❌ Skirtumas: {abs(min_price - expected):.6f}")
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
    print("🛒 PETER'S CHRISTMAS SHOPPING DILEMMA")
    print("=" * 60)
    print("\nPeter nori nusipirkti vieną Kalėdų dovaną.")
    print("Jis turi tris pasirinkimus:")
    print("  • Knyga: x eurų")
    print("  • Muzikos CD: y eurų")
    print("  • USB atmintinė: z eurų")
    print("\nPeter visada perka pigiausią prekę.\n")
    
    try:
        # Gauname kainas
        book_price, cd_price, usb_price = get_prices_input()
        
        # Randame mažiausią kainą
        min_price = find_minimum_price(book_price, cd_price, usb_price)
        
        # Atvaizduojame rezultatus
        display_results(book_price, cd_price, usb_price, min_price)
        
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

