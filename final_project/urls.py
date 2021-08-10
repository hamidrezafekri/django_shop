from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from final_project import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('product.urls')),
                  path('accounts/', include('customer.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
