import sys
import os
from datetime import datetime

# Dodaj ścieżki do modułów
sys.path.append(os.path.abspath("lib/modul1"))
sys.path.append(os.path.abspath("lib/modul2"))
sys.path.append(os.path.abspath("lib/modul3"))

# Importuj funkcje z modułów
from modul import wykonaj as wykonaj_a
from modul import wykonaj as wykonaj_b
from modul import wykonaj as wykonaj_c

wykonaj_a()
wykonaj_b()
wykonaj_c()

print(f"Skrypt wykonany: {datetime.now().strftime('%Y.%m.%d o godzinie %H:%M:%S')}")
