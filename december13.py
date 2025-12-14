"""
Christmas School - Student Name Magic Solution

Užduotis: Suskaičiuoti ir išvardinti visas mergaites iš studentų sąrašo.

Taisyklė: Mergaičių vardai baigiasi raide 'a', berniukų - ne.

Formato reikalavimai:
- Įvestis: "LastName FirstName"
- Išvestis: pirmoje eilutėje - mergaičių skaičius
- Kitos eilutės: kiekvienos mergaitės pilnas vardas tokiu pačiu formatu

Sprendimas:
1. Parsiname kiekvieną studento vardą
2. Tikriname, ar vardas baigiasi raide 'a'
3. Skaičiuojame ir išvardiname mergaites
"""

from typing import List, Tuple


def parse_student_name(full_name):
    """
    Parsina studento pilną vardą į pavardę ir vardą.
    
    Args:
        full_name (str): Pilnas vardas formatu "LastName FirstName"
    
    Returns:
        tuple: (pavardė, vardas) arba None, jei formatas neteisingas
    
    Raises:
        ValueError: Jei vardo formatas neteisingas
    """
    if not isinstance(full_name, str):
        raise ValueError(f"Vardas turi būti eilutė (string), gauta: {type(full_name)}")
    
    full_name = full_name.strip()
    
    if not full_name:
        raise ValueError("Vardas negali būti tuščias")
    
    # Skirstome pagal pirmą tarpą
    parts = full_name.split(None, 1)  # Maksimaliai 2 dalys
    
    if len(parts) != 2:
        raise ValueError(
            f"Neteisingas vardo formatas: '{full_name}'. "
            f"Tikėtasi: 'LastName FirstName' (pvz., 'Petraitis Rokas')"
        )
    
    last_name, first_name = parts
    
    if not last_name or not first_name:
        raise ValueError(
            f"Neteisingas vardo formatas: '{full_name}'. "
            f"Pavardė ir vardas negali būti tuščios"
        )
    
    return last_name.strip(), first_name.strip()


def is_girl(first_name):
    """
    Tikrina, ar studentas yra mergaitė pagal vardo pabaigą.
    
    Taisyklė: Mergaičių vardai baigiasi raide 'a' (arba 'ė', 'ą', 'ę' lietuviškoms raidėms).
    Tačiau pagal užduotį, tikriname tik 'a'.
    
    Args:
        first_name (str): Studento vardas
    
    Returns:
        bool: True, jei mergaitė (vardas baigiasi 'a'), False - berniukas
    """
    if not isinstance(first_name, str) or not first_name:
        return False
    
    # Pašaliname tarpus ir konvertuojame į mažąsias raides
    first_name = first_name.strip().lower()
    
    # Tikriname, ar baigiasi raide 'a'
    return first_name.endswith('a')


def find_girls(students):
    """
    Randa visas mergaites iš studentų sąrašo.
    
    Algoritmas:
    1. Kiekvienam studentui parsinuojame vardą
    2. Tikriname, ar vardas baigiasi 'a'
    3. Jei taip - pridedame prie mergaičių sąrašo
    
    Args:
        students (list): Studentų sąrašas formatu ["LastName FirstName", ...]
    
    Returns:
        tuple: (mergaičių_sąrašas, klaidos_sąrašas)
            - mergaičių_sąrašas: pilni vardai mergaičių
            - klaidos_sąrašas: sąrašas klaidų, jei kai kurie vardai neteisingi
    
    Raises:
        ValueError: Jei įvestis nėra sąrašas
    """
    if not isinstance(students, (list, tuple)):
        raise ValueError(f"Įvestis turi būti sąrašas (list) arba tuple, gauta: {type(students)}")
    
    girls = []
    errors = []
    
    for i, full_name in enumerate(students):
        try:
            last_name, first_name = parse_student_name(full_name)
            
            if is_girl(first_name):
                girls.append(full_name.strip())
                
        except ValueError as e:
            errors.append(f"Eilutė {i+1}: '{full_name}' - {e}")
        except Exception as e:
            errors.append(f"Eilutė {i+1}: '{full_name}' - Netikėta klaida: {e}")
    
    return girls, errors


def format_output(girls):
    """
    Formatuoja išvestį pagal užduoties reikalavimus.
    
    Formatas:
    - Pirmoje eilutėje: mergaičių skaičius
    - Kitos eilutės: kiekvienos mergaitės pilnas vardas
    
    Args:
        girls (list): Mergaičių pilnų vardų sąrašas
    
    Returns:
        str: Suformatuota išvestis
    """
    output_lines = [str(len(girls))]
    
    for girl_name in girls:
        output_lines.append(girl_name)
    
    return "\n".join(output_lines)


def get_students_input():
    """
    Gauna studentų sąrašą iš vartotojo su validacija.
    
    Returns:
        list: Studentų sąrašas
    """
    print("\n📝 Įveskite studentų vardus:")
    print("   Formatas: 'LastName FirstName' (po vieną eilutėje)")
    print("   Arba atskirkite kableliais: 'Petraitis Rokas, Augė Artūras, ...'")
    print("   Arba įveskite 'default', kad naudotumėte pavyzdinius duomenis")
    
    user_input = input("Studentai: ").strip()
    
    if user_input.lower() == 'default':
        return [
            "Petraitis Rokas",
            "Augė Artūras",
            "Mikalauskaitė Aušra",
            "Šlivka Donatas",
            "Stakėnaitė Ieva",
            "Skrėbė Domas",
            "Bruzgaitė Akvilė"
        ]
    
    # Skirstome pagal kablelius arba naujas eilutes
    if ',' in user_input:
        students = [name.strip() for name in user_input.split(',') if name.strip()]
    elif '\n' in user_input:
        students = [name.strip() for name in user_input.split('\n') if name.strip()]
    else:
        # Jei tik vienas vardas
        if user_input.strip():
            students = [user_input.strip()]
        else:
            students = []
    
    if not students:
        raise ValueError("Nepavyko nuskaityti studentų. Įveskite vardus formatu 'LastName FirstName'.")
    
    return students


def display_results(students, girls, errors):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        students (list): Pradiniai studentai
        girls (list): Mergaičių sąrašas
        errors (list): Klaidų sąrašas
    """
    print("\n" + "=" * 60)
    print("📊 REZULTATAI")
    print("=" * 60)
    print(f"Visų studentų skaičius: {len(students)}")
    print(f"Mergaičių skaičius: {len(girls)}")
    print(f"Berniukų skaičius: {len(students) - len(girls) - len(errors)}")
    
    if errors:
        print(f"\n⚠️  Rastos klaidos ({len(errors)}):")
        for error in errors:
            print(f"   {error}")
    
    print("\n" + "=" * 60)
    print("📋 IŠVESTIS (pagal užduoties formatą):")
    print("=" * 60)
    print(format_output(girls))
    
    if girls:
        print("\n" + "=" * 60)
        print("👧 MERGAIČIŲ SĄRAŠAS:")
        print("=" * 60)
        for i, girl_name in enumerate(girls, 1):
            last_name, first_name = parse_student_name(girl_name)
            print(f"{i}. {girl_name} (vardas: '{first_name}')")
    
    print("\n💡 Paaiškinimas:")
    print("   Mergaičių vardai baigiasi raide 'a'.")
    print("   Programa tikrina kiekvieno studento vardą ir")
    print("   identifikuoja mergaites pagal šią taisyklę.")


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas",
            "input": [
                "Petraitis Rokas",
                "Augė Artūras",
                "Mikalauskaitė Aušra",
                "Šlivka Donatas",
                "Stakėnaitė Ieva",
                "Skrėbė Domas",
                "Bruzgaitė Akvilė"
            ],
            "expected_count": 3,
            "expected_girls": [
                "Mikalauskaitė Aušra",
                "Stakėnaitė Ieva",
                "Bruzgaitė Akvilė"
            ],
            "description": "Standartinis testas su 7 studentais"
        },
        {
            "name": "Tik mergaitės",
            "input": [
                "Petraitytė Ana",
                "Jonaitė Ieva",
                "Kazlienė Rasa"
            ],
            "expected_count": 3,
            "expected_girls": [
                "Petraitytė Ana",
                "Jonaitė Ieva",
                "Kazlienė Rasa"
            ],
            "description": "Visi studentai yra mergaitės"
        },
        {
            "name": "Tik berniukai",
            "input": [
                "Petraitis Rokas",
                "Jonaitis Tomas",
                "Kazlauskas Domas"
            ],
            "expected_count": 0,
            "expected_girls": [],
            "description": "Visi studentai yra berniukai"
        },
        {
            "name": "Vienas studentas - mergaitė",
            "input": ["Jonaitė Ieva"],
            "expected_count": 1,
            "expected_girls": ["Jonaitė Ieva"],
            "description": "Tik viena mergaitė"
        },
        {
            "name": "Vienas studentas - berniukas",
            "input": ["Petraitis Rokas"],
            "expected_count": 0,
            "expected_girls": [],
            "description": "Tik vienas berniukas"
        },
        {
            "name": "Tuščias sąrašas",
            "input": [],
            "expected_count": 0,
            "expected_girls": [],
            "description": "Tuščias įvesties sąrašas"
        },
        {
            "name": "Mišrus sąrašas",
            "input": [
                "Petraitis Rokas",
                "Jonaitė Ieva",
                "Kazlauskas Domas",
                "Stakėnaitė Aušra",
                "Mikalauskas Tomas"
            ],
            "expected_count": 2,
            "expected_girls": [
                "Jonaitė Ieva",
                "Stakėnaitė Aušra"
            ],
            "description": "Mišrus sąrašas su tarpais"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    
    for test in test_cases:
        try:
            students = test["input"]
            girls, errors = find_girls(students)
            
            # Patikrinimas: mergaičių skaičius
            count = len(girls)
            expected_count = test["expected_count"]
            
            # Patikrinimas: mergaičių sąrašas (turi būti tokie patys)
            expected_girls = test["expected_girls"]
            
            # Palyginimas (ignoruojame eiliškumą, bet užduotyje jis svarbus)
            girls_set = set(girls)
            expected_set = set(expected_girls)
            
            passed = (
                count == expected_count and
                girls_set == expected_set and
                len(errors) == 0  # Neturėtų būti klaidų testuose
            )
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            print(f"      Įvestis: {students}")
            print(f"      Mergaičių skaičius: {count} (tikėtasi: {expected_count})")
            print(f"      Mergaitės: {girls} (tikėtasi: {expected_girls})")
            
            if errors:
                print(f"      ⚠️  Klaidos: {errors}")
            
            if not passed:
                if count != expected_count:
                    print(f"      ❌ Neteisingas mergaičių skaičius!")
                if girls_set != expected_set:
                    print(f"      ❌ Neteisingas mergaičių sąrašas!")
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
    print("🎓 CHRISTMAS SCHOOL - STUDENT NAME MAGIC")
    print("=" * 60)
    print("\nŠi programa suskaičiuoja ir išvardina visas mergaites")
    print("iš studentų sąrašo pagal taisyklę:")
    print("Mergaičių vardai baigiasi raide 'a'.\n")
    
    try:
        # Gauname studentų sąrašą
        students = get_students_input()
        
        if not students:
            print("❌ Klaida: Nepavyko nuskaityti studentų.")
            return False
        
        # Randame mergaites
        girls, errors = find_girls(students)
        
        # Atvaizduojame rezultatus
        display_results(students, girls, errors)
        
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

