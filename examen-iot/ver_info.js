const fs = require("fs");

const archivo = "info.db";
const salidaHTML = "tabla_info.html";

function generarTablaHTML(datos) {
  const encabezados = [
    "Timestamp",
    "Sónico",
    "Luz",
    "Temperatura",
    "Humedad",
    "Lámpara",
    "PC1","PC2","PC3","PC4","PC5","PC6","PC7","PC8","PC9","PC10",
    "Buzzer",
    "RFID"
  ];

  const filas = datos
    .map((linea) => {
      const celdas = linea.split(",").map((val) => `<td>${val}</td>`);
      return `<tr>${celdas.join("")}</tr>`;
    })
    .join("\n");

  return `
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <title>Registros del PLC</title>
      <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
      </style>
    </head>
    <body>
      <h1>Registros del PLC</h1>
      <table>
        <thead>
          <tr>${encabezados.map((h) => `<th>${h}</th>`).join("")}</tr>
        </thead>
        <tbody>
          ${filas}
        </tbody>
      </table>
    </body>
    </html>
  `;
}

if (fs.existsSync(archivo)) {
  const contenido = fs.readFileSync(archivo, "utf8").trim().split("\n");
  const html = generarTablaHTML(contenido);
  fs.writeFileSync(salidaHTML, html);
  console.log(`✅ Tabla HTML generada: ${salidaHTML}`);
} else {
  console.log("❌ No se encontró el archivo info.db");
}

