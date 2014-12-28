
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.shortcuts import RequestContext
from .models import Preguntas, Respuestas, Categorias, Votante_preg, Votante_resp
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    pregunta = Preguntas.objects.all().order_by('-votos')[:20]
    return render_to_response('mundodjango/index.html', locals(), context_instance = RequestContext(request))

def pregunta_detalle(request, pregunta_id):
    p = get_object_or_404(Preguntas, pk=pregunta_id)
    respuestas = Respuestas.objects.filter(pregunta= pregunta_id)
    return render_to_response('mundodjango/pregunta_detalle.html', locals(), context_instance = RequestContext(request))

@login_required(login_url='/account/login/')
def plus_preg(request, pregunta_id):

    pregunta = Preguntas.objects.get(pk = pregunta_id)
    voter = Votante_preg.objects.filter(usuario=request.user.id, pregunta= pregunta_id)

    if voter.exists():
        pregunta.votos = pregunta.votos - 1
        Votante_preg.objects.get(pregunta=pregunta_id, usuario=request.user.id).delete()
    else:
        pregunta.votos = pregunta.votos +1
        Votante_preg(pregunta=pregunta_id, usuario=request.user.id).save()

    pregunta.save()
    return redirect("/preguntas/%s/" % (pregunta_id))

@login_required(login_url='/account/login/')
def plus_resp(request, respuesta_id):
    respuesta = Respuestas.objects.get(pk = respuesta_id)
    voter_resp = Votante_resp.objects.filter(usuario=request.user.id, respuesta= respuesta_id)
    if voter_resp.exists():
        respuesta.votos = respuesta.votos - 1
        Votante_resp.objects.get(usuario=request.user.id, respuesta=respuesta_id).delete()
    else:
        respuesta.votos = respuesta.votos + 1
        Votante_resp(usuario=request.user.id, respuesta=respuesta_id).save()
    respuesta.save()
    return redirect("/preguntas/%s/" % (respuesta.pregunta_id))


def logout(request):
    return redirect("/")



