"""
Santa's Magic Word Workshop - Anagram Groups Solution

Užduotis: Sugrupuoti visus Kalėdų žodžius, kurie yra anagramos vienas kito.

Anagrama: Du žodžiai yra anagramos, jei jie sudaryti iš tų pačių raidžių,
tik skirtinga tvarka.

Sprendimas:
1. Kiekvienam žodžiui sukuriame "parašą" - surūšiuotas raidės
2. Žodžiai su tuo pačiu parašu yra anagramos
3. Grupuojame juos kartu
4. (Bonus) Rūšiuojame grupes pagal dydį ir žodžius abėcėlės tvarka
"""

from collections import defaultdict
from typing import List, List


def create_signature(word):
    """
    Sukuria žodžio parašą (signature) surūšiuojant jo raides.
    
    Parašas naudojamas anagramų identifikavimui - žodžiai su tuo pačiu
    parašu yra anagramos.
    
    Args:
        word (str): Žodis, kuriam sukurti parašą
    
    Returns:
        str: Surūšiuotos žodžio raidės (parašas)
    
    Example:
        create_signature("eat") -> "aet"
        create_signature("tea") -> "aet"
        create_signature("bat") -> "abt"
    """
    if not isinstance(word, str):
        raise ValueError(f"Žodis turi būti eilutė (string), gauta: {type(word)}")
    
    # Konvertuojame į mažąsias raides ir rūšiuojame
    return ''.join(sorted(word.lower()))


def group_anagrams(words, sort_groups=True, sort_by_size=True):
    """
    Grupuoja žodžius į anagramų grupes.
    
    Algoritmas:
    1. Kiekvienam žodžiui sukuriame parašą (surūšiuotos raidės)
    2. Naudojame žodyną, kur raktas yra parašas, reikšmė - žodžių sąrašas
    3. Visi žodžiai su tuo pačiu parašu yra anagramos
    4. Grąžiname grupių sąrašą
    
    Args:
        words (list): Žodžių sąrašas
        sort_groups (bool): Ar rūšiuoti žodžius kiekvienoje grupėje abėcėlės tvarka
        sort_by_size (bool): Ar rūšiuoti grupes pagal dydį (didžiausios pirmos)
    
    Returns:
        list: Grupių sąrašas, kur kiekviena grupė yra anagramų sąrašas
    
    Raises:
        ValueError: Jei įvestis nėra sąrašas arba yra netinkami duomenys
    
    Example:
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    # Validacija įvesties duomenų
    if not isinstance(words, (list, tuple)):
        raise ValueError(f"Įvestis turi būti sąrašas (list) arba tuple, gauta: {type(words)}")
    
    if len(words) == 0:
        return []
    
    # Naudojame defaultdict, kad automatiškai sukurtume naują sąrašą
    anagram_groups = defaultdict(list)
    
    # Grupuojame žodžius pagal jų parašą
    for word in words:
        # Validacija: patikriname, ar žodis yra eilutė
        if not isinstance(word, str):
            raise ValueError(f"Visi žodžiai turi būti eilutės (string), rasta: {type(word)} - {word}")
        
        # Sukuriame parašą ir pridedame žodį į atitinkamą grupę
        signature = create_signature(word)
        anagram_groups[signature].append(word)
    
    # Konvertuojame žodyną į sąrašą grupių
    result = list(anagram_groups.values())
    
    # (Bonus) Rūšiuojame žodžius kiekvienoje grupėje abėcėlės tvarka
    if sort_groups:
        result = [sorted(group) for group in result]
    
    # (Bonus) Rūšiuojame grupes pagal dydį (didžiausios pirmos)
    if sort_by_size:
        result.sort(key=len, reverse=True)
    
    return result


def format_output(groups):
    """
    Formatuoja išvestį gražiai ir aiškiai.
    
    Args:
        groups (list): Anagramų grupių sąrašas
    
    Returns:
        str: Suformatuota išvestis
    """
    if not groups:
        return "[]"
    
    lines = ["["]
    for i, group in enumerate(groups):
        comma = "," if i < len(groups) - 1 else ""
        lines.append(f"  {group}{comma}")
    lines.append("]")
    
    return "\n".join(lines)


def get_words_input():
    """
    Gauna žodžių sąrašą iš vartotojo su validacija.
    
    Returns:
        list: Žodžių sąrašas
    """
    print("\n📝 Įveskite žodžius (atskirkite kableliais arba po vieną eilutėje):")
    print("   Pavyzdys: eat, tea, tan, ate, nat, bat")
    print("   Arba įveskite 'default', kad naudotumėte pavyzdinius duomenis")
    
    user_input = input("Žodžiai: ").strip()
    
    if user_input.lower() == 'default':
        return ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    # Skirstome žodžius pagal kablelius arba tarpus
    if ',' in user_input:
        words = [word.strip() for word in user_input.split(',') if word.strip()]
    else:
        words = [word.strip() for word in user_input.split() if word.strip()]
    
    if not words:
        raise ValueError("Nepavyko nuskaityti žodžių. Įveskite žodžius atskirdami kableliais.")
    
    return words


def display_results(words, groups):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        words (list): Pradiniai žodžiai
        groups (list): Anagramų grupių sąrašas
    """
    print("\n" + "=" * 60)
    print("📊 REZULTATAI")
    print("=" * 60)
    print(f"Pradiniai žodžiai ({len(words)}): {words}")
    print(f"\nAnagramų grupių skaičius: {len(groups)}")
    
    print("\n📦 Anagramų grupės:")
    print("=" * 60)
    
    for i, group in enumerate(groups, 1):
        print(f"\nGrupė {i} ({len(group)} žodžiai):")
        print(f"  {group}")
        
        # Rodo parašą (surūšiuotas raidės)
        if group:
            signature = create_signature(group[0])
            print(f"  Parašas: '{signature}' (surūšiuotos raidės)")
    
    print("\n" + "=" * 60)
    print("💡 Paaiškinimas:")
    print("   Žodžiai, turintys tą patį parašą (surūšiuotas raidės),")
    print("   yra anagramos ir yra sugrupuoti kartu.")
    
    # Rodo Python formato išvestį
    print("\n📋 Python formato išvestis:")
    print(format_output(groups))


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas",
            "input": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected_groups": 3,
            "expected_sizes": [3, 2, 1],
            "description": "Standartinis testas su 6 žodžiais"
        },
        {
            "name": "Vienas žodis",
            "input": ["hello"],
            "expected_groups": 1,
            "expected_sizes": [1],
            "description": "Tik vienas žodis"
        },
        {
            "name": "Visi žodžiai yra anagramos",
            "input": ["listen", "silent", "enlist"],
            "expected_groups": 1,
            "expected_sizes": [3],
            "description": "Visi žodžiai yra anagramos vienas kito"
        },
        {
            "name": "Jokių anagramų",
            "input": ["cat", "dog", "bird"],
            "expected_groups": 3,
            "expected_sizes": [1, 1, 1],
            "description": "Jokie žodžiai nėra anagramos"
        },
        {
            "name": "Didžiosios ir mažosios raidės",
            "input": ["Eat", "TEA", "eat", "tea"],
            "expected_groups": 1,
            "expected_sizes": [4],
            "description": "Anagramos su skirtingomis raidžių didžiosiomis/mažosiomis"
        },
        {
            "name": "Tuščias sąrašas",
            "input": [],
            "expected_groups": 0,
            "expected_sizes": [],
            "description": "Tuščias įvesties sąrašas"
        },
        {
            "name": "Sudėtingesnis testas",
            "input": ["listen", "silent", "enlist", "cat", "act", "tac", "dog"],
            "expected_groups": 3,
            "expected_sizes": [3, 3, 1],
            "description": "Keli anagramų poros"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    
    for test in test_cases:
        try:
            words = test["input"]
            groups = group_anagrams(words, sort_groups=True, sort_by_size=True)
            
            # Patikrinimas: grupių skaičius
            groups_count = len(groups)
            expected_groups = test["expected_groups"]
            
            # Patikrinimas: grupių dydžiai
            group_sizes = sorted([len(group) for group in groups], reverse=True)
            expected_sizes = test["expected_sizes"]
            
            # Patikrinimas: ar visi žodžiai yra rezultate
            all_result_words = [word for group in groups for word in group]
            input_sorted = sorted(words)
            result_sorted = sorted(all_result_words)
            
            passed = (
                groups_count == expected_groups and
                group_sizes == expected_sizes and
                input_sorted == result_sorted
            )
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            print(f"      Įvestis: {words}")
            print(f"      Grupių skaičius: {groups_count} (tikėtasi: {expected_groups})")
            print(f"      Grupių dydžiai: {group_sizes} (tikėtasi: {expected_sizes})")
            
            if not passed:
                print(f"      Gautos grupės: {groups}")
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
    print("🎅 SANTA'S MAGIC WORD WORKSHOP - ANAGRAM GROUPS")
    print("=" * 60)
    print("\nŠi programa grupuoja Kalėdų žodžius į anagramų grupes.")
    print("Anagramos - tai žodžiai, sudaryti iš tų pačių raidžių,")
    print("tik skirtinga tvarka.\n")
    
    try:
        # Gauname žodžių sąrašą
        words = get_words_input()
        
        if not words:
            print("❌ Klaida: Nepavyko nuskaityti žodžių.")
            return False
        
        # Grupuojame anagramas
        groups = group_anagrams(words, sort_groups=True, sort_by_size=True)
        
        # Atvaizduojame rezultatus
        display_results(words, groups)
        
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
