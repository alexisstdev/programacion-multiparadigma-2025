# Reflexiones - Programacion Funcional

## 1. Que significa que una funcion sea "pura"?

Una funcion pura es aquella que siempre produce el mismo resultado cuando recibe los mismos datos de entrada, sin importar cuantas veces se ejecute. Ademas, no modifica nada fuera de si misma ni depende de informacion externa que pueda cambiar. Un ejemplo de la vida cotidiana seria una receta de cocina: si siempre usas los mismos ingredientes en las mismas cantidades, el resultado sera el mismo platillo. Si cambias un ingrediente o la cantidad, el resultado cambia de forma predecible.

## 2. Por que crear_transformador retorna una funcion en lugar de aplicar directamente la transformacion?

Retornar una funcion en lugar de aplicar directamente la transformacion permite crear funciones reutilizables y configurables. Este patron se llama "funcion de orden superior" y nos da flexibilidad para definir la transformacion una vez y aplicarla a diferentes listas despues. La ventaja es que podemos componer estas funciones en pipelines, como se hace con la funcion componer. Esto hace el codigo mas modular, ya que separamos la configuracion de la transformacion de su ejecucion.

## 3. Que dificultades encontraste al convertir codigo imperativo a funcional?

La mayor dificultad fue cambiar la forma de pensar: pasar de "como hacer algo paso a paso" a "que transformaciones aplicar a los datos". Fue complicado dejar de usar variables mutables y ciclos tradicionales para usar funciones que retornan nuevos valores. Tambien entender como las funciones pueden retornar otras funciones requirio practica para visualizar el flujo de datos. Lo resolvi practicando con ejemplos simples y trazando mentalmente que valor tiene cada variable en cada paso.

## 4. Analogia entre programacion imperativa y funcional

La programacion imperativa es como dar instrucciones paso a paso para armar un mueble: "toma el tornillo, insertalo aqui, gira tres veces, toma la siguiente pieza...". La programacion funcional es como describir el mueble final y las transformaciones necesarias: "estas piezas ensambladas de esta forma producen una mesa". En la imperativa controlas cada accion, mientras que en la funcional describes que quieres lograr y dejas que el sistema determine como hacerlo. La funcional se enfoca en transformar datos de entrada en datos de salida sin preocuparse por los pasos intermedios.