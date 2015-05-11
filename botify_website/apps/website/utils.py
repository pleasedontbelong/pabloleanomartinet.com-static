import os

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates', 'website')
BLACKLISTED_PATHS = ('includes',)


def get_html_pages_from_site():
    return get_html_pages_from_path(TEMPLATES_PATH)
 

def get_html_pages_from_path(path):
    paths = []
    for p in os.listdir(path):
        p = os.path.join(path, p)
        if os.path.isdir(p) and p not in BLACKLISTED_PATHS:
            paths += get_html_pages_from_path(p)
        elif p.endswith('.html'):
            paths.append(p[len(TEMPLATES_PATH) + 1:])
    return paths