from django.views.generic.edit import UpdateView

from {{_input_:project_name}}.{{_input_:app_name}}.forms import {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}UpdateForm
from {{_input_:project_name}}.{{_input_:app_name}}.models import {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}


class {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}UpdateView(UpdateView):
    model = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}
    form_class = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}UpdateForm
    template_name = '{{_input_:app_name}}/{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}_update.html'
{{_cursor_}}
{{_filter_:django-views}}
