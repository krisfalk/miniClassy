from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'App'

def genericFormLoader(currentList):
    html = ""
    for item in currentList:
        if "id" not in item or "updated" not in item:
            html += "<tr><td>%s:</td><td><input name='%s'></td></tr>" %(item.replace("_", " ").capitalize(),item)

    return html
