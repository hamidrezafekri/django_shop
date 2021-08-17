from .models import *
from core.models import *

def add_var_to_context(request):
    category = Category.objects.all()
    return {
        'category': category,
    }
