class {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}FormView(FormView):
    form_class = {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}Form
    template_name = '{{_input_:app_name}}/{{_expr_:substitute('{{_input_:name}}', '\w\+', '\L\0', '')}}.html'
{{_cursor_}}
