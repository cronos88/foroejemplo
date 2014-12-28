from django.db import models
from django.contrib.auth.models import User


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class Preguntas(models.Model):  #Questions
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categorias)
    fecha_pub = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)  #user
    votos = models.IntegerField(default=0) #vote

    def __unicode__(self):
        return self.titulo


class Respuestas(models.Model):
    descripcion = models.TextField()
    pregunta = models.ForeignKey(Preguntas)
    usuario = models.ForeignKey(User)
    fecha_resp = models.DateTimeField(auto_now=True)
    votos = models.IntegerField(default=0)

    def __unicode__(self):
        return self.descripcion

class Votante_preg(models.Model):  #voters
    usuario = models.CharField(max_length=50)
    pregunta = models.IntegerField()

class Votante_resp(models.Model):
    usuario = models.IntegerField()
    respuesta = models.IntegerField()


