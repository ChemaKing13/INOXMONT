# InoxMont · Paquete de diseño (versión aprobada, 3 de octubre de 2026)

Este documento refleja el sitio tal como quedó aprobado. Todo el texto se publica tal cual. Es la base para la siguiente ronda de cambios.

## 0. Estado del proyecto

- **Sitio aprobado por el cliente**, listo para modificaciones posteriores. Aún no está en línea (falta la Fase 10: hosting y dominio).
- **Carpeta que se publica:** `inoxmont/sitio/` (solo `index.html` y `assets/`).
- **Carpeta de trabajo, no se publica:** `inoxmont/review/` (imágenes originales, video original, cuadros de revisión y pruebas).
- **Vista previa local:** servidor en `http://localhost:8850` (configuración "inoxmont" en `Desktop/.claude/launch.json`).
- **Créditos de Higgsfield:** 26 usados de 210; quedan 184 (plan Starter).

### Pendiente de confirmar con el cliente
1. Lista de metales que compran: fierro, acero, acero inoxidable, aluminio, cobre y bronce.
2. Texto del permiso: "Unidades con permiso de Servicio Público Federal para transportar carga."
3. Lista de a quién le compran: talleres, fábricas, constructoras, demoliciones, herrerías, tornerías y particulares.
4. Reseñas reales para agregar (no se inventaron testimonios).

### Datos confirmados por el cliente
- Pago al momento (efectivo o transferencia).
- Recolección sin costo cuando InoxMont compra el material.
- Zona: CDMX y Estado de México.
- WhatsApp y teléfono: 55 2731 6168. Correo: jcmontielinox@gmail.com.
- No pesan frente al cliente ni dan factura (no se menciona en el sitio).
- Las imágenes son generadas con IA y el sitio sale sin aviso.

## 1. Premisa de marca

**"Maniobra."** Toda la página enseña una sola idea: tú no cargas nada. InoxMont llega con grúa y tráiler, carga tu chatarra, se la lleva, te paga al momento y el metal vuelve a fundirse. El video es una maniobra (la última paca baja de la grúa y completa la carga del tráiler), las etiquetas de cada sección cuelgan de un cable con gancho, y el momento interactivo deja que el visitante haga la maniobra.

## 2. Activos de marca

- **Logo:** `assets/inoxmont-emblema.png`, recortado del PDF "LOGO OPCION 2" sin la línea del lema (decía "TRANSPORAMOS"). Se muestra sobre una placa clara #f6f4ee.
- **Lema correcto en el sitio:** "Transportamos, Maniobramos, Reciclamos".
- **Camión:** International 9400i Eagle blanco, versión moderna: cabina aerodinámica de techo alto, cubre tanques blancos, sin escapes cromados, sin visera. Sin emblema de International en la parrilla ni placas (se borran en cada imagen generada por ser marca registrada).
- **Tráiler:** plataforma naranja cargada de pacas de acero inoxidable con cinchos amarillos. Grúa telescópica amarilla.

## 3. Paleta

Sacada del logo (amarillo #f5bc41, verde #6aa237, gris acero #adbdc0, naranja #cf662a) y del atardecer del video.

```css
:root{
  --canvas:#101519; --canvas-2:#141b20; --panel:#19222a; --panel-2:#212c35;
  --line:rgba(173,189,192,.14); --line-strong:#66767f;
  --accent:#f5bc41; --accent-hover:#ffcb5c; --accent-muted:rgba(245,188,65,.18); --accent-ink:#1a1405;
  --green:#6aa237; --steel:#adbdc0; --orange:#cf662a;
  --text-secondary:#a3afb6; --text-primary:#eceee9; --text-over:#dde2e5;
}
```

Desviación dicha en voz alta: fondo oscuro con acento amarillo es un "look de IA" a evitar por defecto. Se usa porque es el mundo real de la marca (amarillo del logo y de la grúa) y la referencia que dio el cliente. Para no verse a plantilla: grafito azul acero, sin tipografía con serifas, y el cable de izaje como elemento firma.

## 4. Tipografías

- **Display:** Big Shoulders Display 800 y 900.
- **Texto:** Barlow 400, 500 y 600.
- **Mono:** IBM Plex Mono 500.

## 5. Video principal

- **Imagen inicial:** Nano Banana Pro, 2K, 16:9 (2 créditos por versión; se hicieron 4 versiones hasta llegar al camión aprobado).
- **Video:** Minimax Hailuo 2.3, 1080p, 6 segundos, sin audio (10 créditos). Seedance 2.5 y Kling 3.0 Pro requieren plan Plus.
- **Movimiento:** la grúa baja la última paca sobre la carga del tráiler mientras la cámara baja y se acerca. La paca toca la carga en el segundo 3.2 (progreso 0.55). La cámara sigue acercándose hasta el último cuadro.
- **Codificación web:** 1920x1072, crf 20, keyframe cada 8 cuadros, 5.3 MB (`assets/hero-scrub.mp4`). Póster, cuadro final y recorte 4:3 para celulares en `assets/`.

## 6. Mapa de bandas del video (hero de 580vh, rango de scroll 480vh)

Todos los textos viven abajo a la izquierda, sobre el suelo oscuro. La acción (paca y camión) queda arriba al centro y a la derecha.

| Banda | Rango | Momento del video | Texto (tal cual) | Entrada | Sombra |
|---|---|---|---|---|---|
| 1 | 0.00 a 0.20 | La paca cuelga alta | Etiqueta: "Compra de chatarra y metales · CDMX y Edomex" / Título (h1): "Lo pesado es nuestro oficio." / Sub: "Compramos tu chatarra, la cargamos con grúa y nos la llevamos." | Colgar (palabras bajan colgadas y se asientan con vaivén). Rampa de carga al abrir. | .64 |
| 2 | 0.24 a 0.47 | La paca desciende | "Nosotros lo cargamos." / "Llegamos con grúa y operadores con experiencia. Subimos piezas grandes al tráiler sin que muevas un dedo." | Caída suave | .60 |
| 3 | 0.51 a 0.73 | La paca toca la carga | "Pago al momento." (la palabra "momento." en amarillo) / "En efectivo o transferencia, el mismo día que cargamos tu material." | Golpe con rebote | .56 |
| 4 | 0.77 a 1.00 | Reposo, camión cerca | Etiqueta: "InoxMont" / "Transportamos. Maniobramos. Reciclamos." (una palabra por línea) / "Recolección sin costo en CDMX y Estado de México." / Botones: "Cotiza por WhatsApp" y "Llamar 55 2731 6168" | Subida palabra por palabra con cierre escalonado | .64 |

Lectura tipo grúa (arriba a la izquierda): "Carga 6.0 m" bajando a "0.0 m", estado Izada / Bajando / Asentada.

**Resultados de las pruebas:** cada banda se lee durante 6 movimientos normales de scroll y ninguna se salta con scroll rápido. Contraste del peor pixel bajo el texto: 6:1 o mejor en todas las bandas (mínimo exigido 3.5:1).

## 7. Hero fijo (celulares, tablets verticales, celular horizontal y movimiento reducido)

Imagen: recorte 4:3 del cuadro final (`assets/hero-static.jpg`). En celular horizontal, imagen a la izquierda y texto a la derecha.
- Etiqueta: "Compra de chatarra y metales · CDMX y Edomex"
- Título: "Lo pesado es nuestro oficio."
- Sub: "Compramos tu chatarra, la recogemos sin costo y te pagamos al momento."
- Botones: "Cotiza por WhatsApp" / "Llamar"

## 8. Secciones debajo del video

**01 · Lo que hacemos** (`#servicios`): "Si es metal y pesa, nosotros lo movemos." / "Cuatro servicios, un solo equipo. Desde unas piezas sueltas hasta lotes completos."
1. Compra de chatarra y metales. "Compramos fierro, acero, acero inoxidable, aluminio, cobre y bronce. El precio depende del metal y del precio del día."
2. Recolección y transporte. "Vamos por tu material con nuestros camiones y tráileres. Si te lo compramos, la recolección no tiene costo."
3. Maniobras, carga y descarga. "Llegamos con grúa y operadores para subir, bajar y acomodar cargas pesadas con cuidado."
4. Procesamiento y reciclaje. "Separamos, cortamos y preparamos el metal para que vuelva a fundirse y sea material nuevo."

**02 · Cómo funciona** (`#como-funciona`): "Tres pasos. Lo pesado va por nuestra cuenta."
1. Mándanos fotos. "Por WhatsApp, con el tipo de material y cuánto hay más o menos."
2. Te cotizamos y agendamos. "Te damos precio y quedamos en el día y la hora de la recolección."
3. Cargamos y te pagamos. "Llegamos con el equipo, cargamos todo y te pagamos al momento."
- Momento interactivo "Haz la maniobra": botón "Mantén presionado para cargar". La grúa iza la paca y la pone en el hueco del tráiler. Si se suelta antes, regresa suave. Al terminar: botón "Carga lista", ayuda "Carga asentada en el tráiler.", los tres pasos se encienden y aparece "Así de fácil. Tú nos mandas fotos, nosotros hacemos lo pesado." con el botón "Cotiza tu material".

**03 · Por qué InoxMont** (`#confianza`): "Llegamos, cargamos y pagamos. Sin vueltas."
- Pago al momento. "Efectivo o transferencia, el mismo día."
- Recolección sin costo. "Si te compramos el material, el flete corre por nuestra cuenta."
- Servicio Público Federal. "Unidades con permiso de Servicio Público Federal para transportar carga."
- Equipo para lo pesado. "Grúa, tráileres y operadores con experiencia en maniobras."
- Cinta: "Compramos a" talleres, fábricas, constructoras, demoliciones, herrerías, tornerías, particulares.

**04 · Cotiza** (`#cotiza`): "Cotiza tu material hoy." / "Llena estos datos y se abre WhatsApp con tu mensaje listo. Agrega tus fotos y envíalo."
- Campos: Tu nombre · ¿Dónde está? · ¿Qué material tienes? · Cantidad aproximada · ¿Necesitas grúa para cargar?
- Botón: "Enviar por WhatsApp". Nota: "Tu mensaje llega a InoxMont cuando lo envías desde tu WhatsApp."
- Éxito: "Listo." / "Se abrió WhatsApp con tu mensaje. Si no se abrió, escríbenos al 55 2731 6168."
- Mensaje que arma: saludo, nombre, material, cantidad, ubicación, si necesita grúa y "Les mando fotos a continuación."

**Pie:** emblema, "Transportamos, Maniobramos, Reciclamos", teléfono, correo, Servicio Público Federal, "© 2026 InoxMont. Compra, recolección y reciclaje de metales."

**En celulares:** barra fija abajo con "Cotiza por WhatsApp" y "Llamar".

**Cambios posteriores a la aprobación (3 de octubre de 2026):** se eliminó la sección de preguntas y respuestas (con su enlace del menú y su estilo) y Cotiza pasó a ser la sección 04. La etiqueta "Compramos a" ahora cubre toda la altura de la cinta.

## 9. Imágenes de apoyo (Nano Banana Pro, 2K, 4:3, 8 créditos)

`servicio-compra.jpg`, `servicio-recoleccion.jpg` (se borró el emblema de International de la parrilla), `servicio-maniobras.jpg` (se borraron placa y etiquetas de la grúa), `servicio-reciclaje.jpg`. Originales en `review/stills/`.

## 10. Ingeniería (cumplida y probada)

Video cargado como Blob con anillo de progreso y vigilante de 20 s; lerp normalizado por dt; seeks con compuerta; escrituras al DOM solo con cambio; sombras por banda con aislamiento de capa (la sombra va delante del video); las cinco compuertas del hero fijo vivas; página completa sin video (cruza del póster al cuadro final); movimiento reducido en vivo en ambos sentidos; pausa en pestañas ocultas; sin desplazamiento lateral; consola sin errores en escritorio, tablet y celular.

## 11. Para cuando se publique (Fase 10)

- Cambiar `og:url` y `og:image` en la marca `<!-- DEPLOY STEP -->` de `index.html` con la dirección real.
- Comprimir el contenido de `sitio/` (no la carpeta) y subirlo con el conector de Hostinger.

## 12. Compuerta de texto

Cero guiones largos, cero palabras de relleno. El triplete "Transportamos. Maniobramos. Reciclamos." es el lema real y se queda.
