# 🎲 Montecarlo sobre Montecarlo

Simulación estadística de máquinas tipo *pick-one* usando métodos de Monte Carlo anidados y multiprocessing en Python.

---

## 📖 Descripción

Las *pick-one machines* (máquinas de “elige una opción”) representan un modelo simple de juego de azar:

- El jugador elige una posición fija.
- La máquina selecciona una posición aleatoria.
- Solo hay ganancia si ambas coinciden.
- Cada intento tiene un costo fijo y un premio asociado.

Este proyecto modela una de estas máquinas y analiza su comportamiento estadístico utilizando **Monte Carlo sobre Monte Carlo**:

1. **Monte Carlo interno**  
   Para un número fijo de repeticiones \( N \), se simula el juego y se estima la ganancia promedio.

2. **Búsqueda del N óptimo**  
   Se evalúan todos los valores \( N = 1, \dots, 100 \) y se identifica el que maximiza la ganancia promedio observada.

3. **Monte Carlo externo**  
   Todo el proceso anterior se repite miles de veces para construir una distribución estadística del:
   - Número óptimo de repeticiones \( N^* \)
   - Valor de la ganancia promedio máxima

4. **Paralelización**  
   Se utiliza `multiprocessing` para acelerar los cálculos, ejecutando simulaciones independientes en múltiples núcleos del procesador.

---

## 🎯 Objetivo

El objetivo principal es estudiar cómo:
- La ganancia muestral fluctúa alrededor de su esperanza teórica
- El tamaño de muestra afecta la estabilidad de los resultados
- La “mejor estrategia” emerge como una propiedad estadística, no determinista

---

## 🧮 Modelo del juego

- Costo por jugada: **1 moneda**
- Probabilidad de acierto: **1/8**
- Premios por posición:

| Posición | Premio |
|--------:|-------:|
| 1 | 5 |
| 2 | 10 |
| 3 | 15 |
| 4 | 20 |
| 5 | 20 |
| 6 | 30 |
| 7 | 30 |
| 8 | 100 |

Ganancia por jugada:
\[
G = \text{premio} - \text{costo}
\]

---

## ⚙️ Requisitos

- Python 3.8+
- NumPy
- Matplotlib

Instalación de dependencias:

```bash
pip install numpy matplotlib
```

## ▶️ Ejecución

```bash
python main.py
```

Durante la ejecución:

* El usuario elige la posición a apostar.
* El programa ejecuta miles de experimentos en paralelo.
* Se muestran estadísticas y una gráfica final.

⚠️ **Advertencia**
Este programa utiliza todos los núcleos disponibles del procesador.
Con `REPETICIONES = 5000` y `MAX_N = 100`, el cálculo puede ser intensivo.

---

## 📊 Resultados

El programa produce:

* Número promedio de iteraciones óptimas ( \langle N^* \rangle )
* Ganancia promedio asociada
* Gráfica de dispersión con:

  * Línea de referencia en ganancia cero
  * Mapa de color según la ganancia promedio

---

## 🔬 Conclusiones

Bajo el supuesto de aleatoriedad pura:

* Apostar por premios altos tiende a maximizar la ganancia promedio observada
* El número óptimo de repeticiones se concentra alrededor de ( N \approx 8 )
* La estrategia óptima no es determinista, sino estadística

---

## 🚀 Extensiones futuras

* Cambiar probabilidades por posición
* Introducir máquinas no completamente aleatorias
* Analizar esperanza teórica vs simulación
* Simular estrategias adaptativas
* Añadir intervalos de confianza

---

## 📜 Licencia

MIT License

---

## ✍️ Autor

Daniel Ramírez
Física · Análisis de datos · Desarrollador de Software
