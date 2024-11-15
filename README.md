# Opis działania aplikacji

Na początku ładujemy zmienne środowiskowe. Otwieramy plik trescArtykulu.txt, który posiada treść artykułu z zadania do wykonania i przypisujemy ją do zmiennej. Aplikacja pobiera klucz api od OpenAI znajdujący się w pliku z zależnościami ".env". Działanie te ma na celu oddzielić kod od danych wrażliwych, których nie chcemy udostepniać w repozytorium. Następnie określamy zasady według których chcemy aby sztuczna inteligencja modyfikowała artykuł, który dołączamy i przypisujemy całość do zmiennej. Następnym krokiem jest konfiguracja modelu sztucznej inteligencji, który przyjmujme nasz wcześniej przypisany do zmiennej tekst artykułu wraz z wytycznymi. Następnie wykonujemy zapytanie, otwieramy plik artykul.html i zapisujemy w nim odpowiedź.

# Wymagania wstępne 

Python 3.8 lub 3.11
Menedżer pakietów pip.

# Jeśli nie masz powyższych to:

1. Windows
a) Pobierz instalator:
Przejdź na stronę oficjalnego Pythona: https://www.python.org/downloads/
Kliknij na wersję Pythona, którą chcesz zainstalować (np. 3.8 lub 3.11).
Pobierz plik instalacyjny odpowiedni dla Twojego systemu (Windows 64-bit lub 32-bit).
b) Zainstaluj Python:
Uruchom pobrany plik instalacyjny.
W oknie instalatora upewnij się, że zaznaczone jest pole "Add Python to PATH" (dzięki temu Python będzie dostępny z wiersza poleceń) oraz "Install pip" żeby zainstalować menadżer pakietów pip.
Kliknij Install Now.
Po zakończeniu instalacji kliknij Close.
c) Sprawdź wersję:
Otwórz Wiersz Poleceń (Command Prompt).
Wpisz poniższą komendę, aby sprawdzić zainstalowaną wersję Pythona:

python --version

Lub, jeśli masz zainstalowaną więcej niż jedną wersję:

python3 --version

2. Linux (Ubuntu/Debian)
a) Instalacja Pythona z repozytoriów:
Otwórz Terminal.
Zaktualizuj listę pakietów:

sudo apt update

Zainstaluj Pythona 3.8 lub 3.11:

sudo apt install python3.8

Lub:

sudo apt install python3.11

b) Zainstaluj pip (jeśli nie jest zainstalowany):
Aby zainstalować pip dla Pythona 3.8 lub 3.11, użyj:

sudo apt install python3.8-venv python3.8-pip

Lub:

sudo apt install python3.11-venv python3.11-pip

c) Sprawdź wersję:
Sprawdź, czy Python jest poprawnie zainstalowany:

python --version

Lub, jeśli masz zainstalowaną więcej niż jedną wersję:

python3 --version

# Kolejnym krokiem jest utworzenie wirtualnego środowiska:

1. Przejdź do folderu projektu i utwórz nowe wirtualne środowisko:

python -m venv myenv

2. Aktywuj wirtualne środowisko:

a) Na Windows:

myenv\Scripts\activate

b) Na Linux:

source myenv/bin/activate

3. Aby zainstalować zależności, użyj pip:

pip install -r requirements.txt

4. Uruchom program:

python main.py