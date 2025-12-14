"""
Santa's Spinning Clock Mystery Solution

Užduotis: Nustatyti, kokį laiką rodys laikrodis po to, kai minutinė rodyklė 
atliks vieną pilną apsisukimą (360°).

Sprendimas: Vienas pilnas apsisukimas = praeina 60 minučių realaus laiko.
"""


def calculate_time_after_rotation(hours, minutes):
    """
    Apskaičiuoja laiką po minutinės rodyklės pilno apsisukimo.
    
    Algoritmas:
    - Vienas pilnas apsisukimas prilygsta 60 minučių
    - Pridedame 60 minučių prie esamo laiko
    - Jei valandos viršija 24, atliekame modulio operaciją
    
    Args:
        hours (int): Dabartinės valandos (0-23)
        minutes (int): Dabartinės minutės (0-59)
    
    Returns:
        tuple: (naujos_valandos, naujos_minutės)
    
    Raises:
        ValueError: Jei valandos arba minutės yra neleistiname diapazone
    """
    # Validacija įvesties duomenų
    if not isinstance(hours, int) or not isinstance(minutes, int):
        raise ValueError("Valandos ir minutės turi būti sveikieji skaičiai")
    
    if not (0 <= hours <= 23):
        raise ValueError(f"Valandos turi būti tarp 0 ir 23, gauta: {hours}")
    
    if not (0 <= minutes <= 59):
        raise ValueError(f"Minutės turi būti tarp 0 ir 59, gauta: {minutes}")
    
    # Vienas pilnas apsisukimas = 60 minučių
    # Optimizuota: kadangi visada pridedame tiksliai 60 minučių,
    # naujos minutės bus tos pačios, o valandos padidės 1
    new_minutes = minutes  # (minutes + 60) % 60 = minutes, nes minutes < 60
    new_hours = (hours + 1) % 24  # Pridedame 1 valandą ir apdorojame perpildymą
    
    return new_hours, new_minutes


def format_time_24h(hours, minutes):
    """
    Formatuoja laiką 24 valandų formatu (HH:MM).
    
    Args:
        hours (int): Valandos (0-23)
        minutes (int): Minutės (0-59)
    
    Returns:
        str: Suformatuotas laikas (pvz., "13:30")
    """
    return f"{hours:02d}:{minutes:02d}"


def format_time_12h(hours, minutes):
    """
    Formatuoja laiką 12 valandų formatu su AM/PM.
    
    Args:
        hours (int): Valandos (0-23)
        minutes (int): Minutės (0-59)
    
    Returns:
        str: Suformatuotas laikas (pvz., "1:30 PM")
    """
    if hours == 0:
        display_hours = 12
        period = "AM"
    elif hours == 12:
        display_hours = 12
        period = "PM"
    elif hours < 12:
        display_hours = hours
        period = "AM"
    else:  # hours > 12
        display_hours = hours - 12
        period = "PM"
    
    return f"{display_hours}:{minutes:02d} {period}"


def get_valid_input(prompt, min_value, max_value, input_name):
    """
    Gauna ir validuoja vartotojo įvestį su pakartotiniais bandymais.
    
    Args:
        prompt (str): Užklausos tekstas
        min_value (int): Mažiausia leistina reikšmė
        max_value (int): Didžiausia leistina reikšmė
        input_name (str): Įvesties pavadinimas (naudojamas klaidų pranešimuose)
    
    Returns:
        int: Validuota reikšmė
    """
    max_attempts = 3
    attempt = 0
    
    while attempt < max_attempts:
        try:
            value = input(prompt).strip()
            
            # Patikrinimas, ar įvestis nėra tuščia
            if not value:
                raise ValueError(f"{input_name} negali būti tuščias. Įveskite skaičių tarp {min_value} ir {max_value}.")
            
            # Konvertavimas į sveikąjį skaičių
            value = int(value)
            
            # Diapazono patikrinimas
            if not (min_value <= value <= max_value):
                raise ValueError(
                    f"Neteisingas {input_name.lower()} formatas. "
                    f"Įveskite skaičių tarp {min_value} ir {max_value}. "
                    f"Gauta reikšmė: {value}"
                )
            
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


def display_results(original_hours, original_minutes, new_hours, new_minutes):
    """
    Atvaizduoja rezultatus aiškiai ir informatyviai.
    
    Args:
        original_hours (int): Pradinės valandos
        original_minutes (int): Pradinės minutės
        new_hours (int): Naujos valandos
        new_minutes (int): Naujos minutės
    """
    print("\n" + "=" * 50)
    print("📊 REZULTATAI")
    print("=" * 50)
    print(f"Pradinis laikas:     {format_time_24h(original_hours, original_minutes)} "
          f"({format_time_12h(original_hours, original_minutes)})")
    print(f"Po pilno apsisukimo: {format_time_24h(new_hours, new_minutes)} "
          f"({format_time_12h(new_hours, new_minutes)})")
    print("=" * 50)
    
    # Papildomas paaiškinimas
    print("\n💡 Paaiškinimas:")
    print("   Vienas pilnas minutinės rodyklės apsisukimas (360°) prilygsta")
    print("   60 minučių realaus laiko. Todėl:")
    print(f"   {original_hours} val. {original_minutes} min. + 60 min. = "
          f"{new_hours} val. {new_minutes} min.")
    
    # Jei perėjome į kitą dieną
    if new_hours < original_hours or (new_hours == 0 and original_hours == 23):
        print("   ⏰ Pastaba: Laikrodis perėjo į kitą dieną!")


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        (12, 0, 13, 0, "12:00 -> 13:00 (1:00 PM)"),
        (12, 30, 13, 30, "12:30 -> 13:30 (1:30 PM)"),
        (23, 45, 0, 45, "23:45 -> 00:45 (12:45 AM, kita diena)"),
        (0, 0, 1, 0, "00:00 -> 01:00 (12:00 AM -> 1:00 AM)"),
        (11, 59, 12, 59, "11:59 -> 12:59 (11:59 AM -> 12:59 PM)"),
        (5, 15, 6, 15, "05:15 -> 06:15 (5:15 AM -> 6:15 AM)"),
        (15, 30, 16, 30, "15:30 -> 16:30 (3:30 PM -> 4:30 PM)"),
        (23, 0, 0, 0, "23:00 -> 00:00 (11:00 PM -> 12:00 AM, kita diena)"),
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 60)
    
    passed_count = 0
    failed_count = 0
    
    for hours, minutes, expected_hours, expected_minutes, description in test_cases:
        try:
            new_hours, new_minutes = calculate_time_after_rotation(hours, minutes)
            passed = (new_hours == expected_hours and new_minutes == expected_minutes)
            
            if passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {description}")
            print(f"      Įvestis: {format_time_24h(hours, minutes)} | "
                  f"Tikėtasi: {format_time_24h(expected_hours, expected_minutes)} | "
                  f"Gauta: {format_time_24h(new_hours, new_minutes)}")
            
        except Exception as e:
            print(f"❌ ERROR | {description}")
            print(f"      Klaida: {e}")
            failed_count += 1
    
    print("=" * 60)
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
    print("=" * 50)
    print("🎅 SANTA'S SPINNING CLOCK MYSTERY")
    print("=" * 50)
    print("\nŠi programa apskaičiuoja, kokį laiką rodys laikrodis")
    print("po to, kai minutinė rodyklė atliks vieną pilną apsisukimą.\n")
    
    try:
        # Gauname ir validuojame vartotojo įvestį
        hours = get_valid_input(
            "⏰ Įveskite dabartines valandas (0-23): ",
            0, 23, "Valandos"
        )
        
        minutes = get_valid_input(
            "⏰ Įveskite dabartines minutes (0-59): ",
            0, 59, "Minutės"
        )
        
        # Apskaičiuojame naują laiką
        new_hours, new_minutes = calculate_time_after_rotation(hours, minutes)
        
        # Atvaizduojame rezultatus
        display_results(hours, minutes, new_hours, new_minutes)
        
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
