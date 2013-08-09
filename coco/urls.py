from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from log.views import send_updated_log
from views import coco_v2, debug, login, logout

urlpatterns = patterns('',
    (r'^login/', login),
    (r'^logout/', logout),
    (r'^debug/', debug),
    (r'^get_updated/', send_updated_log),
    (r'^$', coco_v2),
)