from django.views.generic.edit import CreateView

from {{_input_:project_name}}.{{_input_:app_name}}.forms import {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}CreateForm
from {{_input_:project_name}}.{{_input_:app_name}}.models import {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}


class {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}CreateView(CreateView):
    model = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}
    form_class = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}CreateForm
    template_name = '{{_input_:app_name}}/{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}_create.html'
{{_cursor_}}
{{_filter_:django-views}}
