<div align="center">

# 🚀 Xtrim – Pruebas Automatizadas con Playwright (Python)

Automatización de pruebas end-to-end para el sitio **Xtrim** utilizando  
**Python + Playwright + Pytest**, bajo el patrón **Page Object Model (POM)**.

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Playwright-Automation-green?style=for-the-badge&logo=playwright">
<img src="https://img.shields.io/badge/Pytest-Framework-orange?style=for-the-badge&logo=pytest">
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge">

</div>

---

# 📚 Tabla de Contenidos
- [📘 Descripción del Proyecto](#-descripción-del-proyecto)
- [📂 Estructura del Proyecto](#-estructura-del-proyecto)
- [🧪 Pruebas Implementadas](#-pruebas-implementadas)
- [⚙️ Instalación del Entorno](#️-instalación-del-entorno)
- [▶️ Ejecución de las Pruebas](#️-ejecución-de-las-pruebas)
- [🧱 Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [🧩 Configuración Global](#-configuración-global)
- [🏗️ Arquitectura POM](#️-arquitectura-pom)
- [📸 Screenshots y Depuración](#-screenshots-y-depuración)
- [📄 Autor](#-autor)

---

# 📘 Descripción del Proyecto

Este proyecto contiene pruebas automatizadas **E2E** para funcionalidades clave del sitio:

👉 https://www.xtrim.com.ec/

Las pruebas simulan la interacción real de un usuario en:

- Formulario **"Te llamamos"**  
- Sección **"Pagar Servicio"**  
- Flujos de **Zapping → Selección de plan**  

Todas las pruebas están diseñadas bajo el enfoque **Page Object Model**, asegurando:

- Código limpio  
- Escalabilidad  
- Reutilización de componentes  
- Fácil mantenimiento  

---

# 📂 Estructura del Proyecto
```bash
mi-proyecto-automatizado/
│
├── README.md
├── requirements.txt
├── pytest.ini
│
├── utils/
│ └── config.py
│
├── pages/
│ ├── home_page.py
│ ├── contacto_page.py
│ ├── pagar_page.py
│ └── planes_page.py
│
└── tests/
├── test_contacto.py
├── test_pagar_servicio.py
└── test_planes.py
```

---

# 🧪 Pruebas Implementadas

### ✅ **1. Formulario “Te llamamos”**
Ruta: `tests/test_contacto.py`

Valida:
- Acceso al formulario
- Llenado de datos
- Envío exitoso
- Redirección al landing correcto

---

### ✅ **2. Pagar Servicio**
Ruta: `tests/test_pagar_servicio.py`

Valida:
- Acceso al menú
- Compatibilidad escritorio/móvil
- Apertura del dominio de pagos  
- Manejo de nueva pestaña o la misma

---

### ✅ **3. Zapping – Selección de Plan**
Ruta: `tests/test_planes.py`

Flujo **replicado exactamente del Selenium IDE**:

- Click directo en Zapping (menú principal)  
- Selección del plan usando el selector exportado  
- Validación del landing del plan  

---

# ⚙️ Instalación del Entorno

### 🔹 1. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```
### 🔹 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 🔹 3. Instalar navegadores Playwright

```bash
playwright install
```

---

# ▶️ Ejecución de las Pruebas

### Ejecutar todos los tests:
```bash
pytest -v --headed
```

### Ejecutar un test en específico:
```bash
pytest tests/test_pagar_servicio.py --headed
```

### Modo headless (sin UI):
```bash
pytest -v
```

---

# 🏗️ Arquitectura POM

| Página       | Archivo            | Descripción                       |
|--------------|--------------------|-----------------------------------|
| HomePage     | `home_page.py`     | Menú, navegación, popups, accesos |
| ContactoPage | `contacto_page.py` | Formulario “Te llamamos”          |
| PagarPage    | `pagar_page.py`    | Validación del landing de pagos   |
| PlanesPage   | `planes_page.py`   | Selección del plan Zapping        |