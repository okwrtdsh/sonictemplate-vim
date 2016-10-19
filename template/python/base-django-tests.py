from django.test import TestCase


class {{_expr_:substitute('{{_input_:name}}', '\w\+', '\u\0', '')}}TestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        {{_cursor_}}

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
{{_filter_:django-tests}}
