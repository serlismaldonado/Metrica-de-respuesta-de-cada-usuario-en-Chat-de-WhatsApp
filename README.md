
Experimento con 🐍 [#Python](https://www.linkedin.com/feed/hashtag/?keywords=python&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7078239451197403136)  
  

## Métrica de respuesta de cada usuario en Chat de WhatsApp (Versión 1.0)
No tenía nada más que hacer 😁 , así que me puse a pensar en cómo mejorar algunas habilidades con Python 🐍 , y concluí que podría (a manera de «entretenimiento»): Verificar quién de nosotros (💛 mi pareja y yo), respondía los mensajes del otro más rápido.  
  
**Algunos problemas con los que me encontré:**  
  
1. No todos los registros tenían exactamente la misma orden; en algunos casos solo aparecía el mensaje, en otros solo el remitente, etc. 😪  
  
2. La conversión de texto a fechas resultó ser bastante tediosa, porque había que iterar y separar los mensajes, los contactos, las fechas, y la hora del día con separadores como: ":" y " ". Y luego, convertir de texto a cada uno de los tipos de datos que necesitaba. 😩  
  
**Entrada de datos:**  
  
- Archivo chat.txt con los datos exportados desde WhatsApp. (Nota importante: El archivo .txt lo exporté de un chat hace unos años, y lo comparé con uno más reciente, y encontré que el formato cambió ligeramente.)  
  
**⚙ Algunos procesos:**  
  
1. Separar los datos de cada mensaje de cada usuario.  
2. Obtener una lista de los últimos mensajes de cada usuario y la respuesta del otro usuario respectivamente, asumiendo que se podían enviar hilos de más de un mensaje por usuario.  
3. Conseguir el número de respuestas de cada usuario.  
4. Conseguir con una función aparte, la cantidad de segundos de cada respuesta, en relación con la respuesta de un usuario a otro.  
5. Calcular el promedio de respuesta de cada usuario teniendo en cuenta la cantidad de mensajes y el sumatorio de los segundos de esas respuestas.  
  
🎉 ¡Y voilà! 🎉  
  
**Obtuve un objeto como esto:**  
  
    [{'contact': 'Serlis Maldonado', 'ptr_in_minutes': '10.98'}, {'contact': 'Jessie Argueta', 'ptr_in_minutes': '15.08'}, {'quantity_messages': 7701}]  

  
El [#código](https://www.linkedin.com/feed/hashtag/?keywords=c%C3%B3digo&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7078239451197403136) no está exento de errores, eso seguro. Quizá utilizar una librería específica como [#NumPy](https://www.linkedin.com/feed/hashtag/?keywords=numpy&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7078239451197403136), ¡Que sé yo! 🤣. Lo cierto es que algo aprendí de este pequeño experimento de 2 días.  
  
Trataré de dejar repositorio de esto 👽 por si quieres refactorizar el código. Si llegaste hasta aquí, gracias por leerlo completo. 🎓
