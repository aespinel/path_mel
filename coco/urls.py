from django.conf.urls.defaults import include, patterns, url
from tastypie.api import Api

from log.views import send_updated_log

from api import AdoptionResource, DisseminationResource, MediatorResource, PersonResource, VideoResource, VillageResource
from views import coco_v2, debug, login, logout

v1_api = Api(api_name='v1')
v1_api.register(VillageResource())
v1_api.register(MediatorResource())
v1_api.register(PersonResource())
v1_api.register(DisseminationResource())
v1_api.register(VideoResource())
v1_api.register(AdoptionResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    (r'^login/', login),
    (r'^logout/', logout),
    (r'^debug/', debug),
    (r'^get_log/', send_updated_log),
    (r'^$', coco_v2),
)