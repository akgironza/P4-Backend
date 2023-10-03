"""
URL configuration for willapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from wills.views import WillViewSet, AssetViewSet #, InheritorViewSet, InheritorGroupViewSet, DistributionViewSet

# Eventually want to try nesting the routers I think, but also want to implement auth eventually too


# New router
router = routers.DefaultRouter()
# Register viewsets
router.register(r'will', WillViewSet)
router.register(r'asset', AssetViewSet)
#router.register(r'inheritor', InheritorViewSet)
#router.register(r'inheritor-group', InheritorGroupViewSet)
#router.register(r'distribution', DistributionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('will/', include('will.urls')),
    # path('asset/', include('asset.urls')),
    path('admin/', admin.site.urls),
]
