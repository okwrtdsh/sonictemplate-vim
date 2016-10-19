class {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}DeleteView(DeleteView):
    model = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}
    template_name = '{{_input_:app_name}}/{{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\L\0', '')}}_delete.html'
{{_cursor_}}
