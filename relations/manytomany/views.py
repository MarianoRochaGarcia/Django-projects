from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create(request):

    # art1 = Article(headline='Articulo primero')
    # art1.save()

    # art2 = Article(headline='Articulo segundo')
    # art2.save()

    # art3 = Article(headline='Articulo tercero')
    # art3.save()
    
    # pub1 = Publication(tittle='Publicacion primera')
    # pub1.save()

    # pub2 = Publication(tittle='Publicacion segunda')
    # pub2.save()
   
    # pub3 = Publication(tittle='Publicacion tercera')
    # pub3.save()

    # pub4 = Publication(tittle='Publicacion cuarta')
    # pub4.save()

    # pub5 = Publication(tittle='Publicacion quinta')
    # pub5.save()

    # pub6 = Publication(tittle='Publicacion sexta')
    # pub6.save()

    # pub7 = Publication(tittle='Publicacion septima')
    # pub7.save()

    # art1.publications.add(pub1)
    # art1.publications.add(pub2)
    # art1.publications.add(pub3)
    # art2.publications.add(pub4)
    # art2.publications.add(pub5)
    # art3.publications.add(pub6)
    # art3.publications.add(pub7)

    # pub1 = Publication.objects.get(id=1)
    
    pub1 = Publication.objects.get(id=1)

    # art1.publications.remove(pub1)

    result = pub1.article_set.all()

    return HttpResponse(result)