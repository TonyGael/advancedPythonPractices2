# Advanced Python Practices #2: decorators
Los decoradores en Python son funciones que se utilizan para modificar el comportamiento de otras funciones o métodos. Los decoradores se utilizan comúnmente para agregar funcionalidades adicionales a funciones existentes sin modificar su código.

Aquí tienes un ejemplo sencillo para entender cómo funcionan los decoradores en Python:

Supongamos que queremos crear un decorador que imprima un mensaje antes y después de llamar a una función:

```python
# Definimos el decorador
def mensaje(func):
    def wrapper():
        print("Antes de llamar a la función.")
        func()
        print("Después de llamar a la función.")
    return wrapper

# Definimos una función
def saludo():
    print("¡Hola, mundo!")

# Aplicamos el decorador a la función
saludo_decorado = mensaje(saludo)

# Llamamos a la función decorada
saludo_decorado()
```

En este ejemplo, hemos creado un decorador llamado `mensaje`. Este decorador toma una función como argumento (`func`) y define una función interna llamada `wrapper`, que envuelve a la función original. Dentro de `wrapper`, imprimimos un mensaje antes de llamar a la función (`func()`), y otro mensaje después de llamarla.

Luego, definimos una función `saludo`, que simplemente imprime "¡Hola, mundo!".

Finalmente, aplicamos el decorador `mensaje` a la función `saludo` mediante la línea `saludo_decorado = mensaje(saludo)`. Esto significa que `saludo_decorado` ahora es una versión de `saludo` que ha sido decorada con la funcionalidad adicional del decorador `mensaje`.

Cuando llamamos a `saludo_decorado()`, en realidad estamos llamando a la función `wrapper`, que a su vez llama a la función original `saludo` pero con la funcionalidad adicional del decorador.

La salida de este código sería:

```
Antes de llamar a la función.
¡Hola, mundo!
Después de llamar a la función.
```

Este es solo un ejemplo básico para comprender los decoradores en Python. Los decoradores pueden ser utilizados para una amplia variedad de propósitos, como la gestión de excepciones, la autenticación, el registro, la medición de tiempos, entre otros.