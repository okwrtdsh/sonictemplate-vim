class {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}ListView(ListView):
    model = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}
    template_name = '{{_input_:app_name}}/{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}_list.html'
    context_object_name = '{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}s'
    paginate_by = 20
{{_cursor_}}
