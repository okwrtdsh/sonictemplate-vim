from django.views.generic.list import ListView

from {{_input_:project_name}}.{{_input_:app_name}}.models import {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}


class {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}ListView(ListView):
    model = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}
    template_name = '{{_input_:app_name}}/{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}_list.html'
    context_object_name = '{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}s'
    paginate_by = 20
{{_cursor_}}
{{_filter_:django-views}}
