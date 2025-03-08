"""
URL configuration for JukeboxJam project.

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

#overall project urls
from django.contrib import admin
from django.urls import path, include

# create array of url patters
urlpatters = [
    path('admin/', admin.sit.urls),
    path('authentication/', include('authentication.urls')),
]