from django.test import TestCase, Client
from django.urls import reverse
from users.models import Usuario
from service.models import Servicio, Pago
from datetime import date

class ServiceViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin_user = Usuario.objects.create_user(
            email='admin@correo.com',
            password='adminpass',  # NOSONAR
            rol='ADMIN'
        )
        self.empleado_user = Usuario.objects.create_user(
            email='empleado@correo.com',
            password='empleadopass',  # NOSONAR
            rol='EMPLEADO'
        )

        self.servicio = Servicio.objects.create(
            nombre='Servicio de prueba',
            descripcion='Prueba de servicio',
            valor=50000,
            estado='Pendiente de Pago'
        )

        self.pago = Pago.objects.create(
            servicio=self.servicio,
            usuario=self.empleado_user,
            valor=50000,
            mes='Enero',
            fecha_pago=date.today()
        )

    def test_admin_home_view(self):
        self.client.login(email='admin@correo.com', password='adminpass')  # NOSONAR
        response = self.client.get(reverse('admin_home'))
        self.assertEqual(response.status_code, 200)

    def test_empleado_home_view(self):
        self.client.login(email='empleado@correo.com', password='empleadopass')  # NOSONAR
        response = self.client.get(reverse('empleado_home'))
        self.assertEqual(response.status_code, 200)

    def test_crear_servicio_get(self):
        self.client.login(email='empleado@correo.com', password='empleadopass')  # NOSONAR
        response = self.client.get(reverse('crear_servicio'))
        self.assertEqual(response.status_code, 200)

    def test_crear_servicio_post_valido(self):
        self.client.login(email='admin@correo.com', password='adminpass')  # NOSONAR
        data = {
            'nombre': 'Nuevo Servicio',
            'descripcion': 'Descripción del servicio',
            'valor': 60000,
        }
        response = self.client.post(reverse('crear_servicio'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Servicio.objects.filter(nombre='Nuevo Servicio').exists())

    def test_crear_servicio_post_invalido(self):
        self.client.login(email='admin@correo.com', password='adminpass')  # NOSONAR
        data = {'nombre': '', 'valor': ''}  # faltan campos requeridos
        response = self.client.post(reverse('crear_servicio'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Error al crear el servicio')

    def test_pagar_servicio_get(self):
        self.client.login(email='empleado@correo.com', password='empleadopass')  # NOSONAR
        response = self.client.get(reverse('pagar_servicio'))
        self.assertEqual(response.status_code, 200)

    def test_pagar_servicio_post_valido(self):
        self.client.login(email='empleado@correo.com', password='empleadopass')  # NOSONAR
        data = {
            'servicio': self.servicio.id,
            'valor': 60000,
            'mes': 'Marzo',
            'fecha_pago': date.today()
        }
        response = self.client.post(reverse('pagar_servicio'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Pago.objects.filter(mes='Marzo').exists())

    def test_pagar_servicio_post_invalido(self):
        self.client.login(email='empleado@correo.com', password='empleadopass')  # NOSONAR
        data = {'servicio': '', 'valor': ''}  # Campos inválidos
        response = self.client.post(reverse('pagar_servicio'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Error al registrar el pago')

    def test_resumen_pagos_view(self):
        self.client.login(email='empleado@correo.com', password='empleadopass')  # NOSONAR
        response = self.client.get(reverse('resumen_pagos'))
        self.assertEqual(response.status_code, 200)

    def test_resumen_pagos_por_mes_view(self):
        self.client.login(email='empleado@correo.com', password='empleadopass')  # NOSONAR
        response = self.client.get(reverse('resumen_pagos_por_mes', args=['Enero']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enero')

