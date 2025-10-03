# Mini proyecto: cálculo + validación + acción (con Pytest)

## Estructura
```
mini_pytest_proyecto/
├─ src/myapp/
│  ├─ __init__.py
│  ├─ calc.py
│  ├─ validation.py
│  ├─ action.py
│  └─ flow.py
├─ tests/
│  ├─ test_unit_calc.py
│  ├─ test_unit_validation.py
│  ├─ test_unit_action.py
│  ├─ test_integration_calc_validation.py
│  └─ test_e2e_flow.py
└─ pyproject.toml
```

## Cómo correr
1) Instala pytest si hace falta:
```bash
pip install pytest
```
2) Desde la carpeta `mini_pytest_proyecto`, ejecuta:
```bash
pytest
```
o bien:
```bash
python -m pytest
```

## Idea del flujo
- **cálculo**: sumar subtotales y aplicar impuesto.
- **validación**: asegurar que datos y parámetros son válidos.
- **acción**: guardar un "pedido" (order) a disco (CSV simulado).
- **flujo**: orquesta los tres pasos y devuelve el resultado final.
