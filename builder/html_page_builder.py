from builder.webform_generator import WebformGenerator


class HTMLBuilder:
    def __init__(self, webform: WebformGenerator) -> None:
        self.webform = webform

    def build_html_file(self, file_name: str) -> None:
        with open(file=file_name, mode="w") as file:
            html_page = self._build_skeleton(content=self.webform.generate_webform())
            file.write(html_page)

    def _build_skeleton(self, content: str) -> str:
        return f"<html><body>{content}</body></html>"