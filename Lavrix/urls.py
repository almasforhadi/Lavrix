from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('service/', views.service, name='service'),
    path('support/', include(('support.urls', 'support'), namespace='support'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)