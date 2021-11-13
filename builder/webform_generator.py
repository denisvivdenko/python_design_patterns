from typing import List


class WebformGenerator:
    def __init__(self, fields: List[str]) -> None:
        self.fields = fields

    def generate_webform(self) -> str:
        generate_field = lambda field_name: f'{field_name}:<br><input type="text" name="{field_name}"><br>'
        generated_fields = [generate_field(field_name) for field_name in self.fields]
        return f"<form>{''.join(generated_fields)}</form>"