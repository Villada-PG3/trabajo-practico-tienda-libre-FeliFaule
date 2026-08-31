from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    productos_destacados = [
        {
            "nombre": "Termo Stanley 1 Litro",
            "precio": 45000,
            "descripcion": "Termo de acero inoxidable ideal para mantener tus bebidas calientes.",
            "destacado": True,
        },
        {
            "nombre": "Mate de Acero Inoxidable",
            "precio": 18000,
            "descripcion": "Mate resistente de acero inoxidable para usar todos los días.",
            "destacado": True,
        },
        {
            "nombre": "Vaso Térmico 500 ml",
            "precio": 22000,
            "descripcion": "Vaso térmico con tapa para llevar tus bebidas a cualquier lugar.",
            "destacado": True,
        },
        {
            "nombre": "Bombilla de Acero",
            "precio": 8500,
            "descripcion": "Bombilla de acero inoxidable resistente y fácil de limpiar.",
            "destacado": False,
        },
        {
            "nombre": "Botella Térmica 750 ml",
            "precio": 25000,
            "descripcion": "Botella térmica de 750 ml para conservar la temperatura.",
            "destacado": True,
        },
        {
            "nombre": "Mate de Calabaza Premium",
            "precio": None,
            "descripcion": "Mate de calabaza de excelente calidad con terminaciones premium.",
            "destacado": False,
        },
    ]

    contexto = {
        "titulo": "Tienda Libre",
        "mensaje": "Bienvenido a nuestra tienda online",
        "productos_destacados": productos_destacados,
    }

    return render(request, "tiendalibre/home.html", contexto)



def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca_de_mi.html")
