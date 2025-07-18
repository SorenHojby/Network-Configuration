# Netværkskonfigurationsgenerator

![CI](https://github.com/SorenHojby/Network-Configuration/actions/workflows/python-app.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

Et CLI-værktøj i Python, der genererer konfigurationsfiler til switches baseret på YAML-input og Jinja2-templates.

## Funktionalitet

- Læser switchdata fra en YAML-fil
- Genererer `.conf`-filer med Jinja2
- Logger både til konsol og fil
- Fejlhåndtering i form at logging i både konsol og logfil

## Struktur

- `main.py` – CLI og programflow
- `core/config_loader.py` – Loader og validerer YAML-data
- `core/config_renderer.py` – Genererer konfigurationsfiler
- `templates/switch_config.j2` – Jinja2-template
- `config/switches.yml` – Eksempeldata

## Start dit python miljø

```cli
python -m venv venv
venv\Scripts\activate
```

## Installation

```cli
pip install -r requirements.txt
```

## Brug

```cli
python main.py --input config/switches.yml --output output/
```

Valgfrit:

```cli
--template templates/switch_config.j2
```

## Eksempel på input (YAML)

```yaml
- hostname: switch01
  ip: 10.0.0.1
  location: Billund
  vlan: 42
- hostname: switch02
  ip: 10.0.0.2
  location: Prague
  vlan: 99
```

## Logning

Logs gemmes i `logs/network_config_switches.log`.

## Test

For at køre tests:

```bash
pytest
```

## Krav

- Python 3.8+
- Jinja2
- PyYAML

## GitHub Actions (CI)

Projektet anvender **GitHub Actions** til automatisk test og validering ved hver push og pull request.

### CI-pipeline gør følgende

- Installerer dependencies (`pip install -r requirements.txt`)
- Kører `pytest` for at sikre at funktionaliteten virker

## Github link

- url: [https://github.com/SorenHojby/Network-Configuration](https://github.com/SorenHojby/Network-Configuration)
