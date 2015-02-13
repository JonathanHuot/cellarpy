from bottle import app
from bottle import request


def __convert_menu(route):
    entry = {
            "name": route["name"],
            "url": route["rule"],
        }
    entry.update(route["config"])
    return entry


def read_menu_entry(name):
    try:
        for route in app().routes:
            entry = route.__dict__
            if name == entry["name"]:
                return __convert_menu(entry)
        return None
    except:
        return None


def read_menu(menutitle):
    entries = []
    for route in app().routes:
        entry = route.__dict__
        if "name" not in entry or not entry["name"]:
            continue
        if "menu" not in entry["config"] or entry["config"]["menu"] != menutitle:
            continue
        entries.append(__convert_menu(entry))

    return entries


def read_breadcrumb():
    current = read_current()
    if current["name"] == "homepage":
        return []
    return [read_menu_entry(name="homepage")]


def read_current():
    return __convert_menu(request.route.__dict__)
