# -*- coding: utf-8 -*-
from django.db.models.loading import get_model
from django.http import HttpResponse, JsonResponse


class Content(object):
    def process_request(self, request):
        if request.POST.get('namerequest') == 'editable_text':
            if request.is_ajax() and request.user.is_admin:
                try:
                    model_path, property, obj_id = str(request.POST['data_info']).split('+')
                    text = request.POST['text']
                    app_label, t, model_name = model_path.split('.')
                    model = get_model(app_label=app_label, model_name=model_name)
                    obj = model.objects.get(pk=obj_id)
                    obj.__setattr__(property, text)
                    obj.save()
                except:
                    return JsonResponse({'status': False})

                return JsonResponse({'status': True, 'text': text})
