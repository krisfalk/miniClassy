from django.apps import AppConfig
from App.models import *
import sys

class AppConfig(AppConfig):
    name = 'App'

def genericFormLoader(currentList):
    html = ""
    for item in currentList:
        if "id" not in item and "updated" not in item:
            html += "<tr><td>%s:</td><td><input name='%s'></td></tr>" %(item.replace("_", " ").capitalize(),item)
        elif "updated" not in item:
            if "id" != item:
                html += "<select>"
                temp2 = item.split("_")
                name = temp2[0].capitalize()
                for item1 in GetDatabase(name):
                    html += "<option>"
                    for entry in item1.__dict__.values():
                        html += str(entry) + " "
                    html += "</option>"
                    # html += "<li>" + item1.street_name + "</li>"
                html += "</select>"

    return html

def GetDatabase(currentDB):
    all_entries = globals()[currentDB].objects.all()
    return all_entries
