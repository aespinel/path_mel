from datetime import datetime
from django.forms.models import model_to_dict
from models import ServerLog

class TimestampException(Exception):
    pass

class UserDoesNotExist(Exception):
    pass

def save_log(sender, **kwargs ):
    instance = kwargs["instance"]
    action  = kwargs["created"]
    sender = sender.__name__    # get the name of the table which sent the request
    model_dict = model_to_dict(instance)
    log = ServerLog(action = action, entry_table = sender, model_id = instance.id)
    log.save()

def delete_log(sender, **kwargs ):
    instance = kwargs["instance"]
    sender = sender.__name__    # get the name of the table which sent the request
    try:
        log = ServerLog(village = instance.get_village(), user = user, action = -1, entry_table = sender, model_id = instance.id, partner = instance.get_partner())
        log.save()
    except Exception as ex:
        pass
