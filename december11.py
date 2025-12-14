"""
Santa's Magical Archery Challenge Solution

Užduotis: Apskaičiuoti, kiek taškų pelnė elfas pagal strėlės nusileidimo vietą
ant taikinio su koncentriniais žiedais.

Sprendimas:
1. Apskaičiuojame atstumą nuo strėlės iki taikinio centro
2. Nustatome, kuriame žiede (ar ant jo ribos) nusileido strėlė
3. Jei strėlė nusileido ant ribos - skiriame pusę taškų
4. Jei strėlė nusileido žiede - skiriame visus taškus
5. Jei strėlė nusileido už visų žiedų - 0 taškų
"""

import math


def calculate_distance(x1, y1, x2, y2):
    """
    Apskaičiuoja Euklido atstumą tarp dviejų taškų.
    
    Args:
        x1 (float): Pirmo taško x koordinatė
        y1 (float): Pirmo taško y koordinatė
        x2 (float): Antro taško x koordinatė
        y2 (float): Antro taško y koordinatė
    
    Returns:
        float: Atstumas tarp taškų
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_points(center_x, center_y, arrow_x, arrow_y, rings, points, tolerance=1e-9):
    """
    Apskaičiuoja taškus pagal strėlės nusileidimo vietą.
    
    Algoritmas:
    1. Apskaičiuojame atstumą nuo strėlės iki taikinio centro
    2. Patikriname, kuriame žiede nusileido strėlė (nuo vidinio iki išorinio)
    3. Jei atstumas tiksliai lygus žiedo spinduliui - pusė taškų
    4. Jei atstumas mažesnis už spindulį - visi taškai
    5. Jei atstumas didesnis už visus spindulius - 0 taškų
    
    Args:
        center_x (float): Taikinio centro x koordinatė
        center_y (float): Taikinio centro y koordinatė
        arrow_x (float): Strėlės nusileidimo x koordinatė
        arrow_y (float): Strėlės nusileidimo y koordinatė
        rings (list): Žiedų spindulių sąrašas (nuo vidinio iki išorinio)
        points (list): Taškų sąrašas kiekvienam žiedui (nuo vidinio iki išorinio)
        tolerance (float): Tolerancija, kurią laikome "tiksliai ant ribos"
    
    Returns:
        tuple: (taškai, paaiškinimas)
    """
    # Validacija įvesties duomenų
    if not isinstance(rings, (list, tuple)) or not isinstance(points, (list, tuple)):
        raise ValueError("Žiedų spindulių ir taškų sąrašai turi būti list arba tuple tipai")
    
    if len(rings) != len(points):
        raise ValueError(f"Žiedų skaičius ({len(rings)}) turi sutapti su taškų skaičiumi ({len(points)})")
    
    if len(rings) == 0:
        raise ValueError("Turėtų būti bent vienas žiedas")
    
    # Patikrinimas, ar spinduliai yra teigiami ir didėja
    for i, radius in enumerate(rings):
        if radius <= 0:
            raise ValueError(f"Žiedo {i+1} spindulys turi būti teigiamas, gauta: {radius}")
        if i > 0 and radius <= rings[i-1]:
            raise ValueError(f"Žiedų spinduliai turi didėti. Žiedas {i+1} ({radius}) turi būti didesnis už {i} ({rings[i-1]})")
    
    # Apskaičiuojame atstumą nuo strėlės iki centro
    distance = calculate_distance(center_x, center_y, arrow_x, arrow_y)
    
    # Nustatome, kuriame žiede nusileido strėlė
    # Eini nuo vidinio žiedo (didžiausias taškų skaičius) iki išorinio
    for i in range(len(rings)):
        radius = rings[i]
        ring_points = points[i]
        
        # Patikrinimas, ar strėlė nusileido tiksliai ant ribos
        if abs(distance - radius) < tolerance:
            # Strėlė ant ribos - pusė taškų
            earned_points = ring_points / 2.0
            explanation = (
                f"Strėlė nusileido tiksliai ant {i+1}-ojo žiedo ribos "
                f"(atstumas: {distance:.6f} ≈ spindulys: {radius}). "
                f"Skiriama pusė taškų: {ring_points} / 2 = {earned_points}"
            )
            return earned_points, explanation
        
        # Patikrinimas, ar strėlė nusileido žiede
        if distance < radius:
            # Strėlė žiede - visi taškai
            earned_points = ring_points
            explanation = (
                f"Strėlė nusileido {i+1}-ajame žiede "
                f"(atstumas: {distance:.6f} < spindulys: {radius}). "
                f"Skiriami visi taškai: {earned_points}"
            )
            return earned_points, explanation
    
    # Strėlė nusileido už visų žiedų
    earned_points = 0
    explanation = (
        f"Strėlė nusileido už visų žiedų "
        f"(atstumas: {distance:.6f} > didžiausias spindulys: {rings[-1]}). "
        f"Taškai: 0"
    )
    return earned_points, explanation


def get_float_input(prompt, input_name, allow_negative=False):
    """
    Gauna ir validuoja realųjį skaičių su pakartotiniais bandymais.
    
    Args:
        prompt (str): Užklausos tekstas
        input_name (str): Įvesties pavadinimas (naudojamas klaidų pranešimuose)
        allow_negative (bool): Ar leisti neigiamus skaičius
    
    Returns:
        float: Validuota reikšmė
    """
    max_attempts = 3
    attempt = 0
    
    while attempt < max_attempts:
        try:
            value = input(prompt).strip()
            
            if not value:
                raise ValueError(f"{input_name} negali būti tuščias. Įveskite skaičių.")
            
            value = float(value)
            
            if not allow_negative and value < 0:
                raise ValueError(f"{input_name} negali būti neigiamas. Įveskite neneigiamą skaičių.")
            
            return value
            
        except ValueError as e:
            attempt += 1
            remaining = max_attempts - attempt
            
            if attempt < max_attempts:
                print(f"❌ Klaida: {e}")
                print(f"📝 Bandykite dar kartą. Liko bandymų: {remaining}\n")
            else:
                print(f"❌ Klaida: {e}")
                print(f"⚠️  Pasiektas maksimalus bandymų skaičius ({max_attempts}). Programa baigia darbą.")
                raise
    
    return None


def get_rings_input():
    """
    Gauna žiedų spindulių ir taškų informaciją iš vartotojo.
    
    Returns:
        tuple: (rings, points) - žiedų spindulių ir taškų sąrašai
    """
    print("\n📋 Žiedų konfigūracija:")
    print("   (Vidinis juodas apskritimas + 3 papildomi žiedai = 4 žiedai iš viso)")
    
    num_rings = 4  # Standartinis: vidinis apskritimas + 3 žiedai
    
    rings = []
    points = []
    
    print("\nĮveskite informaciją apie žiedus (nuo vidinio iki išorinio):")
    
    for i in range(num_rings):
        ring_name = "Vidinis juodas apskritimas" if i == 0 else f"{i}-asis žiedas"
        
        radius = get_float_input(
            f"  {ring_name} - spindulys: ",
            f"{ring_name} spindulys",
            allow_negative=False
        )
        
        point_value = get_float_input(
            f"  {ring_name} - taškai: ",
            f"{ring_name} taškai",
            allow_negative=False
        )
        
        rings.append(radius)
        points.append(point_value)
    
    return rings, points


def display_results(center_x, center_y, arrow_x, arrow_y, rings, points, earned_points, explanation):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        center_x (float): Taikinio centro x koordinatė
        center_y (float): Taikinio centro y koordinatė
        arrow_x (float): Strėlės x koordinatė
        arrow_y (float): Strėlės y koordinatė
        rings (list): Žiedų spindulių sąrašas
        points (list): Taškų sąrašas
        earned_points (float): Pelnyti taškai
        explanation (str): Paaiškinimas
    """
    print("\n" + "=" * 60)
    print("📊 REZULTATAI")
    print("=" * 60)
    print(f"Taikinio centras: ({center_x}, {center_y})")
    print(f"Strėlės pozicija: ({arrow_x}, {arrow_y})")
    
    distance = calculate_distance(center_x, center_y, arrow_x, arrow_y)
    print(f"Atstumas nuo centro: {distance:.6f}")
    
    print("\nŽiedų konfigūracija:")
    for i, (radius, point_value) in enumerate(zip(rings, points)):
        ring_name = "Vidinis apskritimas" if i == 0 else f"Žiedas {i}"
        print(f"  {ring_name}: spindulys = {radius}, taškai = {point_value}")
    
    print("\n" + "=" * 60)
    print(f"🎯 PELNYTI TAŠKAI: {earned_points}")
    print("=" * 60)
    print(f"\n💡 Paaiškinimas:")
    print(f"   {explanation}")


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    # Test case 1: Strėlė vidiniame apskritime
    # Test case 2: Strėlė ant pirmo žiedo ribos
    # Test case 3: Strėlė antrame žiede
    # Test case 4: Strėlė už visų žiedų
    # Test case 5: Strėlė tiksliai ant centro
    
    test_cases = [
        {
            "name": "Strėlė vidiniame apskritime",
            "center": (0, 0),
            "arrow": (1, 1),
            "rings": [2, 5, 8, 10],
            "points": [10, 8, 5, 3],
            "expected_points": 10,
            "description": "Atstumas ~1.414 < 2, turėtų gauti 10 taškų"
        },
        {
            "name": "Strėlė tiksliai ant pirmo žiedo ribos",
            "center": (0, 0),
            "arrow": (2, 0),
            "rings": [2, 5, 8, 10],
            "points": [10, 8, 5, 3],
            "expected_points": 5.0,  # Pusė taškų
            "description": "Atstumas = 2 (tiksliai ant ribos), turėtų gauti 5 taškus (10/2)"
        },
        {
            "name": "Strėlė antrame žiede",
            "center": (0, 0),
            "arrow": (3, 0),
            "rings": [2, 5, 8, 10],
            "points": [10, 8, 5, 3],
            "expected_points": 8,
            "description": "Atstumas 3, 2 < 3 < 5, turėtų gauti 8 taškus"
        },
        {
            "name": "Strėlė už visų žiedų",
            "center": (0, 0),
            "arrow": (15, 0),
            "rings": [2, 5, 8, 10],
            "points": [10, 8, 5, 3],
            "expected_points": 0,
            "description": "Atstumas 15 > 10, turėtų gauti 0 taškų"
        },
        {
            "name": "Strėlė tiksliai ant centro",
            "center": (5, 5),
            "arrow": (5, 5),
            "rings": [2, 5, 8, 10],
            "points": [10, 8, 5, 3],
            "expected_points": 10,
            "description": "Atstumas = 0, turėtų gauti 10 taškų (vidinis apskritimas)"
        },
        {
            "name": "Strėlė ant trečiojo žiedo ribos",
            "center": (0, 0),
            "arrow": (8, 0),
            "rings": [2, 5, 8, 10],
            "points": [10, 8, 5, 3],
            "expected_points": 2.5,  # Pusė taškų
            "description": "Atstumas = 8 (tiksliai ant ribos), turėtų gauti 2.5 taškus (5/2)"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    tolerance = 1e-6  # Tolerancija taškų palyginimui
    
    for test in test_cases:
        try:
            center_x, center_y = test["center"]
            arrow_x, arrow_y = test["arrow"]
            rings = test["rings"]
            points = test["points"]
            expected = test["expected_points"]
            
            earned_points, explanation = calculate_points(
                center_x, center_y, arrow_x, arrow_y, rings, points
            )
            
            # Palyginimas su tolerancija (dėl slankiojo kablelio tikslumo)
            passed = abs(earned_points - expected) < tolerance
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            print(f"      Tikėtasi: {expected}, Gauta: {earned_points:.6f}")
            if not passed:
                print(f"      Skirtumas: {abs(earned_points - expected):.6f}")
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
    print("🎯 SANTA'S MAGICAL ARCHERY CHALLENGE")
    print("=" * 60)
    print("\nŠi programa apskaičiuoja, kiek taškų pelnė elfas")
    print("pagal strėlės nusileidimo vietą ant taikinio.\n")
    
    try:
        # Gauname taikinio centro koordinates
        print("📍 Taikinio centro koordinatės:")
        center_x = get_float_input("  X koordinatė: ", "Centro X", allow_negative=True)
        center_y = get_float_input("  Y koordinatė: ", "Centro Y", allow_negative=True)
        
        # Gauname strėlės nusileidimo koordinates
        print("\n🏹 Strėlės nusileidimo koordinatės:")
        arrow_x = get_float_input("  X koordinatė: ", "Strėlės X", allow_negative=True)
        arrow_y = get_float_input("  Y koordinatė: ", "Strėlės Y", allow_negative=True)
        
        # Gauname žiedų konfigūraciją
        rings, points = get_rings_input()
        
        # Apskaičiuojame taškus
        earned_points, explanation = calculate_points(
            center_x, center_y, arrow_x, arrow_y, rings, points
        )
        
        # Atvaizduojame rezultatus
        display_results(
            center_x, center_y, arrow_x, arrow_y, 
            rings, points, earned_points, explanation
        )
        
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
