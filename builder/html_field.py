from typing import Dict


class HTMLFieldDirector:
    def __init__(self, field_parameters: Dict[str, str]) -> None:
        self.html = ""
        field_type = field_parameters["type"]
        if field_type == "text_input":
            self.html = self._constract_text_field(field_parameters)
        elif field_type == "checkbox":
            self.html = self._constract_checkbox_field(field_parameters)
        else:
            raise TypeError("Unknown HTML field type.")

    def __str__(self):
        return self.html

    def _constract_text_field(self, parameters: Dict[str, str]) -> str:
        return f'{parameters["label"]}:<br><input type="text" name="{parameters["name"]}"><br>'

    def _constract_checkbox_field(self, parameters: Dict[str, str]) -> str:
        return f'<label><input type="checkbox" id="{parameters["id"]}" \
                value="{parameters["value"]}"> {parameters["label"]}<br>'

