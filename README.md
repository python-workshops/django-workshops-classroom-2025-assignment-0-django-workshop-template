# 🚀 Django Workshop - Assignment 0: Pierwsze URL-e Django

Witamy w pierwszym zadaniu z serii Django Workshop! To zadanie wprowadzi Cię w podstawy mapowania URL-i w Django.

## 📋 Czego się nauczysz?

- ✅ **Importowanie views** w pliku urls.py
- ✅ **Mapowanie URL-i** na odpowiednie widoki
- ✅ **Trzy typy response Django:** HttpResponse, render(), JsonResponse
- ✅ **Podstawy workflow GitHub Classroom**

## 🎯 Twoje zadanie

### Problem do rozwiązania:
Aplikacja ma trzy gotowe widoki (`views.home`, `views.info`, `views.health_check`), ale **nie są zmapowane na żadne URL-e**. Gdy uruchomisz serwer i wejdziesz na stronę główną, zobaczysz błąd.

### Co musisz zrobić:

#### 1. Zaimportuj views
W pliku `workshop_project/urls.py` dodaj import views w odpowiednim miejscu

#### 2. Dodaj mapowanie URL-i  
W tym samym pliku dodaj mapowanie URL-i zgodnie z komentarzami TODO:
- Strona główna ('') → views.home (HttpResponse)
- Strona informacyjna ('info/') → views.info (render)
- Health check API ('health/') → views.health_check (JsonResponse)

## 🧪 Testowanie rozwiązania

### 1. Uruchom serwer deweloperski
```bash
python manage.py runserver
```

### 2. Sprawdź czy strony działają
- **http://localhost:8000** - Strona główna (HttpResponse z HTML)
- **http://localhost:8000/info/** - Strona informacyjna (render z template)
- **http://localhost:8000/health/** - API endpoint (JsonResponse z JSON)

### 3. Sprawdź autograding
```bash
# Uruchom testy automatyczne (opcjonalne)
DJANGO_SETTINGS_MODULE=workshop_project.settings python -m pytest tests/test_assignment_0.py -v
```

## ✅ Kryteria sukcesu

Zadanie jest zaliczone gdy:

1. **Wszystkie testy przechodzą** ✅
2. **Strona główna** (/) wyświetla się poprawnie
3. **Strona info** (/info/) wyświetla się poprawnie  
4. **Brak błędów 404** na głównych endpoint-ach

## 📚 Co się dzieje pod spodem?

### Trzy typy Django response

**views.home** używa **HttpResponse**:
```python
return HttpResponse("<h1>Django Workshop</h1>...")
```
- Zwraca HTML bezpośrednio jako string
- Najprostrzy sposób zwrócenia HTML

**views.info** używa **render()**: 
```python
return render(request, 'info.html')
```
- Przetwarza plik template HTML
- Może przekazywać dane kontekstu
- Separation of concerns (logika vs prezentacja)

**views.health_check** używa **JsonResponse**:
```python
return JsonResponse({'status': 'ok'})
```
- Zwraca dane w formacie JSON
- Używane w API i AJAX requests
- Automatycznie ustawia Content-Type: application/json

### Mapowanie URL-i
```python
path('', views.home),      # Główna strona
path('info/', views.info), # Strona /info/
```
- **Pierwszy argument**: wzorzec URL (string)
- **Drugi argument**: funkcja widoku do wywołania
- Django automatycznie przekazuje `request` do widoku

## 🐛 Rozwiązywanie problemów

### Problem: "NameError: name 'views' is not defined"
```python
# Upewnij się że zaimportowałeś views:
from . import views
```

### Problem: Strona 404 na głównej stronie
```python
# Sprawdź czy masz mapowanie na pustą ścieżkę:
path('', views.home),
```

### Problem: "Template does not exist: info.html"
- Template `info.html` już istnieje w folderze `templates/`
- Sprawdź czy masz `path('info/', views.info),` w urlpatterns

### Problem: Server nie startuje
```bash
# Sprawdź czy masz aktywne venv:
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate     # Windows

# Zainstaluj zależności:
pip install -r requirements.txt

# Uruchom migracje:
python manage.py migrate
```

## 🎓 Co dalej?

Po zaliczeniu Assignment 0 będziesz gotowy do **Assignment 1: Pierwsza aplikacja Django**, gdzie:

- Utworzysz pierwszą aplikację Django
- Poznasz różnicę między projektem a aplikacją
- Skonfigurujesz INSTALLED_APPS
- Zbudujesz pierwsze modele

## 🔧 Struktura projektu

```
django_workshop_template/
├── manage.py                    # Django management script
├── workshop_project/            # Main Django project
│   ├── settings.py              # Django settings
│   ├── urls.py                  # 🎯 TU ROBISZ ZMIANY
│   ├── views.py                 # Gotowe widoki
│   └── ...
├── templates/                   # HTML templates
│   └── info.html               # Template dla views.info
└── tests/                      # Test files
    └── test_assignment_0.py    # Testy autograding
```

## 💡 Wskazówki

1. **Sprawdzaj logi** w konsoli gdy uruchomisz serwer
2. **URL-e kończące się na /** wymagają slash w mapowaniu
3. **Import views** musi być na górze pliku urls.py
4. **GitHub autograding** sprawdza poprawność automatycznie po każdym push
5. **Template info.html** jest już gotowy - nie musisz go edytować

---

## 🆘 Potrzebujesz pomocy?

- **Discord/Slack**: Zadaj pytanie na kanale warsztatowym  
- **Issues**: Utwórz issue w repozytorium jeśli znajdziesz błąd
- **Instruktor**: Poproś o pomoc podczas warsztatów

---

**Powodzenia!** 🎉

> **Pamiętaj**: Assignment 0 to podstawy URL mapping. W kolejnych zadaniach będziesz budować prawdziwą aplikację Django krok po kroku!