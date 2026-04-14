# Unidad-2---Apuntes-Grafi


# Unidad 2: Graficación 2D

## 2.1 Transformación bidimensional

Las transformaciones bidimensionales son operaciones matemáticas que permiten modificar la posición, tamaño, orientación o forma de objetos en un plano 2D. Son fundamentales en gráficos por computadora, animación y desarrollo de videojuegos.

Las principales transformaciones son:

- Traslación  
- Escalamiento  
- Rotación  
- Sesgado  

---

## 2.1.1 Traslación

La traslación consiste en mover un objeto de una posición a otra sin alterar su forma, tamaño ni orientación.

### Fórmulas

```
x' = x + tx
y' = y + ty
```

### Donde

- (x, y) son las coordenadas originales  
- (tx, ty) es el desplazamiento  
- (x', y') son las nuevas coordenadas  

### Aplicación

Movimiento de objetos en pantalla, como en el control de un personaje usando teclas de dirección.

---

## 2.1.2 Escalamiento

El escalamiento modifica el tamaño de un objeto.

### Fórmulas

```
x' = x * sx
y' = y * sy
```

### Tipos

- Escalamiento uniforme: sx = sy  
- Escalamiento no uniforme: sx ≠ sy  

### Aplicación

Zoom, redimensionamiento de objetos o sprites.

---

## 2.1.3 Rotación

La rotación gira un objeto alrededor de un punto (generalmente el origen).

### Fórmulas

```
x' = x cos(θ) - y sin(θ)
y' = x sin(θ) + y cos(θ)
```

### Donde

- θ es el ángulo de rotación  

### Aplicación

Animaciones de giro y orientación de objetos.

---

## 2.1.4 Sesgado

El sesgado deforma un objeto inclinándolo.

### Fórmulas

```
x' = x + shx * y
y' = y + shy * x
```

### Aplicación

Efectos de perspectiva o deformación visual.

---

## 2.2 Representación matricial de las transformaciones bidimensionales

Las transformaciones pueden representarse mediante matrices, lo que permite combinar múltiples transformaciones en una sola operación.

Se utilizan coordenadas homogéneas:

### Vector

```
| x |
| y |
| 1 |
```

---

## 2.2.1 Matrices básicas

### Traslación

```
| 1  0  tx |
| 0  1  ty |
| 0  0  1  |
```

### Escalamiento

```
| sx  0   0 |
| 0   sy  0 |
| 0   0   1 |
```

### Rotación

```
| cosθ  -sinθ  0 |
| sinθ   cosθ  0 |
| 0      0     1 |
```

### Sesgado

```
| 1   shx  0 |
| shy 1    0 |
| 0   0    1 |
```

---

## 2.2.2 Aplicación práctica

Se implementó un sistema de control con teclado para mover un objeto en 2D:

- Flecha arriba → aumenta Y  
- Flecha abajo → disminuye Y  
- Flecha derecha → aumenta X  
- Flecha izquierda → disminuye X  

Esto utiliza la transformación de traslación.

---

## 2.3 Trazo de líneas curvas

Las curvas permiten representar formas suaves y complejas en gráficos 2D.

---

## 2.3.1 Curvas de Bézier

Las curvas de Bézier se definen mediante puntos de control.

### Fórmula general

```
B(t) = (1 - t)^2 P0 + 2(1 - t)t P1 + t^2 P2
```

### Características

- No pasan necesariamente por todos los puntos de control  
- Son fáciles de manipular  
- Muy usadas en diseño gráfico  

### Aplicaciones

- Diseño vectorial  
- Animaciones  
- Trayectorias suaves  

---

## 2.3.2 Curvas B-spline

Las curvas B-spline son una extensión de las curvas de Bézier.

### Forma general

```
C(t) = Σ Ni,k(t) Pi
```

Donde:

- Ni,k(t) son funciones base  
- Pi son puntos de control  

### Características

- Mayor control sobre la forma  
- Más estabilidad al modificar puntos  
- Curvas más suaves  

### Aplicaciones

- Modelado complejo  
- Animación avanzada  

---

## 2.3.3 Aplicación práctica

Se realizó una animación 2D donde un personaje (mapache) corre y salta.

### Características

- Uso de línea del tiempo  
- Movimiento continuo  
- Dibujos secuenciales  

---

## 2.4 Fractales

Los fractales son figuras geométricas con autosimilitud, es decir, su estructura se repite a diferentes escalas.

### Ejemplo (Mandelbrot)

```
z(n+1) = z(n)^2 + c
```

### Características

- Complejidad infinita  
- Generación mediante algoritmos  
- Detalle a cualquier nivel de zoom  

### Ejemplos

- Conjunto de Mandelbrot  
- Triángulo de Sierpinski  

### Aplicaciones

- Simulación de naturaleza  
- Arte digital  
- Gráficos por computadora  

---

## 2.5 Uso y creación de fuentes de texto

Las fuentes de texto son representaciones gráficas de caracteres.

### Tipos

- Bitmap (basadas en píxeles)  
- Vectoriales (basadas en curvas)  

Las fuentes vectoriales utilizan curvas como Bézier para definir las letras.

---

## 2.5.1 Proceso de creación

1. Diseño de caracteres  
2. Definición de curvas  
3. Ajuste de espaciado  
4. Exportación  

---

## 2.5.2 Aplicación

Uso de texto en gráficos, interfaces y animaciones, incluyendo herramientas como Blender.

---

# Ejercicios realizados

## 1. Control de objeto 2D con teclado

Se desarrolló un sistema para mover un objeto en pantalla.

### Características

- Movimiento en los ejes X y Y  
- Uso de eventos de teclado  
- Aplicación de traslación  

---

## 2. Animación con huesos en Blender

Se realizó una animación utilizando un sistema de huesos (armature).

### Conceptos aplicados

- Jerarquía de huesos  
- Transformaciones locales  
- Interpolación en línea del tiempo  

---

## 3. Animación 2D (mapache)

Se creó una animación donde un personaje corre y salta.

### Características

- Animación cuadro por cuadro  
- Uso de timeline  
- Movimiento fluido  
