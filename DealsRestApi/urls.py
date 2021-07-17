from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from mainapp.views import DealView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deal/', DealView.as_view(), name='deal'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
