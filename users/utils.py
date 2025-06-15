# users/utils.py

def es_admin(user):
    return user.is_authenticated and user.rol == 'ADMIN'

def es_empleado(user):
    return user.is_authenticated and user.rol == 'EMPLEADO'
