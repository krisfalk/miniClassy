from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'App'

def genericFormLoader(currentList):
    html = ""
    for item in currentList:
        if item != "id":
            html += "<tr><td>%s:</td><td><input name='%s'></td></tr><br />" %(item,item)

    return html
