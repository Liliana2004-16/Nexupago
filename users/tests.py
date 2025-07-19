from django.test import TestCase, Client
from django.urls import reverse
from users.models import Usuario

class UsuariosViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = Usuario.objects.create_user(
            email='admin@correo.com',
            password='adminpass', # NOSONAR
            rol='ADMIN'
        )

    def test_login_usuario_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_usuario_post_exitoso(self):
        self.client.login(email='admin@correo.com', password='adminpass')# NOSONAR
            rol='ADMIN'
        response = self.client.post(reverse('login'), {
            'email': 'admin@correo.com',
            'password': 'adminpass'# NOSONAR
            rol='ADMIN'
        })
        self.assertEqual(response.status_code, 302)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_gestion_usuarios_acceso_denegado(self):
        response = self.client.get(reverse('gestion_usuarios'))
        self.assertEqual(response.status_code, 302)  # redirige al login
