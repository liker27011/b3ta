# 🐍 Aprendiendo Python desde Cero

> Repositorio personal para aprender Python paso a paso: desde su historia hasta ejecutar proyectos con entorno virtual.

---

## 📘 Breve Historia de Python

Python fue creado por **Guido van Rossum** y su primera versión fue publicada en 1991. El nombre se inspiró en el grupo de comedia británico *Monty Python's Flying Circus*. Desde sus inicios, Python ha sido reconocido por su:

- Sintaxis limpia y legible 🧼  
- Filosofía de legibilidad y productividad 🧠  
- Comunidad activa y miles de librerías disponibles 🌐

Actualmente, es uno de los lenguajes más populares en el mundo del desarrollo web, análisis de datos, inteligencia artificial, automatización, y más.

---

## 💻 Instalación de Python

1. Ve a la página oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Descarga la versión más reciente para tu sistema operativo.
3. Durante la instalación en Windows, **activa la opción** ✅ `Add Python to PATH`.
4. Verifica la instalación con el siguiente comando en la terminal o consola:

```bash
python --version
```

---

## 🧠 Tipos de Datos en Python

| Tipo de Dato | Ejemplo              | Descripción                        | Nomenclatura recomendada |
|--------------|----------------------|------------------------------------|---------------------------|
| `int`        | `10`, `-3`, `0`      | Números enteros                    | `edad`, `contador`        |
| `float`      | `3.14`, `-0.5`       | Números decimales                  | `altura`, `precio`        |
| `str`        | `"Hola"`, `'Python'` | Cadenas de texto                   | `nombre`, `mensaje`       |
| `bool`       | `True`, `False`      | Valores booleanos (verdadero/falso)| `activo`, `es_valido`     |
| `list`       | `[1, 2, 3]`          | Lista ordenada y mutable           | `numeros`, `colores`      |
| `tuple`      | `(1, 2)`             | Tupla (lista inmutable)            | `coordenadas`, `fecha`    |
| `dict`       | `{"clave": "valor"}` | Diccionario de pares clave-valor   | `persona`, `datos`        |

---

## ⚙️ Entorno Virtual en Python

Crear un entorno virtual te permite trabajar en proyectos aislados, sin afectar otras configuraciones de tu sistema.

### 🔨 Crear el entorno virtual

```bash
python -m venv venv
```

Esto crea una carpeta `venv/` con los archivos del entorno.

---

### 🚀 Activar entorno virtual

- **Windows**:

```bash
venv\Scripts\activate
```

- **Linux / macOS**:

```bash
source venv/bin/activate
```

Cuando el entorno está activo, verás el nombre `venv` al inicio de tu terminal.

---

### ❌ Desactivar entorno virtual

```bash
deactivate
```

---

## 📁 Estructura del Repositorio

```
📦 python-aprendizaje
├── README.md
├── historia_python.py
├── tipos_datos.py
├── entorno_virtual.md
├── ejemplos/
│   ├── variables.py
│   └── entrada_salida.py
└── venv/ (ignorada en Git)
```

> ⚠️ Recuerda agregar `venv/` a tu archivo `.gitignore` para evitar subir el entorno virtual al repositorio.

---

## 🧪 Ejemplos Básicos

### `variables.py`

```python
# Ejemplo de declaración de variables
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

print(f"{nombre} tiene {edad} años, mide {altura}m y su estado estudiantil es {es_estudiante}")
```

---

### `entrada_salida.py`

```python
# Entrada de datos por consola
nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre)
```

---

## 📌 Próximos temas

- ✅ Condicionales (`if`, `else`, `elif`)
- 🔁 Bucles (`for`, `while`)
- 🧰 Funciones y argumentos
- 🗃️ Módulos y paquetes
- 📂 Lectura y escritura de archivos
- 🧪 Manejo de errores con `try/except`

---

## 🙌 Contribuciones

¿Quieres ayudar a mejorar este repositorio?  
Puedes contribuir creando ejercicios, corrigiendo errores o sugiriendo nuevos temas.  
¡Haz un fork y luego un pull request!

---

## 📬 Contacto

📧 Autor: [TuNombre]  
🐙 GitHub: [https://github.com/TuUsuario](https://github.com/TuUsuario)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.  
Puedes usarlo, copiarlo o adaptarlo libremente.

---
