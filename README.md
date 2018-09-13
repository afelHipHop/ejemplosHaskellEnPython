# ejemplosHaskellEnPython
### Samuel Holguin 20161020044
### Andres Ramirez 20161020077
### Kevin Rocha 20161020086
## *Haskell*
Es un lenguaje de programación estandarizado multi-propósito puramente funcional (donde todo se hace con llamadas a funciones),  con semánticas no estrictas, ), perezoso (nada se hace hasta que es completamente necesario) y fuerte tipificación estática (los tipos los revisa el compilador, pero no hace falta declararlos).
## *Caracteristicas*
### Estáticamente tipado
Cada expresión en Haskell tiene un tipo que se determina en tiempo de compilación. Todos los tipos compuestos juntos por aplicación de función tienen que coincidir. Si no lo hacen, el programa será rechazado por el compilador. Los tipos se convierten no solo en una forma de garantía, sino en un lenguaje para expresar la construcción de programas.
### Puramente funcional
Cada función en Haskell es una función en el sentido matemático (es decir, "puro"). Incluso las operaciones IO de efecto secundario son solo una descripción de qué hacer, producidas por código puro. No hay instrucciones o instrucciones, solo expresiones que no pueden mutar variables (locales o globales) ni acceder al estado como el tiempo o números aleatorios.
### Concurrente
Haskell se presta bien a la programación simultánea debido a su manejo explícito de los efectos. Su compilador principal, GHC, viene con un recolector de basura paralela de alto rendimiento y una biblioteca de concurrencia liviana que contiene varias primitivas y abstracciones útiles de simultaneidad.
### Perezoso
Las funciones no evalúan sus argumentos. Esto significa que los programas pueden componer juntos muy bien, con la capacidad de escribir constructos de control (como if / else) simplemente escribiendo funciones normales. La pureza del código Haskell hace que sea fácil fusionar cadenas de funciones juntas, permitiendo beneficios de rendimiento.
### Paquetes
La contribución de código abierto a Haskell es muy activa con una amplia gama de paquetes disponibles en los servidores de paquetes públicos.
### links relacionados
[https://www.haskell.org/](https://www.haskell.org/)

[https://wiki.haskell.org/Aprende_Haskell_en_10_minutos](https://wiki.haskell.org/Aprende_Haskell_en_10_minutos)

                                                        
