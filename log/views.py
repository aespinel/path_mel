from models import ServerLog

def send_updated_log(request):
    timestamp = request.GET.get('timestamp', None)
    if timestamp:
        rows = ServerLog.objects.filter(timestamp__gte = timestamp)
        if rows:
            data = serializers.serialize('json', rows, fields=('action','entry_table','model_id', 'timestamp'))
            return HttpResponse(data, mimetype="application/json")
    return HttpResponse("0")
