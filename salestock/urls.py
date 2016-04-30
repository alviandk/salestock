from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from inventory.routers import router
from inventory.views import (
        APIHomeView,
        CategoryListAPIView,
        CategoryRetrieveAPIView,
        ProductListAPIView,
        ProductRetrieveAPIView,

    )



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
)

#API Patterns
