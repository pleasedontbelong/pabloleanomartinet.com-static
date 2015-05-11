from django.http import Http404
from django.views.generic import TemplateView

from .utils import get_html_pages_from_site

HTML_PAGES = get_html_pages_from_site()


class PageView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(PageView, self).get_context_data(*args, **kwargs)
        context["signin_url"] = "https://app.botify.com/signin/"
        context["signup_url"] = "https://app.botify.com/signup/"
        context["phone_uk"] = "+44 203 475 7735"
        context["phone_fr"] = "+33 1 83 62 90 78"
        return context

    def get_template_names(self):
        path = self.kwargs.get("path", "index.html")
        if path.endswith('/'):
            path += 'index.html'

        if path not in HTML_PAGES:
            raise Http404
        full_path = "website/{}".format(path)
        return full_path