from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .models import ysof_comment
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.
def home_view(request):
    all_data = ysof_comment.objects.all().order_by('-created_at')
    if request.method == 'POST':
        try:
            content = request.POST.get('content')
            cleaned_content = content.strip()
            if cleaned_content != '':
                cleaned_content = ysof_comment(content=cleaned_content)
                cleaned_content.save()
                messages.success(request, '评论已成功发布！')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, '输入不能为空或只包含空格！')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except IntegrityError:
            messages.error(request, '评论发布失败，请稍后再试。')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'template_home.html', {'all_data': all_data})
