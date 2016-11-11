from django.apps import AppConfig
from App.models import *

class AppConfig(AppConfig):
    name = 'App'

def genericFormLoader(currentList):
    html = ""
    for item in currentList:
        if "id" not in item and "updated" not in item:
            html += "<tr><td>%s:</td><td><input name='%s'></td></tr>" %(item.replace("_", " ").capitalize(),item)
        elif "updated" not in item:
            html += "<ul>"
            for item1 in GetDatabase(item):
                html += "<li>" + item1 + "</li>"
            html += "</ul>"

    return html

def GetDatabase(currentDB):
    copy = currentDB.split(_)
    copy = copy[0]
    all_entries = copy.objects.all()
    return all_entries
