from django.views.generic.edit import FormView

from {{_input_:project_name}}.{{_input_:app_name}}.forms import {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}Form


class {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}FormView(FormView):
    form_class = {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}Form
    template_name = '{{_input_:app_name}}/{{_expr_:substitute('{{_input_:name}}', '\w\+', '\L\0', '')}}.html'
{{_cursor_}}
{{_filter_:django-views}}
