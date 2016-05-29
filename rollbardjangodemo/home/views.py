#! /usr/bin/env python2.7
from django.views.generic import TemplateView

import rollbar

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        rollbar.report_message("In Home.get", "info", request=request)
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)
