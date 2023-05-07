/*La función dropHandler(event) maneja la carga del archivo cuando se arrastra y se suelta un archivo en el área designada. Si el archivo es de tipo texto, se lee su contenido y se carga en un elemento de texto textarea. Si no es un archivo de texto, se muestra un mensaje de alerta.
La función borrar() borra el contenido del elemento de texto textarea.
La función calcular() extrae el contenido del textarea en una matriz de números y realiza algún cálculo con ella, actualizando el contenido del elemento de texto resultadoTextarea con el resultado.
La función finalizar() no está definida en el código proporcionado, por lo que no se puede comentar sobre su funcionalidad.
La función seleccionarArchivo() permite seleccionar un archivo a través de un cuadro de diálogo de selección de archivo.
La última sección del código utiliza un evento de cambio en un cuadro de diálogo de selección de archivo para cargar el archivo seleccionado en el textarea utilizando un FileReader.
La función leerMatriz hace lo mismo que dropHandler(); pero en español :D*/


function dropHandler(event) 
{
    event.preventDefault();
    var file = event.dataTransfer.files[0];
    if (file.type.match('text.*')) {
        var reader = new FileReader();
        reader.onload = function (event) {
            var content = event.target.result;
            var textarea = document.getElementById('dragdrop-textarea');
            textarea.value = content;
        };
        reader.readAsText(file);
    } else {
        alert('Solo se permiten archivos de texto');
    }
}

function borrar() 
{
var textarea = document.getElementById('dragdrop-textarea');
textarea.value = '';

}

function calcular() 
{
    // función para realizar el cálculo
}

function finalizar() 
{
    // función para finalizar la operación
}

function seleccionarArchivo() 
{
    // Hacer clic en el input de archivo
    document.getElementById("inputArchivo").click();
  }
  
  // Obtener el archivo seleccionado
  document.getElementById("inputArchivo").addEventListener("change", function() {
    var archivo = this.files[0];
  
    // Leer el contenido del archivo
    var lector = new FileReader();
    lector.onload = function(event) {
      // Asignar el contenido del archivo al textarea
      document.getElementById("dragdrop-textarea").value = event.target.result;
    };
    lector.readAsText(archivo);
  });

function calcular() 
{
var textarea = document.getElementById('dragdrop-textarea');
var matriz = textarea.value.split('\n').map(function (fila) {
return fila.split(' ').map(Number);
});

// Aquí puedes realizar el cálculo que necesites con la matriz

var resultado = 'Aquí va el resultado de la operación'; // Reemplaza esto con el resultado real

var resultadoTextarea = document.getElementById('resultado');
resultadoTextarea.value = resultado;
}

function leerMatriz() 
{
    const archivo = document.getElementById("inputArchivo").files[0];
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