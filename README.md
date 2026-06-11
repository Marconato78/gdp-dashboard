# 🌎 GDP Dashboard Template
https://gdp-dashboard-template.streamlit.app/

Plantilla de aplicación web desarrollada con **Streamlit** para la visualización y análisis de indicadores económicos.

El proyecto sirve como ejemplo de referencia para la creación de dashboards interactivos basados en datos estructurados, utilizando Python y Streamlit como única tecnología de desarrollo frontend y backend.

---

## Descripción

Esta aplicación demuestra cómo construir cuadros de mando interactivos mediante Streamlit para explorar y visualizar información estadística.

La plantilla está diseñada para servir como punto de partida para:

* Dashboards empresariales.
* Aplicaciones de Business Intelligence.
* Herramientas de análisis económico.
* Visualización de series temporales.
* Exploración de datasets tabulares.

---

## Arquitectura

El proyecto sigue una arquitectura ligera basada en una única aplicación Streamlit.

```text
gdp-dashboard-template/
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

### Componentes principales

| Archivo            | Descripción                       |
| ------------------ | --------------------------------- |
| `streamlit_app.py` | Punto de entrada de la aplicación |
| `requirements.txt` | Dependencias del proyecto         |
| `README.md`        | Documentación del repositorio     |

---

## Características Técnicas

### Interfaz Reactiva

La aplicación utiliza el motor reactivo de Streamlit para actualizar automáticamente la interfaz en función de las acciones del usuario.

### Visualización de Datos

La plantilla está preparada para integrar componentes como:

```python
st.dataframe()
st.metric()
st.line_chart()
st.bar_chart()
st.selectbox()
st.slider()
```

Estos elementos permiten construir dashboards interactivos sin necesidad de frameworks frontend externos.

---

### Procesamiento de Datos

La aplicación puede integrarse fácilmente con:

* Archivos CSV.
* Archivos Excel.
* APIs REST.
* Bases de datos SQL.
* Almacenes de datos empresariales.

---

## Requisitos

### Software

* Python 3.9 o superior
* pip

### Dependencias

Las dependencias del proyecto se encuentran definidas en:

```text
requirements.txt
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone <repositorio>
cd gdp-dashboard-template
```

### 2. Crear un entorno virtual (recomendado)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución

Iniciar la aplicación localmente:

```bash
streamlit run streamlit_app.py
```

Por defecto, Streamlit expondrá la aplicación en:

```text
http://localhost:8501
```

---

## Desarrollo

La aplicación aprovecha la recarga automática de Streamlit, permitiendo visualizar cambios en tiempo real durante el desarrollo.

Esto facilita la construcción rápida de prototipos analíticos y dashboards de datos.

---

## Despliegue

Compatible con:

* Streamlit Community Cloud
* Docker
* Kubernetes
* AWS
* Azure
* Google Cloud
* Servidores Linux tradicionales

---

## Tecnologías Utilizadas

* Python
* Streamlit
* Pandas
* NumPy
* Bibliotecas de visualización compatibles con Streamlit

---

## Casos de Uso

Esta plantilla puede utilizarse para:

* Dashboards financieros.
* Informes ejecutivos.
* Seguimiento de KPIs.
* Visualización de datos económicos.
* Herramientas de Business Intelligence.
* Cuadros de mando corporativos.

---

## Ventajas de la Arquitectura

* Desarrollo rápido.
* Mantenimiento sencillo.
* Despliegue simplificado.
* Escalabilidad adecuada para aplicaciones analíticas.
* Integración sencilla con múltiples fuentes de datos.
* Ausencia de dependencias frontend complejas.

---

## Licencia

Este proyecto puede utilizarse como plantilla base para aplicaciones analíticas desarrolladas con Streamlit.
