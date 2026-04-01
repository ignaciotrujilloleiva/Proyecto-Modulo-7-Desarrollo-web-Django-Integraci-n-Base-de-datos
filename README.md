# 💳 Alke Wallet

<p align="center">
  <img src="https://img.shields.io/badge/Django-Web%20Framework-0C4B33?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Estado-Finalizado-success?style=for-the-badge" alt="Estado">
  <img src="https://img.shields.io/badge/Bootcamp-M%C3%B3dulo%207-orange?style=for-the-badge" alt="Bootcamp">
</p>

<p align="center">
  Aplicación web desarrollada con <strong>Django</strong> como parte del Módulo 7 del bootcamp, enfocada en la <strong>integración con bases de datos</strong> utilizando el ORM de Django y operaciones CRUD completas.
</p>

---

## 🚀 Descripción del proyecto

**Alke Wallet** es una aplicación web que permite:

* Gestionar usuarios del sistema
* Registrar transacciones financieras
* Asociar transacciones a monedas
* Administrar datos desde el panel administrativo de Django
* Visualizar y manipular información persistente mediante el ORM

Este proyecto se centra en la integración entre **modelos, base de datos, vistas y templates**.

---

## 🧠 Tecnologías utilizadas

* Python 3
* Django
* HTML5
* CSS3
* Bootstrap
* SQLite3
* Visual Studio Code

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone 

https://github.com/ignaciotrujilloleiva/Proyecto-Modulo-7-Desarrollo-web-Django-Integraci-n-Base-de-datos.git
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

---

### 3. Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

---

### 4. Instalar dependencias

```bash
pip install django
```

---

### 5. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

---

### 7. Ejecutar servidor

```bash
python manage.py runserver
```

---

### 8. Acceder al sistema

* 🌐 Aplicación: http://127.0.0.1:8000/
* ⚙️ Admin: http://127.0.0.1:8000/admin/

---

## 📌 Funcionalidades principales

* 🏠 Página de inicio
* 👤 CRUD de usuarios
* 💸 CRUD de transacciones
* 💱 Gestión de monedas
* 🔗 Relaciones entre modelos (ORM)
* ⚙️ Panel administrativo Django
* 🎨 Interfaz con estilos personalizados y Bootstrap

---

## 🗃️ Modelos del sistema

```python
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Moneda(models.Model):
    nombre = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} ({self.simbolo})"


class Transaccion(models.Model):
    TIPO_TRANSACCION = [
        ('deposito', 'Depósito'),
        ('retiro', 'Retiro'),
        ('transferencia', 'Transferencia'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transacciones')
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='transacciones')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_transaccion = models.CharField(max_length=20, choices=TIPO_TRANSACCION)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.tipo_transaccion} - {self.monto}"
```
Estos modelos implementan relaciones uno a muchos (1:N) mediante claves foráneas, 
permitiendo que un usuario tenga múltiples transacciones y que cada transacción 
esté asociada a una moneda específica.

Además, se incorporan buenas prácticas como:

- uso de `choices` para restringir valores
- métodos `__str__` para mejorar la legibilidad
- `related_name` para facilitar consultas inversas en el ORM

---

## 🔗 Relaciones entre modelos

* Un **usuario** puede tener múltiples **transacciones**
* Una **moneda** puede estar asociada a múltiples **transacciones**

Esto corresponde a relaciones **uno a muchos (1:N)** implementadas mediante `ForeignKey`.

---

## 🏗️ Arquitectura del proyecto

El proyecto sigue el patrón MVT (Modelo - Vista - Template) de Django:

```
Modelo → Vista → Template → Usuario
```

Permite separar:

* la lógica de datos (ORM)
* la lógica de negocio (views)
* la presentación (templates)

---

## 🧩 Estructura del proyecto

```
/Proyecto-Modulo-7-Desarrollo-web-Django
│
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── Entregable/
│   └── Informe-proyecto-Alke-Web-Base.pdf
│
├── alke_wallet/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── wallet/
    ├── migrations/
    ├── static/
    │   └── wallet/
    │       ├── css/
    │       │   └── style.css
    │       └── img/
    │           └── fondo.jpg
    ├── templates/
    │   └── wallet/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── usuario_list.html
    │       ├── usuario_form.html
    │       ├── usuario_confirm_delete.html
    │       ├── transaccion_list.html
    │       ├── transaccion_form.html
    │       └── transaccion_confirm_delete.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

---

## 🔍 Explicación de componentes importantes

`models.py`
Define las entidades del sistema y sus relaciones mediante el ORM.

`views.py`
Contiene la lógica para listar, crear, actualizar y eliminar registros.

`urls.py`
Define las rutas de navegación del sistema.

`admin.py`
Permite gestionar datos desde el panel administrativo de Django.

`templates/`
Contiene las vistas HTML reutilizables del sistema.

`static/`
Incluye estilos CSS e imágenes utilizadas en la interfaz.

`migrations/`
Gestiona los cambios en la base de datos.

---

## 🧪 Pruebas realizadas

Durante el desarrollo se verificó:

* creación de usuarios y transacciones
* relaciones correctas entre modelos
* funcionamiento de migraciones
* operaciones CRUD completas
* visualización correcta en templates
* gestión desde el panel admin

---

## 📷 Evidencias

Se incluyen capturas de:

* Estructura del proyecto
* Base de datos (SQLite)
* CRUD de usuarios
* CRUD de transacciones
* Panel administrativo
* Interfaz web funcionando

---

## 📌 Conclusión

Este proyecto permitió aplicar el uso del ORM de Django para la gestión de datos persistentes, integrando modelos, relaciones, migraciones y operaciones CRUD en una aplicación web funcional, consolidando el flujo completo entre backend y frontend.

---

## ✍️ Autor

Ignacio Trujillo Leiva
Bootcamp Fullstack Python
2026
