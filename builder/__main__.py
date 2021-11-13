from .html_page_builder import HTMLBuilder
from .webform_generator import WebformGenerator


if __name__ == "__main__":
    forms = ["Name", "Surname", "Address"]
    webform = WebformGenerator(forms)
    html_builder = HTMLBuilder(webform)
    html_builder.build_html_file("builder/index.html")