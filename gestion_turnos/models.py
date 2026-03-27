from django.db import models

from django.db import models

# 1. HOSPITAL: La base del sistema
class Hospital(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# 2. ROL: Define los tipos de acceso
class Rol(models.Model):
    nombre = models.CharField(max_length=50) # Admin, Recepcionista, Médico
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# 3. USUARIO: Personal del sistema
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

# 4. MEDICO: Profesionales de la salud
class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.apellido}"

# 5. OBRA SOCIAL
class ObraSocial(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# 6. PACIENTE
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

# 7. TURNO: Gestión de citas
class Turno(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

# 8. DISPONIBILIDAD MEDICA
class DisponibilidadMedico(models.Model):
    dia_semana = models.IntegerField() # 0-6 para los días de la semana
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
