from typing import Dict, List

from builder.html_field import HTMLFieldDirector


class WebformBuilder:
    def __init__(self, fields: List[Dict[str, str]]) -> None:
        self.fields = fields

    def generate_webform(self) -> str:
        generated_fields = ["\n" + str(HTMLFieldDirector(field_parameter)) for field_parameter in self.fields]
        return f"<form>{''.join(generated_fields)}</form>"