from functools import partial
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, NOT_AVAILABLE
from tastypie.validation import Validation

from api_utils import dict_to_foreign_uri, dict_to_foreign_uri_m2m, foreign_key_to_id, many_to_many_to_subfield
from models import Adoption, Attendance, Dissemination, Mediator, Person, Video, Village

class VillageResource(ModelResource):    
    class Meta:
        max_limit = None
        queryset = Village.objects.all()
        resource_name = 'village'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True

class MediatorResource(ModelResource):
    mediator_label = fields.CharField()
    villages = fields.ToManyField(VillageResource, 'villages')
    class Meta:
        max_limit = None
        authentication = SessionAuthentication()
        queryset = Mediator.objects.all()
        resource_name = 'mediator'
        authorization = DjangoAuthorization()
        validation = Validation()
        always_return_data = True
    hydrate_villages = partial(dict_to_foreign_uri_m2m, field_name='villages', resource_name = 'village')
    
    def dehydrate_villages(self, bundle):
        return [{'id': vil.id, 'name': vil.name} for vil in set(bundle.obj.villages.all()) ]

    def dehydrate_mediator_label(self,bundle):
        #for sending out label incase of dropdowns
        return ','.join([ vil.name for vil in set(bundle.obj.villages.all())])


class VideoResource(ModelResource):
    class Meta:
        max_limit = None
        queryset = Video.objects.all()
        resource_name = 'video'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True

class PersonResource(ModelResource):
    village = fields.ForeignKey(VillageResource, 'village')
    
    class Meta:
        queryset = Person.objects.prefetch_related('village').all()
        resource_name = 'person'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
    
    dehydrate_village = partial(foreign_key_to_id, field_name='village',sub_field_names=['id', 'name'])
    hydrate_village = partial(dict_to_foreign_uri, field_name = 'village')

class AdoptionResource(ModelResource):
    person = fields.ForeignKey(PersonResource, 'person')
    mediator = fields.ForeignKey(MediatorResource, 'mediator')
    class Meta:
        max_limit = None
        queryset = Adoption.objects.all()
        resource_name = 'adoption'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True

class DisseminationResource(ModelResource):
    village = fields.ForeignKey(VillageResource, 'village')
    mediator = fields.ForeignKey(MediatorResource, 'mediator')
    video = fields.ForeignKey(VideoResource, 'video')
    attendance_records = fields.ListField()
    dehydrate_village = partial(foreign_key_to_id, field_name='village',sub_field_names=['id','name'])
    dehydrate_mediator = partial(foreign_key_to_id, field_name='mediator',sub_field_names=['id','name'])
    hydrate_village = partial(dict_to_foreign_uri, field_name='village')
    hydrate_mediator = partial(dict_to_foreign_uri, field_name='mediator', resource_name='mediator')
    
    class Meta:
        max_limit = None
        queryset = Dissemination.objects.prefetch_related('village', 'mediator', 'video', 'attendance_set__person').all()
        resource_name = 'dissemination'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
    
    def obj_create(self, bundle, **kwargs):
        bundle = super(DisseminationResource, self).obj_create(bundle, **kwargs)
        dissemination_id  = getattr(bundle.obj,'id')
        att_list = bundle.data.get('attendance_records')
        for att in att_list:
            att = Attendance(dissemination_id=dissemination_id, person_id=att['person_id'], interested = att['interested'], expressed_question = att['expressed_question'])
            att.save()
        return bundle
    
    def obj_update(self, bundle, **kwargs):
        #Edit case many to many handling. First clear out the previous related objects and create new objects
        bundle = super(ScreeningResource, self).obj_update(bundle, **kwargs)
        dissemination_id = bundle.data.get('id')
        del_objs = Attendance.objects.filter(dissemination_id=dissemination_id).delete()
        att_list = bundle.data.get('attendance_records')
        for att in att_list:
            att = Attendance(dissemination_id=dissemination_id, person_id=att['person_id'], 
                                              interested = att['interested'], 
                                              expressed_question = att['expressed_question'])
            att.save()    
        return bundle
    
    def dehydrate_videoes_screened(self, bundle):
        return [{'id': video.id, 'title': video.title,} for video in bundle.obj.videoes_screened.all()]
    
    def dehydrate_attendance_records(self, bundle):
        return [{'person_id':att.person.id, 
                 'name': att.person.name, 
                 'interested': att.interested, 
                 'expressed_question': att.expressed_question, 
                 }  for att in bundle.obj.attendance_set.all()]


