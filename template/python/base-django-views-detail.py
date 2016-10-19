from django.views.generic.detail import DetailView

from {{_input_:project_name}}.{{_input_:app_name}}.models import {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}


class {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}DetailView(DetailView):
    model = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}
    template_name = '{{_input_:app_name}}/{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}_detail.html'
    context_object_name = '{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}s'
{{_cursor_}}
{{_filter_:django-views}}
