"""
Fixes VSTS coverage reports by inlining CSS files.
see https://github.com/Microsoft/vsts-tasks/issues/3027
Based on https://stackoverflow.com/a/23190429/7417402
"""
import os

import bs4

COVERAGE_REPORT_DIR = 'htmlcov/'
COVERAGE_REPORT = os.path.join(COVERAGE_REPORT_DIR, 'index.html')


def embed_css_in_html_file(html_file, css_dir):
    with open(html_file, 'r') as f:
        soup = bs4.BeautifulSoup(f.read(), "html.parser")

    stylesheets = soup.findAll("link", {"rel": "stylesheet"})
    for s in stylesheets:
        t = soup.new_tag('style')
        css_file = s["href"]
        print(f"found link to {css_file}")
        with open(os.path.join(css_dir, css_file), 'r') as f:
            c = bs4.element.NavigableString(f.read())
        t.insert(0, c)
        t['type'] = 'text/css'
        s.replaceWith(t)

    with open(html_file, 'w') as f:
        f.write(str(soup))


for file in os.listdir(COVERAGE_REPORT_DIR):
    if file.endswith(".html"):
        print(f"Embedding CSS in {file}")
        embed_css_in_html_file(os.path.join(COVERAGE_REPORT_DIR, file), COVERAGE_REPORT_DIR)
