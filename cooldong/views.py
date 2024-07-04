from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = {
            "name": "Hello Anirudh"
        }
        return context
