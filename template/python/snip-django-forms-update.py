class {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}UpdateForm(forms.ModelForm):

    class Meta:
        model = {{_expr_:substitute('{{_input_:model_name}}', '\w\+', '\u\0', '')}}
        fields = [
            '{{_cursor_}}',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
