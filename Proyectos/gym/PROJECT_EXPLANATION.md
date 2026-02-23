# Documentación del Proyecto: Gym Tracker App (PRIME)

## 📌 Visión General
**Gym Tracker App** es una aplicación web progresiva (PWA) diseñada para el seguimiento avanzado de entrenamientos en el gimnasio. Su principal enfoque es permitir que múltiples usuarios compartan un mismo dispositivo durante una sesión de entrenamiento, gestionando rutinas compartidas y personales, y ofreciendo una lógica de progresión inteligente.

El objetivo es ofrecer una experiencia **premium**, fluida y eficiente, eliminando la fricción de registrar pesos y repeticiones, y proporcionando estadísticas claras sobre el progreso.

---

## 🚀 Funcionalidades Principales

### 1. Gestión de Sesiones y Usuarios
- **Multiusuario en Dispositivo Único**: Diseñado para que compañeros de entrenamiento (gym bros) usen un solo móvil para registrar sus series alternadamente.
- **Perfiles de Usuario**: Soporte para roles de Usuario y Administrador.
- **Asistente IA**: Integración prevista con ChatGPT para análisis de estadísticas por usuario.

### 2. Rutinas y Ejercicios
- **Rutinas Compartidas**: Editables solo por su creador, pero utilizables por otros.
- **Rutinas Personales**: Totalmente gestionables por el usuario.
- **Estructura**: `Rutina` → `Días` → `Ejercicios`.
- **Base de Datos de Ejercicios**: Gestionada globalmente por administradores, con fotos y notas. Los usuarios pueden sugerir ejercicios mediante fotos (validación por IA/Admin).

### 3. Modos de la Aplicación
- **Modo Gym (Entrenamiento)**: Interfaz optimizada para el registro rápido de series, RIR (Repeticiones en Reserva) y tiempos de descanso.
- **Estadísticas**: Visualización del progreso (cargas, volumen) y peso corporal semanal.
- **Panel de Administración**: Para gestión de la base de datos de ejercicios y usuarios.

### 4. Lógica de Progresión (Overload)
El sistema sugiere automáticamente las cargas para la siguiente sesión basándose en el rendimiento:
- **Éxito (Reps objetivo cumplidas)**: Sugiere aumento de peso.
- **Fallo**: Sugiere mantener o reducir la carga (deload).
- **Primera Sesión**: Sin objetivos predefinidos, establece la línea base.

---

## 🛠 Arquitectura Técnica

### Stack Tecnológico
- **Frontend**: 
  - **Framework**: React 19 + Vite (Rendimiento máximo).
  - **Lenguaje**: TypeScript.
  - **Routing**: React Router 7.
  - **Estado Local / Caché**: Dexie.js (IndexedDB) para robustez y posible soporte offline.
  - **Iconos**: Lucide React.
  - **Gráficos**: Recharts.

- **Backend / Datos**:
  - **Supabase**: Base de datos PostgreSQL, Autenticación y Almacenamiento.
  - **Esquema Relacional**: Definido en `schema.sql` (tablas para usuarios, ejercicios, rutinas, logs de entrenamiento, historial de peso).

- **Estilos y Diseño**:
  - **Enfoque**: CSS Nativo con Variables CSS (Custom Properties).
  - **Utilidades**: `clsx` y `tailwind-merge` para gestión condicional de clases (aunque el núcleo de estilos es propio).
  - **No dependencia de frameworks UI pesados**: Para control total del diseño "Apple-like".

---

## 🎨 Sistema de Diseño: Dark Premium Apple Blue

La aplicación sigue una estética **"Dark Mode"** pulida y minimalista, inspirada en las interfaces de Apple Health y Fitness.

### Tokens de Diseño (`variables.css`)
- **Colores Principales**:
  - Fondo: `#0F1115` (Casi negro, muy elegante).
  - Superficies: `#161A22` (Tarjetas), `#1C2230` (Elementos interactivos).
  - Acento (Primary): `#3B82F6` (Azul Apple).
  - Éxito/Peligro: `#30D158` (Verde), `#FF453A` (Rojo).
  
- **Tipografía**:
  - Stack del sistema (`-apple-system`, `San Francisco`, `Inter`) para máxima legibilidad nativa.
  
- **Componentes**:
  - **Tarjetas**: Bordes redondeados (`14px` - `20px`), fondos oscuros sutiles.
  - **Botones**: Altura mínima de `44px` (touch-friendly), feedbacks visuales claros.

---

## 📂 Estructura del Proyecto

```
/
├── gym-tracker/            # Código Fuente de la Aplicación (Vitest/React)
│   ├── src/
│   │   ├── components/     # Componentes UI reutilizables
│   │   ├── pages/          # Vistas principales (Gym, Routines, Stats)
│   │   ├── styles/         # Definiciones CSS globales y variables
│   │   │   ├── variables.css # Tokens del sistema de diseño
│   │   │   └── global.css    # Reset y estilos base
│   │   ├── contexts/       # Gestión de estado global (React Context)
│   │   ├── services/       # Comunicación con Supabase
│   │   └── types/          # Definiciones TypeScript (DB types)
│   ├── public/             # Assets estáticos
│   └── index.html          # Punto de entrada
│
├── functional_spec.md      # Especificación funcional detallada
├── design_system.md        # Guía de estilos y UX
├── schema.sql              # Definición de la base de datos SQL
├── exercises_seed.csv      # Datos semilla de ejercicios
├── routines_seed.json      # Datos semilla de rutinas iniciales
└── README.md               # Instrucciones rápidas de inicio
```

---

## 🔄 Flujo de Trabajo Recomendado (Desarrollo)

1. **Base de Datos**: Configurar proyecto en Supabase y ejecutar el script `schema.sql`.
2. **Datos Iniciales**: Importar el CSV de ejercicios y el JSON de rutinas.
3. **Entorno Local**: 
   - `cd gym-tracker`
   - `npm install`
   - `npm run dev`
4. **Iteración**:
   - Consultar `functional_spec.md` para lógica de negocio.
   - Usar tokens de `variables.css` para cualquier nuevo componente UI.

---

## 📝 Notas Adicionales
- **No Hardcoding**: Se prohíbe el uso de valores hexadecimales de color directamente en los componentes; siempre usar variables CSS (`var(--primary)`, etc.).
- **Escalabilidad**: El proyecto está preparado para PWA (Progressive Web App) y escalado futuro de usuarios.
