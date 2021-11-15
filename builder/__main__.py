from .html_page_builder import HTMLBuilder
from .webform_generator import WebformGenerator


if __name__ == "__main__":
    forms = [
        {
            "type": "text_input",
            "label": "Name",
            "name": "user_name"
        },
        {
            "type": "text_input",
            "label": "Surname",
            "name": "user_surname"
        },
        {
            "type": "checkbox",
            "value": 1,
            "id": "gendre",
            "label": "male"
        },
        {
            "type": "checkbox",
            "value": 1,
            "id": "gendre",
            "label": "female"
        },
        {
            "type": "text_input",
            "label": "Address",
            "name": "user_address"
        }
    ]
    webform = WebformGenerator(forms)
    html_builder = HTMLBuilder(webform)
    html_builder.build_html_file("builder/index.html")