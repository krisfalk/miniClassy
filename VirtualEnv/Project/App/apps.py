from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'App'

def genericFormLoader(currentList):
    html = ""
    for item in currentList:
<<<<<<< HEAD
        if "id" not in item and "updated" not in item:
=======
<<<<<<< HEAD
        if "id" not in item:
=======
        if "id" not in item or "updated" not in item:
>>>>>>> 7da58cf3396b267e0b091cb548c0095807fc2ef7
>>>>>>> 22917691f61d945cc4647228a622214ee117259f
            html += "<tr><td>%s:</td><td><input name='%s'></td></tr>" %(item.replace("_", " ").capitalize(),item)

    return html
