class {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}Form(forms.Form):
    {{_cursor_}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
