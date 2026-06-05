# 🌡️ Convertidor de Temperatura · DEN

Aplicativo web construido con **Python + Streamlit** para convertir valores de temperatura entre las escalas **Celsius (°C)**, **Fahrenheit (°F)** y **Kelvin (K)**.

---

## 📁 Estructura del repositorio

```
/
├── app.py              ← Código principal de la aplicación
├── requirements.txt    ← Dependencias Python
└── README.md           ← Este archivo
```

---

## 🚀 Despliegue en Streamlit Cloud (paso a paso)

### 1. Subir archivos a GitHub

1. Creá un repositorio nuevo en [github.com](https://github.com) (público o privado).
2. Subí los tres archivos: `app.py`, `requirements.txt` y `README.md`.
   - Podés hacerlo desde la interfaz web de GitHub → **Add file → Upload files**
   - O desde la terminal:
     ```bash
     git init
     git add .
     git commit -m "Initial commit - Convertidor de Temperatura DEN"
     git branch -M main
     git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
     git push -u origin main
     ```

### 2. Conectar con Streamlit Cloud

1. Ingresá a [share.streamlit.io](https://share.streamlit.io) con tu cuenta de GitHub.
2. Hacé clic en **"New app"**.
3. Completá el formulario:
   | Campo | Valor |
   |-------|-------|
   | **Repository** | `TU_USUARIO/TU_REPO` |
   | **Branch** | `main` |
   | **Main file path** | `app.py` |
4. Hacé clic en **"Deploy!"**
5. En 1–2 minutos tu app estará disponible en una URL del tipo:
   `https://TU_USUARIO-TU_REPO-app-XXXX.streamlit.app`

---

## 💻 Correr localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
streamlit run app.py
```

La app se abre automáticamente en `http://localhost:8501`

---

## ✨ Funcionalidades

- Conversión bidireccional entre **°C**, **°F** y **K**
- Selector de escala de entrada
- Validación de **cero absoluto** (−273.15 °C / 0 K)
- Fórmulas aplicadas en tiempo real
- **8 referencias rápidas** clicables (cuerpo humano, ebullición, FLIR, etc.)
- **Tabla de referencia** descargable como CSV
- Pestaña de fórmulas e información técnica

---

## 🛠 Stack

| Tecnología | Uso |
|-----------|-----|
| Python 3.9+ | Lógica de conversión |
| Streamlit 1.32+ | Framework de UI web |
| Pandas | Tabla de referencia y exportación CSV |

---

*DEN — Herramienta Conversión de Unidades*
