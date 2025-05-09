# Clean-PC 🧹💻

**Clean-PC** es una herramienta de limpieza para Windows que elimina archivos temporales del sistema, incluyendo las carpetas `Temp`, `%temp%` y `Prefetch`.  
Ideal para mantener tu computadora limpia, liberar espacio en disco y mejorar el rendimiento general.

---

## 🧩 ¿Qué hace?

El script analiza y limpia tres ubicaciones comunes donde se acumulan archivos temporales:

- 🗂️ Carpeta `Temp` del sistema.
- 🧾 Carpeta `%temp%` del usuario.
- ⚙️ Carpeta `C:\Windows\Prefetch`.

Todos los archivos y carpetas dentro de estas ubicaciones son eliminados de forma segura.

---

## ⚠️ Requiere permisos de administrador

La aplicación solicita automáticamente permisos de administrador al ejecutarse, ya que son necesarios para acceder a ciertas carpetas del sistema.

---

## 📄 Archivos incluidos

- `CleanPc.py` → Código fuente de la aplicación.
- `CleanPcError.txt` → Archivo de registro donde se anotan errores si no se puede eliminar algún archivo.

---

## 💡 Michel.sr145

Esta aplicación fue creada con la intención de brindar una herramienta rápida y efectiva para eliminar archivos temporales en Windows sin necesidad de usar aplicaciones externas pesadas o llenas de publicidad.

Ideal para usar antes de apagar la PC o cuando se nota una ralentización general del sistema.

---
