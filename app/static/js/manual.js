/*La función agregarColumna() agrega una columna al final de cada fila de la tabla, y cada celda de esta nueva columna contiene un input HTML de tipo text con un tamaño de 5 caracteres.
La función agregarFila() agrega una fila al final de la tabla y cada celda en la fila contiene un input HTML de tipo text con un tamaño de 5 caracteres.
La función eliminarFila() elimina la última fila de la tabla si hay más de una fila. Primero, elimina todas las celdas de la última fila, y luego elimina la fila en sí.
La función borrarNumeros() limpia todos los valores de entrada de la tabla estableciéndolos en una cadena vacía.
La función finalizar() limpia todos los valores de entrada y el área de texto de salida.
La función eliminarColumna() elimina la última columna de la tabla si hay más de una columna. Elimina la última celda de cada fila que tenga más de una celda.*/

/*La función calcular() de momento solo suma los valores; pero al menos ya puede trabajar con números introducidos por el usuario*/

/*La función leerMatriz() intenta meter todos los valores dentro de una lista*/

var sum = 0;

function agregarColumna() 
{
    var matriz = document.getElementById("matriz");
    var filas = matriz.getElementsByTagName("tr");
    for (var i = 0; i < filas.length; i++) 
    {
        var celda = document.createElement("td");
        celda.innerHTML = '<input type="number" size="5" step="0.001" id = "entrada" />';
        filas[i].appendChild(celda);
    }
}
  
function agregarFila() 
{
    var matriz = document.getElementById("matriz");
    var numColumnas = matriz.getElementsByTagName("tr")[0].getElementsByTagName("td").length;
    var fila = document.createElement("tr");
    for (var i = 0; i < numColumnas; i++) 
    {
        var celda = document.createElement("td");
        celda.innerHTML = '<input type="number" size="5" step="0.001" id = "entrada" />';
        fila.appendChild(celda);
    }
    matriz.appendChild(fila);
}
  
function eliminarFila() 
{
    var matriz = document.getElementById("matriz");
    var ultimaFila = matriz.rows.length - 1;
    if (ultimaFila > 1) 
    {
        var ultimaColumna = matriz.rows[ultimaFila].getElementsByTagName("td").length - 1;
        for (var i = ultimaColumna; i >= 0; i--) 
        {
            matriz.rows[ultimaFila].deleteCell(i);
        }
        matriz.deleteRow(ultimaFila);
    }
}

function borrarNumeros() 
{
    var matriz = document.getElementById("matriz");
    var celdas = matriz.getElementsByTagName("td");
    for (var i = 0; i < celdas.length; i++) 
    {
        celdas[i].childNodes[0].value = "";
    }
}

function finalizar() 
{
    // Obtener elementos HTML
    var inputElements = document.querySelectorAll('input[type="text"]');
    var textareaElement = document.querySelector('textarea');
  
    // Limpiar valores de input y textarea
    for (var i = 0; i < inputElements.length; i++) 
    {
        inputElements[i].value = '';
    }
    textareaElement.value = '';
}
  
  
function eliminarColumna() 
{
    var matriz = document.getElementById("matriz");
    var filas = matriz.getElementsByTagName("tr");
    var ultimaColumna = filas[0].getElementsByTagName("td").length - 1;
    if (ultimaColumna > 0) 
    {
        for (var i = 0; i < filas.length; i++) 
        {
            if (filas[i].getElementsByTagName("td").length > 1) 
            {
                filas[i].deleteCell(ultimaColumna);
            }
        }
    }
}

function calcular()
{
    var matriz = document.getElementById("matriz");
    var columna = matriz.getElementsByTagName("td");
    for (let i = 0; i < columna.length; i++)
    {
        sum = sum + parseFloat(columna[i].childNodes[0].value);
    }
    console.log("columna[]: ", sum);
}

function leerMatriz() {
    const archivo = document.getElementById("matriz").files[0];
    const lector = new FileReader();
  
    lector.onload = function(evento) {
      const contenido = evento.target.result;
      const lineas = contenido.trim().split("\n");
      const matriz = [];
  
      for (let i = 0; i < lineas.length; i++) {
        const valores = lineas[i].trim().split(" ");
        matriz.push(valores.map((x) => parseInt(x)));
      }
  
      // Procesa la matriz como desees
      const resultado = matriz.map((fila) => fila.reverse());
  
      // Escribe el resultado en un archivo de texto
      escribirMatriz(resultado);
    };
  
    lector.readAsText(archivo);
  }