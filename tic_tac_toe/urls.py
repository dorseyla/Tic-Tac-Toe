from django.conf.urls.defaults import *
from tic_tac_toe.settings import *


urlpatterns = patterns('', 
     (r'^$', 'tic_tac_toe.views.index'),
     
     (r'^game/$', 'tic_tac_toe.views.game'),
     
     (r'^admin/', include('django.contrib.admin.urls')),
)                  