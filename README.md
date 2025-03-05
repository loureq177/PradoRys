<div align="center">

# 📉 PrądoRys 📈

![Demo GIF](static\demo.gif)

</div>

- *PrądoRys* to aplikacja do wizualizacji danych dotyczących zużycia energii elektrycznej. Aplikacja umożliwia generowanie wykresów, które mogą pomóc w analizie i monitorowaniu zużycia energii w czasie.
- Wykresy generowane są za pomocą biblioteki [chart.js](https://www.chartjs.org) i jako danych wejściowych używają plików CSV (przykłady w katalogu static).

## Wymagania (w requirements.txt)
- Python 3.x
- Django
- Django REST Framework
- Pandas

## Instalacja
1. Sklonuj repozytorium:
  ```bash
  git clone https://github.com/loureq177/PradoRys.git
  cd PradoRys
  ```
2. Zainstaluj zależności:
  ```bash
  pip install -r requirements.txt
  ```

## Użycie
  Aby uruchomić aplikację lokalnie:
```bash
python manage.py runserver
