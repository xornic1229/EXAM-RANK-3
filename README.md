# 42 Madrid - Exam Rank 03 Python

Repositorio de preparación para el **Exam Rank 03 de Python de 42 Madrid**.

Contiene soluciones de referencia y ejemplos de prueba para los ejercicios del examen. La idea es tener en un solo sitio los patrones más habituales para resolverlos rápido durante la práctica.

## Contenido

- [Estructura del repositorio](#estructura-del-repositorio)
- [Ejercicios](#ejercicios)
- [Uso](#uso)
- [Casos a comprobar](#casos-a-comprobar)

## Estructura del repositorio

```text
exam3/
├── ex1/
│   ├── bracket_validator.py
│   └── cryptic_sorter.py
├── ex2/
│   ├── echo_validator.py
│   └── mirror_matrix.py
├── ex3/
│   ├── hidenp.py
│   ├── inter.py
│   ├── number_base_converter.py
│   └── pattern_tracker.py
├── ex4/
│   ├── anagram.py
│   ├── shadow_merge.py
│   └── string_permutation_checker.py
├── ex5/
│   ├── string_sculpur.py
│   └── twist_sequence.py
├── ex6/
│   └── whisper_checker.py
└── README
```

## Ejercicios

### Ejercicio 1

**bracket_validator** comprueba si paréntesis, corchetes y llaves están bien emparejados y anidados.

```python
bracket_validator("()")
bracket_validator("([{}])")
bracket_validator("([)]")
bracket_validator("hello")
```

**cryptic_sorter** ordena una lista de cadenas por longitud, orden lexicográfico, número de vocales y valor original como desempate.

### Ejercicio 2

**echo_validator** comprueba si una cadena es un palíndromo ignorando mayúsculas, espacios y caracteres no alfabéticos.

**mirror_matrix** invierte horizontalmente cada fila de una matriz sin cambiar el orden de las filas.

### Ejercicio 3

**hidenp** verifica si una cadena aparece como subsecuencia de otra.

**inter** devuelve los caracteres comunes a dos cadenas sin repetirlos y conservando el orden de la primera.

**number_base_converter** convierte un número entre bases de 2 a 36 y devuelve `ERROR` si la entrada no es válida.

**pattern_tracker** cuenta pares consecutivos de dígitos donde el segundo es exactamente uno mayor que el primero.

### Ejercicio 4

**anagram** comprueba si dos cadenas son anagramas ignorando espacios y mayúsculas.

**shadow_merge** fusiona dos listas ordenadas en una sola lista ordenada conservando duplicados.

**string_permutation_checker** comprueba si dos cadenas son permutaciones exactas, distinguiendo espacios y mayúsculas.

### Ejercicio 5

**string_sculpur** alterna minúsculas y mayúsculas en una cadena sin modificar los caracteres no alfabéticos.

**twist_sequence** rota una lista hacia la derecha `k` posiciones.

### Ejercicio 6

**whisper_checker** aplica un cifrado César respetando mayúsculas, minúsculas y caracteres no alfabéticos.

## Uso

Cada solución puede probarse importándola desde otro archivo o ejecutando el módulo directamente.

```python
from ex3.inter import inter

print(inter("hello", "world"))
```

```python
if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))
```

```bash
python3 ex3/inter.py
```

## Casos a comprobar

Conviene probar, como mínimo:

- Entradas vacías.
- Un único elemento.
- Elementos repetidos.
- Mayúsculas y minúsculas.
- Espacios y caracteres especiales.
- Valores límite.
- Entradas ya ordenadas.
- Entradas completamente desordenadas.
- Casos válidos e inválidos.

## Objetivo

El objetivo del repositorio es practicar los patrones de resolución más comunes del examen y poder identificar rápidamente qué técnica aplicar en cada ejercicio.
