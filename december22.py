"""
Kalėdų Eglutės Teksto Formatuotojas

Programa pertvarko tekstą į "kalėdų eglutės" formą:
- Eilutės pertvarkomos su didėjančiu žodžių skaičiumi (1, 2, 3, ...)
- Eilutės kaitaliojamos tarp kairiojo ir dešiniojo lygiavimo
- Visos eilutės lygiuojamos pagal bendrą vertikalią ašį (kamieną)

Apribojimai:
- Pertvarkytas tekstas turi turėti ne daugiau nei 100 eilučių
- Kiekviena originali įvesties eilutė gali turėti iki 255 simbolių
"""

# Konstantos
MAX_OUTPUT_LINES = 100
MAX_INPUT_LINE_LENGTH = 255


def split_into_words(line):
    """
    Padalina eilutę į žodžius, paliekant skyrybos ženklus prie žodžių.
    
    Pagal užduoties reikalavimus, skyrybos ženklai (pvz. , . ! ? : ;),
    kurie pagal rašymo taisykles yra pritvirtinti prie žodžio pabaigos,
    laikomi žodžio dalimi.
    
    Args:
        line (str): Įvesties teksto eilutė
        
    Returns:
        list: Žodžių sąrašas (su skyrybos ženklais)
    """
    # Padalinimas pagal tarpus - skyrybos ženklai lieka prie žodžių
    words = line.split()
    return words


def rearrange_words(words):
    """
    Pertvarko žodžius į eilutes su didėjančiu žodžių skaičiumi (1, 2, 3, ...).
    
    Algoritmas:
    - 1-oji eilutė turi 1 žodį
    - 2-oji eilutė turi 2 žodžius
    - 3-oji eilutė turi 3 žodžius
    - ir t.t.
    - Jei liko nepakanka žodžių pilnai eilutei, likę žodžiai sudaro paskutinę
      (nepilną) eilutę
    
    Args:
        words (list): Žodžių sąrašas
        
    Returns:
        list: Pertvarkytų eilučių sąrašas (kiekviena eilutė yra žodžių eilutė)
    """
    rearranged = []
    word_index = 0
    line_number = 1
    
    while word_index < len(words):
        # Nustatome, kiek žodžių turėtų būti šioje eilutėje
        words_needed = line_number
        
        # Paimame žodžius šiai eilutei
        line_words = words[word_index:word_index + words_needed]
        
        # Sujungiame žodžius su tarpais
        line_text = " ".join(line_words)
        rearranged.append(line_text)
        
        # Perkeliame prie kito žodžių rinkinio
        word_index += words_needed
        line_number += 1
    
    return rearranged


def process_all_lines(input_lines):
    """
    Apdoroja visas įvesties eilutes ir pertvarko jas į eglutės formatą.
    
    Kiekviena įvesties eilutė apdorojama atskirai pagal užduoties reikalavimus.
    
    Args:
        input_lines (list): Įvesties teksto eilučių sąrašas
        
    Returns:
        list: Visų pertvarkytų eilučių sąrašas iš visų įvesties eilučių
        
    Raises:
        ValueError: Jei pertvarkytų eilučių skaičius viršija MAX_OUTPUT_LINES
    """
    all_rearranged = []
    
    for line in input_lines:
        words = split_into_words(line)
        if words:  # Apdorojame tik netuščias eilutes
            rearranged = rearrange_words(words)
            all_rearranged.extend(rearranged)
            
            # Tikriname apribojimą: ne daugiau nei 100 eilučių
            if len(all_rearranged) > MAX_OUTPUT_LINES:
                raise ValueError(
                    f"Pertvarkytas tekstas turi per daug eilučių: {len(all_rearranged)}. "
                    f"Maksimalus leistinas skaičius: {MAX_OUTPUT_LINES}."
                )
    
    return all_rearranged


def find_max_length(lines):
    """
    Randa maksimalų simbolių skaičių tarp visų eilučių.
    
    Šis ilgis naudojamas kaip ašies (kamieno) padėtis - visos eilutės
    lygiuojamos pagal šią vertikalią ašį.
    
    Args:
        lines (list): Teksto eilučių sąrašas
        
    Returns:
        int: Maksimalus eilutės ilgis (simbolių skaičius)
    """
    if not lines:
        return 0
    return max(len(line) for line in lines)


def format_tree_lines(rearranged_lines):
    """
    Formatuoja pertvarkytas eilutes į kalėdų eglutės formą su kaitaliojamu lygiavimu.
    
    Visos eilutės išplečiamos iki max_length pločio. Ašis (kamienas) yra stulpelyje max_length.
    - Kairiojo lygiavimo eilutės (nelyginės): tekstas kairėje, tarpai dešinėje (baigiasi ties ašimi)
    - Dešiniojo lygiavimo eilutės (lyginės): tarpai kairėje, tekstas dešinėje (baigiasi ties ašimi)
    
    Pagal užduoties reikalavimus, eilutės kaitaliojamos:
    - 1-oji eilutė - kairiojo lygiavimo
    - 2-oji eilutė - dešiniojo lygiavimo
    - 3-oji eilutė - kairiojo lygiavimo
    - ir t.t.
    
    Args:
        rearranged_lines (list): Pertvarkytų teksto eilučių sąrašas
        
    Returns:
        list: Suformatuotų eilučių sąrašas, paruoštas išvedimui
    """
    if not rearranged_lines:
        return []
    
    # Randame maksimalų ilgį (ašies padėtis)
    max_length = find_max_length(rearranged_lines)
    
    formatted = []
    
    for i, line in enumerate(rearranged_lines):
        line_index = i + 1  # 1-bazinis indeksas
        
        if line_index % 2 == 1:  # Nelyginės eilutės: kairiojo lygiavimo (baigiasi ties ašimi)
            # Pridedame tarpus dešinėje, kad pasiektume ašį
            formatted_line = line + " " * (max_length - len(line))
        else:  # Lyginės eilutės: dešiniojo lygiavimo (baigiasi ties ašimi)
            # Pridedame tarpus kairėje, kad tekstas baigtųsi ties ašimi
            formatted_line = " " * (max_length - len(line)) + line
        
        formatted.append(formatted_line)
    
    return formatted


def validate_input(n, input_lines):
    """
    Validuoja įvesties duomenis pagal užduoties apribojimus.
    
    Args:
        n (int): Eilučių skaičius
        input_lines (list): Įvesties eilučių sąrašas
        
    Raises:
        ValueError: Jei įvesties duomenys neatitinka reikalavimų
    """
    if n < 0:
        raise ValueError(
            f"Eilučių skaičius negali būti neigiamas. Gauta: {n}."
        )
    
    if len(input_lines) != n:
        raise ValueError(
            f"Nesutampa eilučių skaičius: nurodyta {n}, bet nuskaityta {len(input_lines)}. "
            f"Patikrinkite, ar visos eilutės buvo įvestos teisingai."
        )
    
    # Tikriname kiekvienos eilutės ilgį
    for i, line in enumerate(input_lines, start=1):
        if len(line) > MAX_INPUT_LINE_LENGTH:
            raise ValueError(
                f"Eilutė {i} per ilga: {len(line)} simbolių. "
                f"Maksimalus leistinas ilgis: {MAX_INPUT_LINE_LENGTH} simbolių."
            )


def main():
    """
    Pagrindinė funkcija, kuri apdoroja įvestį ir išveda kalėdų eglutę.
    
    Programa:
    1. Nuskaito eilučių skaičių n
    2. Nuskaito n teksto eilučių
    3. Validuoja įvesties duomenis
    4. Pertvarko tekstą į eglutės formą
    5. Išveda rezultatą
    """
    input_lines = []
    
    # Nuskaitome eilučių skaičių
    n_input = None
    try:
        n_input = input().strip()
        if not n_input:
            print("Klaida: Nepateiktas eilučių skaičius. "
                  "Pirmoje eilutėje turite įvesti teigiamą sveikąjį skaičių.")
            return
        n = int(n_input)
    except ValueError:
        error_msg = f"Klaida: Nepavyko nuskaityti eilučių skaičiaus. " \
                   f"Įvestis turi būti teigiamas sveikasis skaičius."
        if n_input is not None:
            error_msg += f" Gauta: '{n_input}'"
        print(error_msg)
        return
    except EOFError:
        print("Klaida: Netikėta įvesties pabaiga. "
              "Patikrinkite, ar visi duomenys buvo teisingai įvesti.")
        return
    
    if n == 0:
        print("Klaida: Eilučių skaičius negali būti 0. "
              "Įveskite teigiamą sveikąjį skaičių.")
        return
    
    # Nuskaitome n eilučių
    try:
        for i in range(n):
            line = input().strip()
            input_lines.append(line)
    except EOFError:
        print(f"Klaida: Netikėta įvesties pabaiga. "
              f"Tikėtasi {n} eilučių, bet nuskaityta tik {len(input_lines)}. "
              f"Patikrinkite, ar visos eilutės buvo įvestos.")
        return
    
    # Validuojame įvesties duomenis
    try:
        validate_input(n, input_lines)
    except ValueError as e:
        print(f"Klaida: Neteisingi įvesties duomenys. {e}")
        return
    
    # Apdorojame visas eilutes
    try:
        rearranged_lines = process_all_lines(input_lines)
    except ValueError as e:
        print(f"Klaida: {e}")
        return
    
    # Formatuojame į eglutės formą
    formatted_lines = format_tree_lines(rearranged_lines)
    
    # Išvedame eglutę
    if not formatted_lines:
        print("Perspėjimas: Po apdorojimo nebuvo gauta jokių eilučių. "
              "Patikrinkite, ar įvesties eilutėse yra žodžių.")
        return
    
    for line in formatted_lines:
        print(line)


if __name__ == "__main__":
    main()

