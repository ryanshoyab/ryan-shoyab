# -*- coding: utf-8 -*-
import os
from datetime import datetime

ROOT_DIR = "c:/Users/Rihan/Desktop/ryan-shoyab-main"

# Static lists of pages
static_pages = [
    {"loc": "", "priority": "1.0", "changefreq": "weekly"},
    {"loc": "about.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "services.html", "priority": "0.9", "changefreq": "monthly"},
    {"loc": "portfolio.html", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "lab.html", "priority": "0.9", "changefreq": "weekly"},
    {"loc": "resources.html", "priority": "0.9", "changefreq": "weekly"}
]

# Generate article list
articles_dir = os.path.join(ROOT_DIR, "lab")
article_pages = []
if os.path.exists(articles_dir):
    for f in os.listdir(articles_dir):
        if f.endswith(".html"):
            article_pages.append({
                "loc": f"lab/{f}",
                "priority": "0.7",
                "changefreq": "monthly"
            })

# Generate prompts list
prompts_dir = os.path.join(ROOT_DIR, "prompts")
prompt_pages = []
if os.path.exists(prompts_dir):
    for f in os.listdir(prompts_dir):
        if f.endswith(".html"):
            prompt_pages.append({
                "loc": f"prompts/{f}",
                "priority": "0.7",
                "changefreq": "monthly"
            })

all_pages = static_pages + article_pages + prompt_pages
today = datetime.today().strftime('%Y-%m-%d')

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for p in all_pages:
    url = f"https://ryanshoyab.in/{p['loc']}"
    sitemap_xml += f"  <url>\n"
    sitemap_xml += f"    <loc>{url}</loc>\n"
    sitemap_xml += f"    <lastmod>{today}</lastmod>\n"
    sitemap_xml += f"    <changefreq>{p['changefreq']}</changefreq>\n"
    sitemap_xml += f"    <priority>{p['priority']}</priority>\n"
    sitemap_xml += f"  </url>\n"

sitemap_xml += '</urlset>\n'

with open(os.path.join(ROOT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print(f"Generated sitemap.xml successfully with {len(all_pages)} pages!")
