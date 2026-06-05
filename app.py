import streamlit as st
import math

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Convertidor de Temperatura · DEN",
    page_icon="🌡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Estilos personalizados ───────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700&family=DM+Mono:wght@400;500&display=swap');

/* Fondo y tipografía general */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

/* Fondo oscuro */
.stApp {
    background-color: #0f1117;
    background-image:
        linear-gradient(rgba(255,255,255,0.018) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.018) 1px, transparent 1px);
    background-size: 40px 40px;
}

/* Ocultar toolbar de Streamlit */
#MainMenu, footer, header { visibility: hidden; }

/* Inputs numéricos */
input[type="number"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 1.6rem !important;
    font-weight: 500 !important;
    background-color: #181c27 !important;
    color: #e8eaf0 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    padding: 0.6rem 1rem !important;
}
input[type="number"]:focus {
    border-color: hsl(215,75%,62%) !important;
    box-shadow: 0 0 0 1px hsl(215,75%,62%) !important;
}

/* Botones de referencia */
.stButton > button {
    background-color: #181c27 !important;
    color: #7c8099 !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 10px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    transition: all 0.15s !important;
    width: 100% !important;
}
.stButton > button:hover {
    border-color: rgba(255,255,255,0.18) !important;
    color: #e8eaf0 !important;
    background-color: #1e2333 !important;
}

/* Selectbox */
.stSelectbox [data-baseweb="select"] > div {
    background-color: #181c27 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
    font-family: 'Syne', sans-serif !important;
}

/* Métricas */
[data-testid="metric-container"] {
    background-color: #181c27;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1rem 1.25rem;
}
[data-testid="metric-container"] label {
    color: #7c8099 !important;
    font-size: 0.68rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    font-family: 'Syne', sans-serif !important;
}
[data-testid="stMetricValue"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 1.8rem !important;
    font-weight: 500 !important;
    color: #e8eaf0 !important;
}
[data-testid="stMetricDelta"] { display: none; }

/* Divisores */
hr { border-color: rgba(255,255,255,0.07) !important; margin: 1.5rem 0 !important; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background-color: #181c27 !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    padding: 4px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    color: #7c8099 !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
}
.stTabs [aria-selected="true"] {
    background-color: #1e2333 !important;
    color: #e8eaf0 !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding-top: 1.25rem !important;
}

/* Alertas / info */
.stAlert {
    background-color: hsla(355,75%,62%,0.10) !important;
    border: 1px solid hsla(355,75%,62%,0.25) !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
}

/* Texto general */
p, li, span, div {
    color: #e8eaf0;
}

.formula-box {
    background: #181c27;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.9;
    color: #7c8099;
    margin-top: 0.5rem;
}
.formula-box .hl-c  { color: hsl(20, 80%, 65%); }
.formula-box .hl-f  { color: hsl(215, 75%, 65%); }
.formula-box .hl-k  { color: hsl(158, 65%, 55%); }

.header-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #181c27;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 100px;
    padding: 4px 14px;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7c8099;
    margin-bottom: 0.75rem;
    font-family: 'Syne', sans-serif;
}
.dot-green {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: hsl(158,65%,52%);
    display: inline-block;
    box-shadow: 0 0 5px hsl(158,65%,52%);
    margin-right: 2px;
}
.scale-card {
    border-radius: 16px;
    padding: 1.1rem 1.25rem 0.9rem;
    border: 1px solid rgba(255,255,255,0.07);
    margin-bottom: 0.75rem;
}
.sc-c  { background: hsla(20,80%,60%,0.07);  border-color: hsla(20,80%,60%,0.20); }
.sc-f  { background: hsla(215,75%,62%,0.07); border-color: hsla(215,75%,62%,0.20); }
.sc-k  { background: hsla(158,65%,52%,0.07); border-color: hsla(158,65%,52%,0.20); }
.scale-label {
    font-size: 0.68rem; font-weight: 600;
    letter-spacing: 0.1em; text-transform: uppercase;
    margin-bottom: 0.2rem; font-family: 'Syne', sans-serif;
}
.lbl-c { color: hsl(20,80%,65%); }
.lbl-f { color: hsl(215,75%,65%); }
.lbl-k { color: hsl(158,65%,55%); }
.scale-val {
    font-family: 'DM Mono', monospace;
    font-size: 2rem; font-weight: 500;
    color: #e8eaf0; line-height: 1;
}
.scale-unit {
    font-size: 0.72rem; color: #7c8099;
    font-family: 'Syne', sans-serif; margin-top: 2px;
}
.ref-pill {
    display: inline-block;
    background: #181c27;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 100px;
    padding: 3px 12px;
    font-size: 0.72rem;
    font-family: 'DM Mono', monospace;
    color: #7c8099;
    margin: 3px;
}
.footer-den {
    text-align: center;
    font-size: 0.7rem;
    color: #3a3f55;
    letter-spacing: 0.08em;
    margin-top: 2.5rem;
    font-family: 'Syne', sans-serif;
}
</style>
""", unsafe_allow_html=True)


# ── Funciones de conversión ──────────────────────────────────────────────────
def c_to_f(c: float) -> float:
    return c * 9 / 5 + 32

def c_to_k(c: float) -> float:
    return c + 273.15

def f_to_c(f: float) -> float:
    return (f - 32) * 5 / 9

def k_to_c(k: float) -> float:
    return k - 273.15

CERO_ABSOLUTO_C = -273.15

def fmt(n: float, decimals: int = 4) -> str:
    """Formatea un número eliminando ceros finales innecesarios."""
    return f"{round(n, decimals):g}"


# ── Referencias rápidas ──────────────────────────────────────────────────────
REFERENCIAS = [
    {"nombre": "Cero absoluto",      "c": -273.15},
    {"nombre": "Fusión del hielo",   "c": 0.0},
    {"nombre": "Cuerpo humano",      "c": 37.0},
    {"nombre": "Ebullición H₂O",     "c": 100.0},
    {"nombre": "Leidenfrost",        "c": 185.0},
    {"nombre": "Zona crítica FLIR",  "c": 220.0},
    {"nombre": "Superficie de Venus","c": 464.0},
    {"nombre": "Hierro fundido",     "c": 1538.0},
]


# ── Estado de sesión ─────────────────────────────────────────────────────────
if "valor_c" not in st.session_state:
    st.session_state["valor_c"] = 0.0
if "escala_origen" not in st.session_state:
    st.session_state["escala_origen"] = "Celsius (°C)"


# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 1.5rem 0 0.5rem;">
  <div class="header-badge">
    <span class="dot-green"></span>
    Herramienta Conversión de Unidades
  </div>
  <h1 style="font-family:'Syne',sans-serif; font-size:2.2rem; font-weight:700;
             letter-spacing:-0.03em; color:#e8eaf0; margin:0; line-height:1.1;">
    Temperatura
  </h1>
  <p style="color:#7c8099; font-size:0.88rem; margin-top:0.4rem; font-family:'Syne',sans-serif;">
    Convertidor entre °C · °F · K
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Tabs: Conversor / Tabla / Acerca ─────────────────────────────────────────
tab_conv, tab_tabla, tab_info = st.tabs([
    "🌡️  Conversor",
    "📋  Tabla de referencia",
    "ℹ️  Fórmulas",
])


# ═══════════════════════════════════════════════════════════════════
# TAB 1 — CONVERSOR
# ═══════════════════════════════════════════════════════════════════
with tab_conv:

    # Selección de escala de entrada
    escala = st.selectbox(
        "Escala de entrada",
        ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"],
        key="escala_origen",
        label_visibility="collapsed",
    )

    col_input, col_spacer = st.columns([3, 1])
    with col_input:
        if escala == "Celsius (°C)":
            valor = st.number_input(
                "Valor en °C", value=st.session_state["valor_c"],
                format="%.4f", step=1.0,
                label_visibility="collapsed",
            )
            c_val = valor

        elif escala == "Fahrenheit (°F)":
            valor_f = st.number_input(
                "Valor en °F", value=c_to_f(st.session_state["valor_c"]),
                format="%.4f", step=1.0,
                label_visibility="collapsed",
            )
            c_val = f_to_c(valor_f)

        else:  # Kelvin
            valor_k = st.number_input(
                "Valor en K", value=c_to_k(st.session_state["valor_c"]),
                format="%.4f", step=1.0,
                label_visibility="collapsed",
            )
            c_val = k_to_c(valor_k)

    # Guardar °C equivalente en sesión
    st.session_state["valor_c"] = c_val

    # Validación cero absoluto
    if c_val < CERO_ABSOLUTO_C:
        st.error(f"⚠️ Por debajo del cero absoluto ({CERO_ABSOLUTO_C} °C / 0 K). Valor físicamente imposible.")
        st.stop()

    # Calcular los tres valores
    res_c = c_val
    res_f = c_to_f(c_val)
    res_k = c_to_k(c_val)

    st.markdown("---")

    # Tarjetas de resultado
    st.markdown(f"""
    <div class="scale-card sc-c">
      <div class="scale-label lbl-c">● Celsius</div>
      <div class="scale-val">{fmt(res_c)} °C</div>
      <div class="scale-unit">grados Celsius</div>
    </div>
    <div class="scale-card sc-f">
      <div class="scale-label lbl-f">● Fahrenheit</div>
      <div class="scale-val">{fmt(res_f)} °F</div>
      <div class="scale-unit">grados Fahrenheit</div>
    </div>
    <div class="scale-card sc-k">
      <div class="scale-label lbl-k">● Kelvin</div>
      <div class="scale-val">{fmt(res_k)} K</div>
      <div class="scale-unit">escala absoluta · 0 K = cero absoluto</div>
    </div>
    """, unsafe_allow_html=True)

    # Fórmulas aplicadas
    if escala == "Celsius (°C)":
        f1 = f'<span class="hl-f">°F = ({fmt(res_c)} × 9/5) + 32 = {fmt(res_f)} °F</span>'
        f2 = f'<span class="hl-k">K  = {fmt(res_c)} + 273.15 = {fmt(res_k)} K</span>'
    elif escala == "Fahrenheit (°F)":
        f1 = f'<span class="hl-c">°C = ({fmt(res_f)} − 32) × 5/9 = {fmt(res_c)} °C</span>'
        f2 = f'<span class="hl-k">K  = {fmt(res_c)} + 273.15 = {fmt(res_k)} K</span>'
    else:
        f1 = f'<span class="hl-c">°C = {fmt(res_k)} − 273.15 = {fmt(res_c)} °C</span>'
        f2 = f'<span class="hl-f">°F = ({fmt(res_c)} × 9/5) + 32 = {fmt(res_f)} °F</span>'

    st.markdown(f'<div class="formula-box">{f1}<br>{f2}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Referencias rápidas
    st.markdown(
        "<p style='font-size:0.7rem;font-weight:600;letter-spacing:0.1em;"
        "text-transform:uppercase;color:#7c8099;margin-bottom:0.6rem;'>"
        "Referencias rápidas</p>",
        unsafe_allow_html=True,
    )

    cols_ref = st.columns(4)
    for i, ref in enumerate(REFERENCIAS):
        with cols_ref[i % 4]:
            label = f"{ref['nombre']}\n{ref['c']}°C"
            if st.button(label, key=f"ref_{i}"):
                st.session_state["valor_c"] = ref["c"]
                st.rerun()


# ═══════════════════════════════════════════════════════════════════
# TAB 2 — TABLA DE REFERENCIA
# ═══════════════════════════════════════════════════════════════════
with tab_tabla:
    st.markdown(
        "<p style='font-size:0.75rem;color:#7c8099;margin-bottom:1rem;'>"
        "Puntos de referencia comunes en las tres escalas.</p>",
        unsafe_allow_html=True,
    )

    puntos = [
        ("Cero absoluto",       -273.15),
        ("Nitrógeno líquido",   -196.0),
        ("CO₂ sólido (hielo seco)", -78.5),
        ("Fusión del hielo",    0.0),
        ("Cuerpo humano",       37.0),
        ("Ebullición H₂O",      100.0),
        ("Leidenfrost",         185.0),
        ("Zona crítica FLIR ΔT",220.0),
        ("Plomo fundido",       327.5),
        ("Superficie de Venus", 464.0),
        ("Hierro fundido",      1538.0),
        ("Superficie del Sol",  5505.0),
    ]

    import pandas as pd
    df = pd.DataFrame([
        {
            "Referencia": p[0],
            "°C": fmt(p[1]),
            "°F": fmt(c_to_f(p[1])),
            "K":  fmt(c_to_k(p[1])),
        }
        for p in puntos
    ])

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Referencia": st.column_config.TextColumn("Referencia", width="large"),
            "°C": st.column_config.TextColumn("°C"),
            "°F": st.column_config.TextColumn("°F"),
            "K":  st.column_config.TextColumn("K"),
        },
    )

    # Descarga CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇ Descargar tabla como CSV",
        data=csv,
        file_name="referencias_temperatura_DEN.csv",
        mime="text/csv",
    )


# ═══════════════════════════════════════════════════════════════════
# TAB 3 — FÓRMULAS E INFO
# ═══════════════════════════════════════════════════════════════════
with tab_info:
    st.markdown("""
<div style="font-family:'Syne',sans-serif; color:#e8eaf0; line-height:1.8;">

<h3 style="font-size:1rem; font-weight:700; margin-bottom:0.5rem; color:hsl(20,80%,65%);">
  Celsius → Fahrenheit / Kelvin
</h3>
</div>
""", unsafe_allow_html=True)

    st.code("°F = (°C × 9/5) + 32\nK  = °C + 273.15", language="text")

    st.markdown("""
<div style="font-family:'Syne',sans-serif; color:#e8eaf0; line-height:1.8; margin-top:1rem;">
<h3 style="font-size:1rem; font-weight:700; margin-bottom:0.5rem; color:hsl(215,75%,65%);">
  Fahrenheit → Celsius / Kelvin
</h3>
</div>
""", unsafe_allow_html=True)

    st.code("°C = (°F − 32) × 5/9\nK  = (°C resultante) + 273.15", language="text")

    st.markdown("""
<div style="font-family:'Syne',sans-serif; color:#e8eaf0; line-height:1.8; margin-top:1rem;">
<h3 style="font-size:1rem; font-weight:700; margin-bottom:0.5rem; color:hsl(158,65%,55%);">
  Kelvin → Celsius / Fahrenheit
</h3>
</div>
""", unsafe_allow_html=True)

    st.code("°C = K − 273.15\n°F = (°C resultante × 9/5) + 32", language="text")

    st.markdown("""
<hr style="border-color:rgba(255,255,255,0.07); margin: 1.5rem 0;">
<div style="font-size:0.78rem; color:#7c8099; font-family:'Syne',sans-serif; line-height:1.8;">
  <strong style="color:#e8eaf0;">Cero absoluto:</strong> −273.15 °C / 0 K / −459.67 °F<br>
  Es el límite inferior teórico de temperatura. Por debajo de este valor no existe temperatura física posible.<br><br>
  <strong style="color:#e8eaf0;">Kelvin</strong> es la unidad del Sistema Internacional (SI). No usa el símbolo °.<br>
  <strong style="color:#e8eaf0;">Celsius</strong> define 0°C = fusión del hielo y 100°C = ebullición del agua (a 1 atm).<br>
  <strong style="color:#e8eaf0;">Fahrenheit</strong> es la escala oficial de EE.UU. y algunos territorios insulares.
</div>
""", unsafe_allow_html=True)


# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown('<div class="footer-den">DEN</div>', unsafe_allow_html=True)
