from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm
def form(request):
    comment_form = CommentForm({'name': 'Juanjo', 'url': 'http://openbootcamp.com', 'comment': 'comentario'})
    return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
    if request.method != "POST":
        return HttpResponse("Metodo no permitido")
    
    return HttpResponse(request.POST['name'])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #Todas las acciones a realizar cuando los datos son correctos
            return HttpResponse('Valido')
        else:
            #Comunicamos al usuario que los datos no son validos
            return render(request, 'widget.html', {'form': form})
