from django.shortcuts import render
from django.conf import settings


# Create your views here.
def landing(request):
    language = getattr(request, "LANGUAGE_CODE", "ar")
    template_name = "landing_en.html" if language.startswith("en") else "landing.html"
    return render(request, template_name, {
        'payhip_url': settings.PAYHIP_URL,
        'free_tool_url': settings.FREE_TOOL_URL
    })