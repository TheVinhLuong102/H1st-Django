from django.urls.conf import include, path

from .data import urls as data_urls
from .model import urls as model_urls
from .trust import urls as trust_urls


urlpatterns = [
    path('data/', include(data_urls)),
    path('models/', include(model_urls)),
    path('trust/', include(trust_urls))
]