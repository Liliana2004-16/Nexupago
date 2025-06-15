from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from functools import wraps

def rol_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')  # Ajusta al nombre correcto si tu login se llama diferente
            if request.user.rol in roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("No tienes permiso para acceder a esta vista.")
        return _wrapped_view
    return decorator
