from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home(request):
    """
    Widok strony głównej używający HttpResponse z HTML jako string
    Ten widok będzie zmapowany na URL '' (root) przez studenta
    """
    return HttpResponse(
        "<h1>🎉 Django Workshop</h1>"
        "<p>Witaj w Django Workshop! URL mapping działa poprawnie.</p>"
        "<p>Ta strona używa <strong>HttpResponse</strong> - Django zwraca HTML jako string.</p>"
        "<p><a href='/info/'>Przejdź do strony info (używa render)</a> | <a href='/health/'>Health check (JsonResponse)</a></p>"
    )


def info(request):
    """
    Widok strony informacyjnej używający render z template
    Ten widok będzie zmapowany na URL 'info/' przez studenta
    """
    return render(request, 'info.html')


def health_check(request):
    """
    Health check endpoint używający JsonResponse
    Ten widok będzie zmapowany na URL 'health/' przez studenta
    """
    return JsonResponse({'status': 'ok'})