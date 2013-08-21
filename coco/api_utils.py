from django.forms.models import model_to_dict

def many_to_many_to_subfield(bundle, field_name, sub_field_names):
    sub_fields = getattr(bundle.obj, field_name).values(*sub_field_names)
    return list(sub_fields)

def foreign_key_to_id(bundle, field_name,sub_field_names):
    field = getattr(bundle.obj, field_name)
    if(field == None):
        dict = {}
        for sub_field in sub_field_names:
            dict[sub_field] = None 
    else:
        dict = model_to_dict(field, fields=sub_field_names, exclude=[])
    return dict

def dict_to_foreign_uri(bundle, field_name, resource_name=None):
    field_dict = bundle.data.get(field_name)
    print field_dict
    if field_dict:
        bundle.data[field_name] = "/coco/api/v1/%s/%s/"%(resource_name if resource_name else field_name, 
                                                    str(field_dict.get('id')))
    else:
        bundle.data[field_name] = None
    return bundle

def dict_to_foreign_uri_m2m(bundle, field_name, resource_name):
    #print resource_name, bundle
    #print field_name
    m2m_list = bundle.data.get(field_name)
    resource_uri_list = []
    print m2m_list
    if m2m_list:
        print 'in m2m list'
        for item in m2m_list:
            try:
                resource_uri_list.append("/coco/api/v1/%s/%s/"%(resource_name, str(item.get('id'))))
            except:
                return bundle
    bundle.data[field_name] = resource_uri_list
    return bundle
