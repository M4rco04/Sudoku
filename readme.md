# Sudoku Solver - Constraint Satisfaction Problem (CSP)

Projekt to implementacja narzędzia do rozwiązywania Sudoku w języku Python. Wykorzystuje ono modelowanie oparte na **CSP - Constraint Satisfaction Problem** oraz algorytm **Backtracking Search** (przeszukiwanie z nawrotami).

Aby zoptymalizować proces rozwiązywania, w projekcie zaimplementowano następujące heurystyki:

- **MRV (Minimum Remaining Values):** Wybiera w pierwszej kolejności puste pole (zmienną), dla którego pozostało najmniej dozwolonych wartości.
- **Degree Heuristic:** Używana jako heurystyka rozstrzygająca przy remisach w MRV. Wybiera zmienną, która bierze udział w największej liczbie ograniczeń z innymi nieprzypisanymi zmiennymi.
- **LCV (Least Constraining Value):** Porządkuje domeny wartości tak, aby w pierwszej kolejności sprawdzać liczby, które najmniej ograniczają możliwości wyboru dla sąsiednich, pustych pól.

---

## 🛠 Wymagania

Do uruchomienia projektu wymagany jest język **Python 3.x** oraz biblioteka **NumPy**.

Możesz zainstalować brakujące zależności za pomocą menedżera pakietów `pip`:

```bash
pip install numpy
```

---

## 📂 Struktura Projektu

Projekt został podzielony na moduły, aby zapewnić czytelność i łatwość utrzymania kodu:

- `main.py` - Główny punkt wejścia do aplikacji. Odpowiada za parsowanie argumentów z linii poleceń i uruchamianie procesu rozwiązywania.
- `algorithm/backtracking_search.py` - Implementacja algorytmu przeszukiwania z nawrotami (Backtracking). Odpowiada za proces znajdowania rozwiązania oraz renderowanie wyniku w konsoli.
- `csp/csp.py` - Definicja problemu CSP. Zarządza dziedzinami (domenami), ograniczeniami (constraints) pomiędzy polami, weryfikuje spójność (consistency) oraz zawiera logikę dla heurystyk MRV i LCV.
- `representation/board.py` - Reprezentacja planszy Sudoku. Odpowiada za wczytywanie danych z pliku tekstowego oraz udostępnia metody pomocnicze do indeksowania rzędów, kolumn i bloków 3x3.

---

## 🚀 Jak uruchomić

Aby uruchomić solver, użyj pliku `main.py` podając jako argument flagę `-f` (lub `--file`) wraz z nazwą pliku tekstowego zawierającego planszę.

**Ważne:** Zgodnie z założeniami projektu, pliki z planszami muszą znajdować się w katalogu `data/` w głównym folderze projektu.

### Przykład użycia

```bash
python main.py -f 04.txt
```

---

## 📝 Format pliku wejściowego

Plik tekstowy (np. `04.txt`) reprezentujący planszę powinien składać się z 9 linii.

Każda linia to 9 liczb oddzielonych pojedynczą spacją.

- Liczby od `1` do `9` oznaczają z góry przypisane wartości.
- `0` (zero) oznacza puste pole do rozwiązania.

### Przykładowy wygląd pliku

```text
2 0 4 0 0 0 0 0 5
0 7 8 0 0 1 0 0 0
9 0 0 0 0 0 3 0 0
0 0 0 0 2 6 0 0 4
0 0 0 0 7 0 0 0 9
0 0 0 0 5 0 7 8 0
0 9 0 0 0 0 0 6 2
4 0 0 6 0 0 0 0 8
0 1 0 0 0 8 0 0 0
```

---

## 📊 Wynik działania

Po pomyślnym rozwiązaniu łamigłówki, program narysuje w konsoli kompletną planszę Sudoku podzieloną na siatkę 3x3, na przykład:

```text
|-------|-------|-------|
| 2 3 4 | 9 6 7 | 8 1 5 |
| 5 7 8 | 3 4 1 | 2 9 6 |
| 9 6 1 | 2 8 5 | 3 4 7 |
|-------|-------|-------|
| 7 8 9 | 1 2 6 | 5 3 4 |
| 1 4 5 | 8 7 3 | 6 2 9 |
| 3 2 6 | 4 5 9 | 7 8 1 |
|-------|-------|-------|
| 8 9 7 | 5 3 4 | 1 6 2 |
| 4 5 3 | 6 1 2 | 9 7 8 |
| 6 1 2 | 7 9 8 | 4 5 3 |
|-------|-------|-------|
```

Jeśli dane Sudoku nie posiada rozwiązania, program wyświetli odpowiedni komunikat.
