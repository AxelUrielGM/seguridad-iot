const { SerialPort } = require("serialport");
const fs = require("fs");

const puerto = new SerialPort({
  path: "COM6",
  baudRate: 9600,
});

class PLC {
  constructor() {
    this.sonico = "";
    this.luz = "";
    this.temperatura = "";
    this.humedad = "";
    this.lampara = "";
    this.computadoras = Array(10).fill("0");
    this.buzzer = "";
    this.rfid = "";
  }

  actualizarDesdeCadena(cadena) {
    const partes = cadena.trim().split(",");
    if (partes.length !== 17) return; // ✅ CORREGIDO

    this.sonico = partes[0];
    this.luz = partes[1];
    this.temperatura = partes[2];
    this.humedad = partes[3];
    this.lampara = partes[4];
    this.computadoras = partes.slice(5, 15);
    this.buzzer = partes[15];
    this.rfid = partes[16];
  }

  generarLineaConTimestamp() {
    const timestamp = Math.floor(Date.now() / 1000);
    return `${timestamp},${this.sonico},${this.luz},${this.temperatura},${this.humedad},${this.lampara},${this.computadoras.join(",")},${this.buzzer},${this.rfid}\n`;
  }
}

const plc = new PLC();

puerto.on("data", (data) => {
  const texto = data.toString().trim();
  plc.actualizarDesdeCadena(texto);

  console.clear();
  console.log("📡 Datos recibidos del emulador:");
  console.table([{
    sonico: plc.sonico,
    luz: plc.luz,
    temperatura: plc.temperatura,
    humedad: plc.humedad,
    lampara: plc.lampara,
    buzzer: plc.buzzer,
    rfid: plc.rfid,
    computadoras: plc.computadoras.join(" ")
  }]);

  const linea = plc.generarLineaConTimestamp();
  fs.appendFile("info.db", linea, (err) => {
    if (err) console.error("[X] Error al guardar:", err);
    else console.log("[💾] Registro guardado en info.db");
  });
});
