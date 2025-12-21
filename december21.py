"""
Christmas Library Task Solution

Užduotis: Sukurti Kalėdų bibliotekos sistemą naudojant objektinio programavimo principus.

Sistema turi mokėti:
- Saugoti informaciją apie knygas
- Registruoti skaitytojus
- Skolinti knygas skaitytojams
- Priimti grąžintas knygas
- Spausdinti šventinę bibliotekos būsenos ataskaitą

Klasės:
- Book: knyga bibliotekoje
- Reader: bibliotekos skaitytojas
- Loan: skolinta knyga
- Library: pagrindinė klasė, valdanti viską
"""

from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum


class LoanStatus(Enum):
    """Skolos būsenos enum."""
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"


class Book:
    """
    Knygos klasė - reprezentuoja knygą bibliotekoje.
    
    Laukai:
        id: Knygos unikalus identifikatorius
        title: Knygos pavadinimas
        author: Autorius
        totalCopies: Bendras egzempliorių skaičius
        availableCopies: Prieinamų egzempliorių skaičius
    
    Taisyklės:
        - availableCopies negali būti neigiamas
        - availableCopies negali viršyti totalCopies
    """
    
    def __init__(self, book_id: str, title: str, author: str, total_copies: int):
        """
        Inicializuoja knygą.
        
        Args:
            book_id (str): Knygos ID
            title (str): Pavadinimas
            author (str): Autorius
            total_copies (int): Bendras egzempliorių skaičius
        
        Raises:
            ValueError: Jei duomenys netinkami
        """
        if not isinstance(book_id, str) or not book_id.strip():
            raise ValueError("Knygos ID turi būti netuščia eilutė")
        
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Knygos pavadinimas turi būti netuščia eilutė")
        
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Autorius turi būti netuščia eilutė")
        
        if not isinstance(total_copies, int) or total_copies <= 0:
            raise ValueError(f"Bendras egzempliorių skaičius turi būti teigiamas sveikasis skaičius, gauta: {total_copies}")
        
        self.id = book_id
        self.title = title
        self.author = author
        self.totalCopies = total_copies
        self.availableCopies = total_copies  # Pradžioje visi egzemplioriai prieinami
    
    def isAvailable(self) -> bool:
        """
        Tikrina, ar yra bent vienas prieinamas egzempliorius.
        
        Returns:
            bool: True, jei yra bent vienas prieinamas egzempliorius
        """
        return self.availableCopies > 0
    
    def borrow(self) -> bool:
        """
        Skolina vieną egzempliorių.
        
        Returns:
            bool: True, jei pavyko, False - jei nėra prieinamų egzempliorių
        """
        if self.availableCopies > 0:
            self.availableCopies -= 1
            return True
        return False
    
    def return_copy(self) -> None:
        """
        Grąžina vieną egzempliorių.
        
        Raises:
            ValueError: Jei availableCopies jau lygus totalCopies
        """
        if self.availableCopies >= self.totalCopies:
            raise ValueError(f"Negalima grąžinti knygos '{self.title}' - visi egzemplioriai jau grąžinti")
        
        self.availableCopies += 1
    
    def __repr__(self) -> str:
        """Grąžina knygos tekstinį atvaizdavimą."""
        return f"Book(id='{self.id}', title='{self.title}', author='{self.author}', available={self.availableCopies}/{self.totalCopies})"


class Reader:
    """
    Skaitytojo klasė - reprezentuoja bibliotekos skaitytoją.
    
    Laukai:
        id: Skaitytojo unikalus identifikatorius
        name: Vardas
        borrowLimit: Maksimalus skolintų knygų skaičius
        borrowedBookIds: Skolintų knygų ID sąrašas
    """
    
    def __init__(self, reader_id: str, name: str, borrow_limit: int):
        """
        Inicializuoja skaitytoją.
        
        Args:
            reader_id (str): Skaitytojo ID
            name (str): Vardas
            borrow_limit (int): Maksimalus skolintų knygų skaičius
        
        Raises:
            ValueError: Jei duomenys netinkami
        """
        if not isinstance(reader_id, str) or not reader_id.strip():
            raise ValueError("Skaitytojo ID turi būti netuščia eilutė")
        
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Skaitytojo vardas turi būti netuščia eilutė")
        
        if not isinstance(borrow_limit, int) or borrow_limit <= 0:
            raise ValueError(f"Skolinimo limitas turi būti teigiamas sveikasis skaičius, gauta: {borrow_limit}")
        
        self.id = reader_id
        self.name = name
        self.borrowLimit = borrow_limit
        self.borrowedBookIds = []  # Sąrašas skolintų knygų ID
    
    def canBorrow(self) -> bool:
        """
        Tikrina, ar skaitytojas gali skolintis daugiau knygų.
        
        Returns:
            bool: True, jei skaitytojas dar nepasiekė limito
        """
        return len(self.borrowedBookIds) < self.borrowLimit
    
    def addBorrowedBook(self, book_id: str) -> None:
        """
        Prideda knygos ID prie skolintų knygų sąrašo.
        
        Args:
            book_id (str): Knygos ID
        
        Raises:
            ValueError: Jei skaitytojas jau pasiekė limitą
        """
        if not self.canBorrow():
            raise ValueError(f"Skaitytojas '{self.name}' jau pasiekė skolinimo limitą ({self.borrowLimit})")
        
        if book_id in self.borrowedBookIds:
            raise ValueError(f"Skaitytojas '{self.name}' jau turi skolintą knygą su ID '{book_id}'")
        
        self.borrowedBookIds.append(book_id)
    
    def removeBorrowedBook(self, book_id: str) -> None:
        """
        Pašalina knygos ID iš skolintų knygų sąrašo.
        
        Args:
            book_id (str): Knygos ID
        
        Raises:
            ValueError: Jei knyga nerasta skolintų sąraše
        """
        if book_id not in self.borrowedBookIds:
            raise ValueError(f"Skaitytojas '{self.name}' neturi skolintos knygos su ID '{book_id}'")
        
        self.borrowedBookIds.remove(book_id)
    
    def __repr__(self) -> str:
        """Grąžina skaitytojo tekstinį atvaizdavimą."""
        return f"Reader(id='{self.id}', name='{self.name}', borrowLimit={self.borrowLimit}, borrowed={len(self.borrowedBookIds)})"


class Loan:
    """
    Skolos klasė - reprezentuoja skolintą knygą.
    
    Laukai:
        id: Skolos unikalus identifikatorius
        bookId: Knygos ID
        readerId: Skaitytojo ID
        loanDate: Skolinimo data
        returnDate: Grąžinimo data (gali būti None)
        status: Skolos būsena (ACTIVE arba RETURNED)
    """
    
    def __init__(self, loan_id: str, book_id: str, reader_id: str, loan_date: datetime):
        """
        Inicializuoja skolą.
        
        Args:
            loan_id (str): Skolos ID
            book_id (str): Knygos ID
            reader_id (str): Skaitytojo ID
            loan_date (datetime): Skolinimo data
        """
        self.id = loan_id
        self.bookId = book_id
        self.readerId = reader_id
        self.loanDate = loan_date
        self.returnDate: Optional[datetime] = None
        self.status = LoanStatus.ACTIVE
    
    def markAsReturned(self, return_date: datetime) -> None:
        """
        Pažymi skolą kaip grąžintą.
        
        Args:
            return_date (datetime): Grąžinimo data
        """
        if self.status == LoanStatus.RETURNED:
            raise ValueError(f"Skolos '{self.id}' jau pažymėta kaip grąžinta")
        
        self.returnDate = return_date
        self.status = LoanStatus.RETURNED
    
    def __repr__(self) -> str:
        """Grąžina skolos tekstinį atvaizdavimą."""
        status_str = f", returnDate={self.returnDate}" if self.returnDate else ""
        return f"Loan(id='{self.id}', bookId='{self.bookId}', readerId='{self.readerId}', status={self.status.value}{status_str})"


class Library:
    """
    Bibliotekos klasė - pagrindinė klasė, valdanti viską.
    
    Laukai:
        books: Knygų kolekcija
        readers: Skaitytojų kolekcija
        loans: Skolų kolekcija
    """
    
    def __init__(self):
        """Inicializuoja tuščią biblioteką."""
        self.books: Dict[str, Book] = {}
        self.readers: Dict[str, Reader] = {}
        self.loans: Dict[str, Loan] = {}
        self._next_loan_id = 1
    
    def addBook(self, book: Book) -> None:
        """
        Prideda knygą į biblioteką.
        
        Args:
            book (Book): Knygos objektas
        
        Raises:
            ValueError: Jei knyga su tuo pačiu ID jau egzistuoja
        """
        if not isinstance(book, Book):
            raise ValueError(f"Knyga turi būti Book tipo objektas, gauta: {type(book)}")
        
        if book.id in self.books:
            raise ValueError(f"Knyga su ID '{book.id}' jau egzistuoja bibliotekoje")
        
        self.books[book.id] = book
    
    def registerReader(self, reader: Reader) -> None:
        """
        Registruoja skaitytoją bibliotekoje.
        
        Args:
            reader (Reader): Skaitytojo objektas
        
        Raises:
            ValueError: Jei skaitytojas su tuo pačiu ID jau egzistuoja
        """
        if not isinstance(reader, Reader):
            raise ValueError(f"Skaitytojas turi būti Reader tipo objektas, gauta: {type(reader)}")
        
        if reader.id in self.readers:
            raise ValueError(f"Skaitytojas su ID '{reader.id}' jau egzistuoja bibliotekoje")
        
        self.readers[reader.id] = reader
    
    def borrowBook(self, reader_id: str, book_id: str, date: datetime) -> Loan:
        """
        Skolina knygą skaitytojui.
        
        Algoritmas:
        1. Tikrina, ar knyga ir skaitytojas egzistuoja
        2. Tikrina, ar yra prieinamų egzempliorių
        3. Tikrina, ar skaitytojas gali skolintis daugiau knygų
        4. Sukuria skolą ir atnaujina būsenas
        
        Args:
            reader_id (str): Skaitytojo ID
            book_id (str): Knygos ID
            date (datetime): Skolinimo data
        
        Returns:
            Loan: Sukurta skola
        
        Raises:
            ValueError: Jei skolinimas nepavyko (knyga/skaitytojas neegzistuoja, nėra egzempliorių, pasiektas limitas)
        """
        # Tikrinimas: ar knyga egzistuoja
        if book_id not in self.books:
            raise ValueError(f"Knyga su ID '{book_id}' neegzistuoja bibliotekoje")
        
        # Tikrinimas: ar skaitytojas egzistuoja
        if reader_id not in self.readers:
            raise ValueError(f"Skaitytojas su ID '{reader_id}' neegzistuoja bibliotekoje")
        
        book = self.books[book_id]
        reader = self.readers[reader_id]
        
        # Tikrinimas: ar yra prieinamų egzempliorių
        if not book.isAvailable():
            raise ValueError(f"Nėra prieinamų '{book.title}' egzempliorių")
        
        # Tikrinimas: ar skaitytojas gali skolintis daugiau knygų
        if not reader.canBorrow():
            raise ValueError(f"Skaitytojas '{reader.name}' pasiekė skolinimo limitą ({reader.borrowLimit})")
        
        # Skoliname knygą
        book.borrow()
        reader.addBorrowedBook(book_id)
        
        # Sukuriame skolą
        loan_id = f"LOAN{self._next_loan_id}"
        self._next_loan_id += 1
        
        loan = Loan(loan_id, book_id, reader_id, date)
        self.loans[loan.id] = loan
        
        return loan
    
    def returnBook(self, loan_id: str, date: datetime) -> None:
        """
        Grąžina knygą į biblioteką.
        
        Args:
            loan_id (str): Skolos ID
            date (datetime): Grąžinimo data
        
        Raises:
            ValueError: Jei skola neegzistuoja arba jau grąžinta
        """
        if loan_id not in self.loans:
            raise ValueError(f"Skolos su ID '{loan_id}' neegzistuoja")
        
        loan = self.loans[loan_id]
        
        if loan.status == LoanStatus.RETURNED:
            raise ValueError(f"Skolos '{loan_id}' jau grąžinta")
        
        # Grąžiname knygą
        book = self.books[loan.bookId]
        book.return_copy()
        
        # Atnaujiname skaitytojo būseną
        reader = self.readers[loan.readerId]
        reader.removeBorrowedBook(loan.bookId)
        
        # Pažymime skolą kaip grąžintą
        loan.markAsReturned(date)
    
    def getActiveLoans(self) -> List[Loan]:
        """
        Grąžina visų aktyvių skolų sąrašą.
        
        Returns:
            list: Aktyvių skolų sąrašas
        """
        return [loan for loan in self.loans.values() if loan.status == LoanStatus.ACTIVE]
    
    def printChristmasReport(self) -> str:
        """
        Spausdina šventinę bibliotekos būsenos ataskaitą.
        
        Formatas:
        - Knygų sąrašas su prieinamų/bendrų egzempliorių skaičiumi
        - Aktyvių skolų sąrašas
        
        Returns:
            str: Ataskaitos tekstas
        """
        lines = []
        lines.append("CHRISTMAS LIBRARY REPORT")
        lines.append("")
        
        # Knygų sąrašas
        for book in sorted(self.books.values(), key=lambda b: b.title):
            lines.append(f"{book.title}: {book.availableCopies} / {book.totalCopies} available")
        
        lines.append("")
        lines.append("ACTIVE LOANS")
        
        # Aktyvių skolų sąrašas
        active_loans = self.getActiveLoans()
        if active_loans:
            for loan in active_loans:
                book = self.books[loan.bookId]
                reader = self.readers[loan.readerId]
                lines.append(f"{reader.name} → {book.title}")
        else:
            lines.append("(No active loans)")
        
        return "\n".join(lines)


def run_christmas_scenario():
    """
    Vykdo Kalėdų scenarijų iš užduoties.
    
    Scenarijus:
    1. Sukuria knygas
    2. Registruoja skaitytojus
    3. Alice skolina "Clean Code"
    4. Alice skolina "Clean Code" dar kartą
    5. Bob bando skolinti "Clean Code" (turi nepavykti)
    6. Alice grąžina vieną "Clean Code" egzempliorių
    7. Spausdina galutinę ataskaitą
    """
    print("=" * 60)
    print("🎄 CHRISTMAS LIBRARY SCENARIO")
    print("=" * 60)
    print()
    
    # Sukuriame biblioteką
    library = Library()
    
    # Pridedame knygas
    print("📚 Pridedame knygas...")
    library.addBook(Book("B1", "Clean Code", "Robert C. Martin", 2))
    library.addBook(Book("B2", "The Pragmatic Programmer", "Andrew Hunt", 1))
    library.addBook(Book("B3", "Refactoring", "Martin Fowler", 1))
    print("✅ Knygos pridėtos")
    print()
    
    # Registruojame skaitytojus
    print("👥 Registruojame skaitytojus...")
    alice = Reader("R1", "Alice", 2)
    bob = Reader("R2", "Bob", 1)
    library.registerReader(alice)
    library.registerReader(bob)
    print("✅ Skaitytojai užregistruoti")
    print()
    
    # Scenarijus
    date1 = datetime(2024, 12, 1, 10, 0)
    date2 = datetime(2024, 12, 1, 11, 0)
    date3 = datetime(2024, 12, 1, 12, 0)
    date4 = datetime(2024, 12, 2, 10, 0)
    
    # 1. Alice skolina "Clean Code"
    print("1️⃣  Alice skolina 'Clean Code'...")
    try:
        loan1 = library.borrowBook("R1", "B1", date1)
        print(f"✅ BORROW OK: Alice borrowed \"Clean Code\"")
    except ValueError as e:
        print(f"❌ BORROW FAILED: {e}")
    print()
    
    # 2. Alice skolina "Clean Code" dar kartą
    print("2️⃣  Alice skolina 'Clean Code' dar kartą...")
    try:
        loan2 = library.borrowBook("R1", "B1", date2)
        print(f"✅ BORROW OK: Alice borrowed \"Clean Code\"")
    except ValueError as e:
        print(f"❌ BORROW FAILED: {e}")
    print()
    
    # 3. Bob bando skolinti "Clean Code" (turi nepavykti)
    print("3️⃣  Bob bando skolinti 'Clean Code'...")
    try:
        loan3 = library.borrowBook("R2", "B1", date3)
        print(f"✅ BORROW OK: Bob borrowed \"Clean Code\"")
    except ValueError as e:
        print(f"❌ BORROW FAILED: Bob cannot borrow \"Clean Code\" ({e})")
    print()
    
    # 4. Alice grąžina vieną "Clean Code" egzempliorių
    print("4️⃣  Alice grąžina vieną 'Clean Code' egzempliorių...")
    try:
        library.returnBook(loan1.id, date4)
        print(f"✅ RETURN OK: \"Clean Code\" returned by Alice")
    except ValueError as e:
        print(f"❌ RETURN FAILED: {e}")
    print()
    
    # 5. Spausdiname ataskaitą
    print("=" * 60)
    print(library.printChristmasReport())
    print("=" * 60)


def run_tests():
    """
    Vykdo automatinius testus, kad patikrintų sprendimo teisingumą.
    
    Returns:
        bool: True, jei visi testai praėjo sėkmingai
    """
    print("🧪 Vykdomi automatiniai testai...")
    print("=" * 70)
    
    passed_count = 0
    failed_count = 0
    
    # Test 1: Book creation and isAvailable
    try:
        book = Book("B1", "Test Book", "Test Author", 2)
        assert book.isAvailable() == True, "Knyga turėtų būti prieinama"
        book.borrow()
        assert book.availableCopies == 1, "Turėtų likti 1 egzempliorius"
        assert book.isAvailable() == True, "Knyga vis dar turėtų būti prieinama"
        book.borrow()
        assert book.availableCopies == 0, "Turėtų likti 0 egzempliorių"
        assert book.isAvailable() == False, "Knyga neturėtų būti prieinama"
        print("✅ PASS | Book creation and isAvailable")
        passed_count += 1
    except Exception as e:
        print(f"❌ FAIL | Book creation and isAvailable: {e}")
        failed_count += 1
    
    # Test 2: Reader canBorrow
    try:
        reader = Reader("R1", "Test Reader", 2)
        assert reader.canBorrow() == True, "Skaitytojas turėtų galėti skolintis"
        reader.addBorrowedBook("B1")
        assert reader.canBorrow() == True, "Skaitytojas vis dar turėtų galėti skolintis"
        reader.addBorrowedBook("B2")
        assert reader.canBorrow() == False, "Skaitytojas neturėtų galėti skolintis"
        print("✅ PASS | Reader canBorrow")
        passed_count += 1
    except Exception as e:
        print(f"❌ FAIL | Reader canBorrow: {e}")
        failed_count += 1
    
    # Test 3: Library borrowBook
    try:
        library = Library()
        library.addBook(Book("B1", "Test Book", "Author", 1))
        library.registerReader(Reader("R1", "Test Reader", 1))
        
        loan = library.borrowBook("R1", "B1", datetime.now())
        assert loan.status == LoanStatus.ACTIVE, "Skolos būsena turėtų būti ACTIVE"
        assert library.books["B1"].availableCopies == 0, "Knyga neturėtų būti prieinama"
        assert "B1" in library.readers["R1"].borrowedBookIds, "Knyga turėtų būti skaitytojo sąraše"
        
        print("✅ PASS | Library borrowBook")
        passed_count += 1
    except Exception as e:
        print(f"❌ FAIL | Library borrowBook: {e}")
        failed_count += 1
    
    # Test 4: Library returnBook
    try:
        library = Library()
        library.addBook(Book("B1", "Test Book", "Author", 1))
        library.registerReader(Reader("R1", "Test Reader", 1))
        
        loan = library.borrowBook("R1", "B1", datetime.now())
        library.returnBook(loan.id, datetime.now())
        
        assert loan.status == LoanStatus.RETURNED, "Skolos būsena turėtų būti RETURNED"
        assert library.books["B1"].availableCopies == 1, "Knyga turėtų būti prieinama"
        assert "B1" not in library.readers["R1"].borrowedBookIds, "Knyga neturėtų būti skaitytojo sąraše"
        
        print("✅ PASS | Library returnBook")
        passed_count += 1
    except Exception as e:
        print(f"❌ FAIL | Library returnBook: {e}")
        failed_count += 1
    
    # Test 5: Borrow limit
    try:
        library = Library()
        library.addBook(Book("B1", "Book 1", "Author", 10))
        library.addBook(Book("B2", "Book 2", "Author", 10))
        library.addBook(Book("B3", "Book 3", "Author", 10))
        library.registerReader(Reader("R1", "Test Reader", 2))
        
        library.borrowBook("R1", "B1", datetime.now())
        library.borrowBook("R1", "B2", datetime.now())
        
        try:
            library.borrowBook("R1", "B3", datetime.now())
            assert False, "Turėjo kilti klaida - pasiektas limitas"
        except ValueError:
            pass  # Tikėtina klaida
        
        print("✅ PASS | Borrow limit")
        passed_count += 1
    except Exception as e:
        print(f"❌ FAIL | Borrow limit: {e}")
        failed_count += 1
    
    print("=" * 70)
    print(f"📈 Rezultatai: {passed_count} sėkmingi, {failed_count} nesėkmingi iš 5 testų")
    
    if failed_count == 0:
        print("🎉 Visi testai praėjo sėkmingai!")
        return True
    else:
        print("⚠️  Kai kurie testai nepavyko. Patikrinkite kodą.")
        return False


def main():
    """
    Pagrindinė programa.
    """
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1].lower() == "test":
        success = run_tests()
        sys.exit(0 if success else 1)
    elif len(sys.argv) > 1 and sys.argv[1].lower() == "scenario":
        run_christmas_scenario()
    else:
        print("Naudojimas:")
        print("  python library_solution.py scenario  - Vykdo Kalėdų scenarijų")
        print("  python library_solution.py test     - Vykdo testus")
        run_christmas_scenario()


if __name__ == "__main__":
    main()

