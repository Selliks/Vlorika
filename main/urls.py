from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (main, login_view, registration_view, item_detail, cart_view,
                    add_to_cart, remove_from_cart, catalog_view)

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_view, name='register/login'),
    path('registration/', registration_view, name='register/registration'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('item/<int:item_id>/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('catalog/', catalog_view, name='catalog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
