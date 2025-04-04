const { SerialPort } = require('serialport');

// Abrir puerto COM6 a 9600 baud
const puerto = new SerialPort({ path: 'COM6', baudRate: 9600 }, (err) => {
  if (err) {
    return console.error('Error al abrir el puerto:', err.message);
  }
  console.log('Puerto COM6 abierto y listo para leer.');
});

// Evento al recibir datos
puerto.on('data', (data) => {
  const texto = data.toString();  // convertir buffer a cadena
  console.log('Dato recibido:', texto);
});
