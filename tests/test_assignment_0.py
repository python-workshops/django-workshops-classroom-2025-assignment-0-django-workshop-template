"""
Assignment 0: URL Mapping Tests

Te testy sprawdzają czy student poprawnie zmapował URL-e na widoki
i czy rozumie różnicę między HttpResponse a render().
"""

import pytest
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.conf import settings
from workshop_project import views


class Assignment0URLMappingTestCase(TestCase):
    """Testy sprawdzające poprawność mapowania URL-i"""
    
    def setUp(self):
        self.client = Client()
    
    def test_home_page_accessible(self):
        """Test 1: Sprawdza czy strona główna (/) jest dostępna"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django Workshop')
    
    def test_home_page_uses_httpresponse(self):
        """Test 2: Sprawdza czy strona główna używa HttpResponse (string w response)"""
        response = self.client.get('/')
        self.assertContains(response, 'HttpResponse')
        self.assertContains(response, 'zwraca HTML jako string')
    
    def test_info_page_accessible(self):
        """Test 3: Sprawdza czy strona /info/ jest dostępna"""
        response = self.client.get('/info/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Strona Informacyjna')
    
    def test_info_page_uses_template(self):
        """Test 4: Sprawdza czy strona /info/ używa template"""
        response = self.client.get('/info/')
        self.assertContains(response, 'render()')
        self.assertContains(response, 'przetwarza plik template')
    
    def test_home_url_resolves_to_home_view(self):
        """Test 5: Sprawdza czy URL '' mapuje na views.home"""
        resolver = resolve('/')
        self.assertEqual(resolver.func, views.home)
    
    def test_info_url_resolves_to_info_view(self):
        """Test 6: Sprawdza czy URL 'info/' mapuje na views.info"""
        resolver = resolve('/info/')
        self.assertEqual(resolver.func, views.info)
    
    def test_health_check_still_works(self):
        """Test 7: Sprawdza czy health check endpoint nadal działa"""
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'OK')
    
    def test_admin_still_accessible(self):
        """Test 8: Sprawdza czy panel admin jest nadal dostępny"""
        response = self.client.get('/admin/')
        # Powinien przekierować do logowania (302) lub pokazać stronę logowania (200)
        self.assertIn(response.status_code, [200, 302])
    
    def test_views_import_works(self):
        """Test 9: Sprawdza czy import views działa poprawnie"""
        # Sprawdza czy można zaimportować views
        from workshop_project import views
        self.assertTrue(hasattr(views, 'home'))
        self.assertTrue(hasattr(views, 'info'))
        self.assertTrue(hasattr(views, 'health_check'))
    
    def test_home_and_info_are_different_responses(self):
        """Test 10: Sprawdza czy home i info zwracają różne treści"""
        home_response = self.client.get('/')
        info_response = self.client.get('/info/')
        
        # Oba powinny zawierać różne charakterystyczne teksty
        self.assertContains(home_response, 'HttpResponse')
        self.assertContains(info_response, 'render()')
        
        # Nie powinny zawierać tych samych unikalnych słów
        self.assertNotContains(home_response, 'render()')
        self.assertNotContains(info_response, 'HttpResponse')


@pytest.mark.django_db
class Assignment0IntegrationTests:
    """Dodatkowe testy integracyjne sprawdzające pełny workflow"""
    
    def test_navigation_between_pages(self):
        """Test 11: Sprawdza nawigację między stronami"""
        client = Client()
        
        # Start na stronie głównej
        home_response = client.get('/')
        assert home_response.status_code == 200
        
        # Sprawdź link do strony info
        assert '/info/' in home_response.content.decode()
        
        # Przejdź na stronę info
        info_response = client.get('/info/')
        assert info_response.status_code == 200
        
        # Sprawdź link powrotny
        assert '/' in info_response.content.decode()
    
    def test_template_and_static_configuration(self):
        """Test 12: Sprawdza konfigurację templates i static files"""
        assert hasattr(settings, 'TEMPLATES')
        template_dirs = settings.TEMPLATES[0]['DIRS']
        assert len(template_dirs) > 0
        
        assert hasattr(settings, 'STATIC_URL')
        assert settings.STATIC_URL == '/static/'
    
    def test_assignment_completion_indicators(self):
        """Test 13: Sprawdza czy zadanie zostało faktycznie wykonane"""
        # Test czy URLs są poprawnie skonfigurowane
        client = Client()
        
        # Wszystkie endpoint-y powinny zwracać 200
        endpoints = ['/', '/info/', '/health/']
        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200, f"Endpoint {endpoint} should return 200, got {response.status_code}"
        
        # Strony powinny zawierać oczekiwaną treść
        home = client.get('/').content.decode()
        info = client.get('/info/').content.decode()
        
        assert 'Django Workshop' in home
        assert 'Strona Informacyjna' in info
        assert 'HttpResponse' in home
        assert 'render()' in info