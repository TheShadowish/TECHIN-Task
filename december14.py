"""
Santa's Gift Cart Engine Solution

Užduotis: Implementuoti dovanų krepšelio sistemą su dovanų pridėjimu,
pašalinimu, kainos skaičiavimu ir nuolaidų kodų taikymu.

Funkcijos:
- add(id, price) - Prideda dovaną į krepšelį
- remove(id) - Pašalina dovaną iš krepšelio
- total() - Grąžina visų dovanų kainą su nuolaida
- applyDiscount(code) - Taiko nuolaidos kodą

Taisyklės:
- Kiekviena dovanos ID turi būti unikali (jokių dublikatų)
- Promo kodai saugomi objekte
- Netinkami promo kodai ignoruojami
- Krepšelio būsena turi būti išlaikyta

Bonus:
- Neleisti neigiamų kainų
- Leisti tik vieną promo kodą vienu metu
- clear() metodas
- list() metodas
"""

from typing import Dict, List, Optional, Tuple


class SantasGiftCart:
    """
    Santa's Gift Cart Engine klasė.
    
    Valdo dovanų krepšelį su galimybe pridėti, pašalinti dovanas,
    taikyti nuolaidos kodus ir skaičiuoti bendrą kainą.
    """
    
    # Nuolaidų kodų žodynas
    PROMO_CODES = {
        "PROMO10": 0.10,
        "PROMO25": 0.25,
        "SANTA50": 0.50
    }
    
    def __init__(self):
        """
        Inicializuoja tuščią krepšelį.
        
        Atributai:
            gifts (dict): Dovanų žodynas {id: price}
            current_discount (float): Dabartinė nuolaida (0.0 - 1.0)
            discount_code (str): Dabartinis nuolaidos kodas (None, jei nėra)
        """
        self.gifts: Dict[str, float] = {}
        self.current_discount: float = 0.0
        self.discount_code: Optional[str] = None
    
    def add(self, gift_id: str, price: float) -> bool:
        """
        Prideda dovaną į krepšelį.
        
        Taisyklės:
        - Dovanos ID turi būti unikalus (jokių dublikatų)
        - Kaina turi būti neneigiama (bonus)
        - Jei dovana jau egzistuoja, ji nepridedama
        
        Args:
            gift_id (str): Dovanos unikalus identifikatorius
            price (float): Dovanos kaina (candy canes)
        
        Returns:
            bool: True, jei dovana pridėta sėkmingai, False - jei jau egzistuoja
        
        Raises:
            ValueError: Jei kaina neigiama arba netinkamas tipas
        """
        # Validacija: patikrinimas, ar gift_id yra eilutė
        if not isinstance(gift_id, str):
            raise ValueError(f"Dovanos ID turi būti eilutė (string), gauta: {type(gift_id)}")
        
        if not gift_id.strip():
            raise ValueError("Dovanos ID negali būti tuščias")
        
        # Validacija: patikrinimas, ar kaina yra skaičius
        try:
            price = float(price)
        except (TypeError, ValueError):
            raise ValueError(f"Kaina turi būti skaičius, gauta: {type(price)}")
        
        # Bonus: neleisti neigiamų kainų
        if price < 0:
            raise ValueError(f"Kaina negali būti neigiama, gauta: {price}")
        
        # Tikrinimas, ar dovana jau egzistuoja (unikali ID taisyklė)
        if gift_id in self.gifts:
            return False  # Dovanos ID jau egzistuoja
        
        # Pridedame dovaną
        self.gifts[gift_id] = price
        return True
    
    def remove(self, gift_id: str) -> bool:
        """
        Pašalina dovaną iš krepšelio.
        
        Args:
            gift_id (str): Dovanos identifikatorius, kurį reikia pašalinti
        
        Returns:
            bool: True, jei dovana pašalinta sėkmingai, False - jei neegzistuoja
        """
        if not isinstance(gift_id, str):
            return False
        
        if gift_id in self.gifts:
            del self.gifts[gift_id]
            return True
        
        return False
    
    def total(self) -> float:
        """
        Apskaičiuoja bendrą krepšelio kainą su nuolaida.
        
        Skaičiavimas:
        1. Sumuojamos visų dovanų kainos
        2. Taikoma nuolaida (jei yra)
        3. Grąžinama galutinė suma
        
        Returns:
            float: Bendras krepšelio kiekis su nuolaida
        """
        # Sumuojame visas dovanų kainas
        subtotal = sum(self.gifts.values())
        
        # Taikome nuolaidą
        discount_amount = subtotal * self.current_discount
        final_total = subtotal - discount_amount
        
        # Užtikriname, kad suma nėra neigiama
        return max(0.0, final_total)
    
    def applyDiscount(self, promo_code: str) -> bool:
        """
        Taiko nuolaidos kodą.
        
        Taisyklės:
        - Bonus: leidžiamas tik vienas promo kodas vienu metu
        - Netinkami promo kodai ignoruojami saugiai
        - Jei taikomas naujas kodas, senasis pakeičiamas
        
        Args:
            promo_code (str): Nuolaidos kodas
        
        Returns:
            bool: True, jei kodas taikytas sėkmingai, False - jei netinkamas
        """
        if not isinstance(promo_code, str):
            return False
        
        promo_code = promo_code.strip().upper()
        
        # Tikrinimas, ar kodas egzistuoja promo kodų žodyne
        if promo_code in self.PROMO_CODES:
            # Bonus: leidžiame tik vieną promo kodą vienu metu
            # Naujas kodas pakeičia senąjį
            self.current_discount = self.PROMO_CODES[promo_code]
            self.discount_code = promo_code
            return True
        
        # Netinkamas kodas - ignoruojame saugiai (nekelia klaidos)
        return False
    
    def clear(self) -> None:
        """
        Išvalo krepšelį (bonus metodas).
        
        Pašalina visas dovanas ir nuolaidos kodą.
        """
        self.gifts.clear()
        self.current_discount = 0.0
        self.discount_code = None
    
    def list(self) -> List[Tuple[str, float]]:
        """
        Grąžina visų krepšelyje esančių dovanų sąrašą (bonus metodas).
        
        Returns:
            list: Dovanų sąrašas formatu [(id, price), ...]
        """
        return list(self.gifts.items())
    
    def get_info(self) -> Dict:
        """
        Grąžina detalizuotą informaciją apie krepšelį.
        
        Returns:
            dict: Informacija apie krepšelį
        """
        subtotal = sum(self.gifts.values())
        discount_amount = subtotal * self.current_discount
        final_total = self.total()
        
        return {
            "gifts": dict(self.gifts),
            "gift_count": len(self.gifts),
            "subtotal": subtotal,
            "discount_code": self.discount_code,
            "discount_percent": self.current_discount * 100,
            "discount_amount": discount_amount,
            "total": final_total
        }


def format_output(cart_info):
    """
    Formatuoja krepšelio informaciją gražiai ir aiškiai.
    
    Args:
        cart_info (dict): Krepšelio informacija iš get_info()
    
    Returns:
        str: Suformatuota išvestis
    """
    lines = []
    lines.append("=" * 60)
    lines.append("🛒 KREPŠELIO INFORMACIJA")
    lines.append("=" * 60)
    lines.append(f"Dovanų skaičius: {cart_info['gift_count']}")
    
    if cart_info['gifts']:
        lines.append("\nDovanos:")
        for gift_id, price in cart_info['gifts'].items():
            lines.append(f"  • {gift_id}: {price} candy canes")
    else:
        lines.append("\nKrepšelis tuščias")
    
    lines.append(f"\nTarpinė suma: {cart_info['subtotal']:.2f} candy canes")
    
    if cart_info['discount_code']:
        lines.append(f"Nuolaidos kodas: {cart_info['discount_code']}")
        lines.append(f"Nuolaida: {cart_info['discount_percent']:.0f}%")
        lines.append(f"Nuolaidos suma: {cart_info['discount_amount']:.2f} candy canes")
    else:
        lines.append("Nuolaidos kodas: nėra")
    
    lines.append(f"\nBENDRA SUMA: {cart_info['total']:.2f} candy canes")
    lines.append("=" * 60)
    
    return "\n".join(lines)


def run_example():
    """
    Vykdo pavyzdį iš užduoties.
    
    Example:
        cart.add("train", 30)
        cart.add("doll", 20)
        cart.applyDiscount("PROMO10")
        cart.total()    // 45
        cart.remove("train")
        cart.total()    // 18
    """
    print("📖 Vykdomas užduoties pavyzdys...")
    print("=" * 60)
    
    cart = SantasGiftCart()
    
    print("\n1. Pridedame dovanas:")
    cart.add("train", 30)
    cart.add("doll", 20)
    print(f"   Pridėta: train (30), doll (20)")
    print(f"   Krepšelio turinys: {cart.list()}")
    
    print("\n2. Taikome nuolaidos kodą PROMO10:")
    cart.applyDiscount("PROMO10")
    total1 = cart.total()
    print(f"   Bendras kiekis: {total1}")
    print(f"   (30 + 20) * (1 - 0.10) = 50 * 0.90 = 45.0")
    
    print("\n3. Pašaliname 'train':")
    cart.remove("train")
    total2 = cart.total()
    print(f"   Bendras kiekis: {total2}")
    print(f"   (20) * (1 - 0.10) = 20 * 0.90 = 18.0")
    
    print("\n" + format_output(cart.get_info()))
    
    return cart


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    test_cases = [
        {
            "name": "Pagrindinis testas - užduoties pavyzdys",
            "actions": [
                ("add", "train", 30),
                ("add", "doll", 20),
                ("applyDiscount", "PROMO10", None),
                ("total", None, None, 45.0),
                ("remove", "train", None),
                ("total", None, None, 18.0),
            ],
            "description": "Standartinis užduoties pavyzdys"
        },
        {
            "name": "Unikali ID taisyklė",
            "actions": [
                ("add", "gift1", 10),
                ("add", "gift1", 20),  # Bandome pridėti tą patį ID
                ("total", None, None, 10.0),  # Turėtų būti tik pirmoji dovana
            ],
            "description": "Tikrinimas, ar neleidžiama pridėti dublikatų"
        },
        {
            "name": "Netinkamas promo kodas",
            "actions": [
                ("add", "gift1", 100),
                ("applyDiscount", "INVALID", None),
                ("total", None, None, 100.0),  # Neturėtų būti nuolaidos
            ],
            "description": "Netinkami promo kodai turi būti ignoruojami"
        },
        {
            "name": "Vienas promo kodas vienu metu (bonus)",
            "actions": [
                ("add", "gift1", 100),
                ("applyDiscount", "PROMO10", None),
                ("total", None, None, 90.0),
                ("applyDiscount", "SANTA50", None),  # Pakeičia senąjį
                ("total", None, None, 50.0),  # Turėtų būti 50% nuolaida
            ],
            "description": "Naujas promo kodas pakeičia senąjį"
        },
        {
            "name": "clear() metodas (bonus)",
            "actions": [
                ("add", "gift1", 10),
                ("add", "gift2", 20),
                ("clear", None, None),
                ("total", None, None, 0.0),
            ],
            "description": "clear() metodas išvalo krepšelį"
        },
        {
            "name": "list() metodas (bonus)",
            "actions": [
                ("add", "gift1", 10),
                ("add", "gift2", 20),
                ("list", None, None, [("gift1", 10), ("gift2", 20)]),
            ],
            "description": "list() metodas grąžina dovanų sąrašą"
        },
        {
            "name": "Neigiamos kainos (bonus)",
            "actions": [
                ("add", "gift1", -10, ValueError),  # Turėtų kelti klaidą
            ],
            "description": "Neleisti neigiamų kainų"
        },
        {
            "name": "Tuščias krepšelis",
            "actions": [
                ("total", None, None, 0.0),
            ],
            "description": "Tuščio krepšelio suma turėtų būti 0"
        },
        {
            "name": "Visų promo kodų testas",
            "actions": [
                ("add", "gift1", 100),
                ("applyDiscount", "PROMO10", None),
                ("total", None, None, 90.0),
                ("applyDiscount", "PROMO25", None),
                ("total", None, None, 75.0),
                ("applyDiscount", "SANTA50", None),
                ("total", None, None, 50.0),
            ],
            "description": "Tikrinimas visų promo kodų"
        },
    ]
    
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    
    for test in test_cases:
        try:
            cart = SantasGiftCart()
            test_passed = True
            error_msg = None
            
            for action in test["actions"]:
                action_type = action[0]
                
                if action_type == "add":
                    gift_id, price = action[1], action[2]
                    expected_error = action[3] if len(action) > 3 else None
                    
                    try:
                        result = cart.add(gift_id, price)
                        if expected_error:
                            test_passed = False
                            error_msg = f"Tikėtasi klaidos {expected_error}, bet jos nebuvo"
                            break
                    except Exception as e:
                        if expected_error and isinstance(e, expected_error):
                            continue  # Tikėta klaida
                        else:
                            test_passed = False
                            error_msg = f"Nenumatyta klaida: {e}"
                            break
                
                elif action_type == "remove":
                    gift_id = action[1]
                    cart.remove(gift_id)
                
                elif action_type == "applyDiscount":
                    code = action[1]
                    cart.applyDiscount(code)
                
                elif action_type == "total":
                    expected = action[3] if len(action) > 3 else None
                    if expected is not None:
                        result = cart.total()
                        if abs(result - expected) > 0.01:  # Tolerancija slankiojo kablelio palyginimui
                            test_passed = False
                            error_msg = f"total() grąžino {result}, tikėtasi {expected}"
                            break
                
                elif action_type == "clear":
                    cart.clear()
                
                elif action_type == "list":
                    expected = action[3] if len(action) > 3 else None
                    if expected is not None:
                        result = cart.list()
                        # Konvertuojame į list ir palyginame
                        result_list = sorted(result)
                        expected_list = sorted(expected)
                        if result_list != expected_list:
                            test_passed = False
                            error_msg = f"list() grąžino {result_list}, tikėtasi {expected_list}"
                            break
            
            if test_passed:
                status = "✅ PASS"
                passed_count += 1
            else:
                status = "❌ FAIL"
                failed_count += 1
            
            print(f"{status} | {test['name']}")
            print(f"      {test['description']}")
            if error_msg:
                print(f"      ❌ {error_msg}")
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


def interactive_demo():
    """
    Interaktyvus demonstracinis režimas.
    """
    print("=" * 60)
    print("🛒 SANTA'S GIFT CART ENGINE - INTERAKTYVUS REŽIMAS")
    print("=" * 60)
    print("\nGalimos komandos:")
    print("  add <id> <price>     - Pridėti dovaną")
    print("  remove <id>          - Pašalinti dovaną")
    print("  discount <code>      - Taikyti nuolaidos kodą")
    print("  total                - Rodyti bendrą sumą")
    print("  list                 - Rodyti visų dovanų sąrašą")
    print("  clear                - Išvalyti krepšelį")
    print("  info                 - Rodyti detalizuotą informaciją")
    print("  example              - Vykdyti užduoties pavyzdį")
    print("  help                 - Rodyti šią pagalbą")
    print("  quit                 - Išeiti")
    print("\nPavyzdys: add train 30")
    print("=" * 60)
    
    cart = SantasGiftCart()
    
    while True:
        try:
            command = input("\n> ").strip().split()
            
            if not command:
                continue
            
            cmd = command[0].lower()
            
            if cmd == "quit" or cmd == "exit":
                print("👋 Iki pasimatymo!")
                break
            
            elif cmd == "help":
                print("\nGalimos komandos:")
                print("  add <id> <price>     - Pridėti dovaną")
                print("  remove <id>          - Pašalinti dovaną")
                print("  discount <code>      - Taikyti nuolaidos kodą")
                print("  total                - Rodyti bendrą sumą")
                print("  list                 - Rodyti visų dovanų sąrašą")
                print("  clear                - Išvalyti krepšelį")
                print("  info                 - Rodyti detalizuotą informaciją")
                print("  example              - Vykdyti užduoties pavyzdį")
                print("  quit                 - Išeiti")
            
            elif cmd == "add":
                if len(command) < 3:
                    print("❌ Klaida: Naudokite: add <id> <price>")
                    continue
                try:
                    gift_id = command[1]
                    price = float(command[2])
                    if cart.add(gift_id, price):
                        print(f"✅ Dovana '{gift_id}' pridėta (kaina: {price})")
                    else:
                        print(f"⚠️  Dovana su ID '{gift_id}' jau egzistuoja")
                except ValueError as e:
                    print(f"❌ Klaida: {e}")
            
            elif cmd == "remove":
                if len(command) < 2:
                    print("❌ Klaida: Naudokite: remove <id>")
                    continue
                gift_id = command[1]
                if cart.remove(gift_id):
                    print(f"✅ Dovana '{gift_id}' pašalinta")
                else:
                    print(f"⚠️  Dovana su ID '{gift_id}' neegzistuoja")
            
            elif cmd == "discount":
                if len(command) < 2:
                    print("❌ Klaida: Naudokite: discount <code>")
                    continue
                code = command[1]
                if cart.applyDiscount(code):
                    print(f"✅ Nuolaidos kodas '{code}' taikytas")
                else:
                    print(f"⚠️  Netinkamas nuolaidos kodas: '{code}'")
            
            elif cmd == "total":
                total = cart.total()
                print(f"💰 Bendras kiekis: {total:.2f} candy canes")
            
            elif cmd == "list":
                gifts = cart.list()
                if gifts:
                    print("📦 Dovanos krepšelyje:")
                    for gift_id, price in gifts:
                        print(f"  • {gift_id}: {price} candy canes")
                else:
                    print("📦 Krepšelis tuščias")
            
            elif cmd == "clear":
                cart.clear()
                print("🗑️  Krepšelis išvalytas")
            
            elif cmd == "info":
                print(format_output(cart.get_info()))
            
            elif cmd == "example":
                run_example()
            
            else:
                print(f"❌ Nežinoma komanda: {cmd}. Įveskite 'help' pagalbai.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Iki pasimatymo!")
            break
        except Exception as e:
            print(f"❌ Netikėta klaida: {e}")


def main():
    """
    Pagrindinė programa.
    """
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "test":
            success = run_tests()
            sys.exit(0 if success else 1)
        elif command == "example":
            run_example()
            sys.exit(0)
        else:
            print(f"❌ Nežinomas argumentas: {command}")
            print("Naudokite: python cart_solution.py [test|example|interactive]")
            sys.exit(1)
    else:
        # Interaktyvus režimas pagal nutylėjimą
        interactive_demo()


if __name__ == "__main__":
    main()