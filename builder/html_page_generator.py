from builder.webform_builder import WebformBuilder


class HTMLPageGenerator:
    def __init__(self, webform: WebformBuilder) -> None:
        self.webform = webform

    def build_html_file(self, file_name: str) -> None:
        with open(file=file_name, mode="w") as file:
            html_page = self._build_skeleton(content=self.webform.generate_webform())
            file.write(html_page)

    def _build_skeleton(self, content: str) -> str:
        return "<html><body>{0}\n</body></html>".format(
            content
        )