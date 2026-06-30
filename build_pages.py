# -*- coding: utf-8 -*-
import os
import re

ROOT_DIR = "c:/Users/Rihan/Desktop/ryan-shoyab-main"

# Read original index.html (ensure we check it out clean before running script)
with open(os.path.join(ROOT_DIR, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract CSS
css_match = re.search(r"<style[^>]*>(.*?)</style>", html, re.DOTALL)
if css_match:
    css_content = css_match.group(1).strip()
    with open(os.path.join(ROOT_DIR, "index.css"), "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Extracted index.css successfully!")
else:
    print("Could not find style block!")
    exit(1)

# 2. Extract JS
js_matches = re.findall(r"<script[^>]*>(.*?)</script>", html, re.DOTALL)
if len(js_matches) >= 2:
    js_content = js_matches[-1].strip()
    with open(os.path.join(ROOT_DIR, "index.js"), "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Extracted index.js successfully!")
else:
    print("Could not find interactive script block!")
    exit(1)

# 3. Extract exact prefix and layout blocks
head_idx = html.find("<head>")
body_idx = html.find("<body>")
head_content = html[head_idx:body_idx].strip()

# Clean up style block from head template
head_content_cleaned = re.sub(r"<style[^>]*>.*?</style>", '<link rel="stylesheet" href="index.css?v=1.1">', head_content, flags=re.DOTALL)

body_prefix = """<!DOCTYPE html>
<html lang="en">
""" + head_content_cleaned + """
<body>
"""

# Extract layout components
noise_html = html[html.find('<!-- SITE-WIDE NOISE OVERLAY -->'):html.find('<!-- PAGE LOADER SCREEN -->')].strip()
loader_html = html[html.find('<!-- PAGE LOADER SCREEN -->'):html.find('<!-- CUSTOM TIGER CURSOR SYSTEM -->')].strip()
cursor_html = html[html.find('<!-- CUSTOM TIGER CURSOR SYSTEM -->'):html.find('<!-- 1. NAVBAR -->')].strip()

# Extract Navbar and dynamically insert Resources nav item!
navbar_html = html[html.find('<!-- 1. NAVBAR -->'):html.find('<!-- 2. HERO SECTION -->')].strip()
navbar_html = navbar_html.replace(
    '<li><a href="#contact" class="nav-link">Contact</a></li>',
    '<li><a href="#resources" class="nav-link">Resources</a></li>\n                <li><a href="#contact" class="nav-link">Contact</a></li>'
)

contact_html = html[html.find('<!-- 10. CONTACT -->'):html.find('<!-- FOOTER -->')].strip()
contact_html = contact_html.replace(
    '<li><a href="#contact" class="nav-link">Contact</a></li>',
    '<li><a href="#resources" class="nav-link">Resources</a></li>\n                <li><a href="#contact" class="nav-link">Contact</a></li>'
)

footer_html = html[html.find('<!-- FOOTER -->'):html.find('<!-- FLOATING WHATSAPP CTA -->')].strip()
footer_html = footer_html.replace(
    '<li><a href="#contact" class="footer-link">Contact</a></li>',
    '<li><a href="#resources" class="footer-link">Resources</a></li>\n                <li><a href="#contact" class="footer-link">Contact</a></li>'
)

floating_whatsapp = html[html.find('<!-- FLOATING WHATSAPP CTA -->'):html.find('<!-- FLOATING BACK-TO-TOP BUTTON -->')].strip()
# Back-to-top button
back_to_top = """    <!-- Back to Top Button -->
    <button class="back-to-top" id="back-to-top" aria-label="Back to Top">
        <i class="fa-solid fa-arrow-up"></i>
    </button>"""

footer_suffix = """
    <!-- Shared Script -->
    <script src="index.js?v=1.1" defer></script>
</body>
</html>
"""

def make_page(body_content, title_tag=None, is_sub=False, canonical_url="https://ryanshoyab.in/", custom_head=None):
    prefix = body_prefix
    if title_tag:
        prefix = re.sub(r"<title>.*?</title>", f"<title>{title_tag}</title>", prefix)
    
    if custom_head:
        prefix = prefix.replace('</head>', f'{custom_head}\n</head>')
        
    prefix = prefix.replace('href="https://ryanshoyab.in/"', f'href="{canonical_url}"')
    
    if is_sub:
        prefix = prefix.replace('href="index.css?v=1.1"', 'href="../index.css?v=1.1"')
        body_content = body_content.replace('src="ASSETS/', 'src="../ASSETS/')
        
        # Resolve navbar links for subpage
        nav_resolved = navbar_html.replace('href="#about"', 'href="../about.html"')\
                                  .replace('href="#services"', 'href="../services.html"')\
                                  .replace('href="#portfolio"', 'href="../portfolio.html"')\
                                  .replace('href="#lab"', 'href="../lab.html"')\
                                  .replace('href="#resources"', 'href="../resources.html"')\
                                  .replace('href="#contact"', 'href="../#contact"')\
                                  .replace('href="#" class="nav-logo"', 'href="../index.html" class="nav-logo"')
        
        # Resolve contact image references
        contact_resolved = contact_html.replace('src="ASSETS/', 'src="../ASSETS/')\
                                       .replace('href="#', 'href="../#')
        
        footer_resolved = footer_html.replace('href="#', 'href="../#')\
                                      .replace('href="#" class="footer-logo"', 'href="../index.html" class="footer-logo"')\
                                      .replace('href="#resources"', 'href="../resources.html"')
        floating_whatsapp_resolved = floating_whatsapp.replace('href="#', 'href="../#')
        
        suffix = footer_suffix.replace('src="index.js?v=1.1"', 'src="../index.js?v=1.1"')
        
        return prefix + "\n    " + noise_html + "\n    " + cursor_html.replace('src="ASSETS/', 'src="../ASSETS/') + "\n    " + nav_resolved + "\n\n" + body_content + "\n\n    " + contact_resolved + "\n\n    " + footer_resolved + "\n    " + floating_whatsapp_resolved + "\n" + back_to_top + suffix
    else:
        # Resolve navbar links for root pages
        nav_resolved = navbar_html.replace('href="#about"', 'href="about.html"')\
                                  .replace('href="#services"', 'href="services.html"')\
                                  .replace('href="#portfolio"', 'href="portfolio.html"')\
                                  .replace('href="#lab"', 'href="lab.html"')\
                                  .replace('href="#resources"', 'href="resources.html"')\
                                  .replace('href="#contact"', 'href="#contact"')\
                                  .replace('href="#" class="nav-logo"', 'href="index.html" class="nav-logo"')
        
        footer_resolved = footer_html.replace('href="#" class="footer-logo"', 'href="index.html" class="footer-logo"')\
                                      .replace('href="#resources"', 'href="resources.html"')
        return prefix + "\n    " + noise_html + "\n    " + loader_html + "\n    " + cursor_html + "\n    " + nav_resolved + "\n\n" + body_content + "\n\n    " + contact_html + "\n\n    " + footer_resolved + "\n    " + floating_whatsapp + "\n" + back_to_top + footer_suffix

# Extracted segments
# 1. Hero
hero_html = html[html.find('<!-- 2. HERO SECTION -->'):html.find('<!-- 3. MARQUEE STRIP -->')].strip()
marquee_html = html[html.find('<!-- 3. MARQUEE STRIP -->'):html.find('<!-- 4. MY INTRODUCTION -->')].strip()

# 2. About section content
intro_html = html[html.find('<!-- 4. MY INTRODUCTION -->'):html.find('<!-- 6. SERVICES & PRICING -->')].strip()

# 3. Services content (Services section only, stops at Portfolio)
services_html = html[html.find('<!-- 6. SERVICES & PRICING -->'):html.find('<!-- 7. PORTFOLIO / PROJECTS -->')].strip()

# 4. Portfolio content (Portfolio section, stops at Tech Stack)
portfolio_html = html[html.find('<!-- 7. PORTFOLIO / PROJECTS -->'):html.find('<!-- TECH STACK SECTION -->')].strip()

# 5. Tech stack, process, testimonials
tech_stack_html = html[html.find('<!-- TECH STACK SECTION -->'):html.find('<!-- 8. WORK PROCESS (Pink Playful Theme) -->')].strip()
process_html = html[html.find('<!-- 8. WORK PROCESS (Pink Playful Theme) -->'):html.find('<!-- 9. TESTIMONIALS (Yellow Playful Theme) -->')].strip()
testimonials_html = html[html.find('<!-- 9. TESTIMONIALS (Yellow Playful Theme) -->'):html.find('<!-- 9.5 THE LAB & EXPERIMENTS -->')].strip()

# 6. Lab content
lab_html = html[html.find('<!-- 9.5 THE LAB & EXPERIMENTS -->'):html.find('<!-- 10. CONTACT -->')].strip()

# Build index.html
# Link navbar on the homepage directly to the separate pages!
homepage_body_sections = f"""
    {hero_html}
    {marquee_html}
    {intro_html}
    {services_html}
    {portfolio_html}
    {tech_stack_html}
    {process_html}
    {testimonials_html}
    {lab_html}
"""

with open(os.path.join(ROOT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(make_page(homepage_body_sections, "Ryan Shoyab Shaikh | AI Systems Builder & Founder", canonical_url="https://ryanshoyab.in/"))

# Build about.html
with open(os.path.join(ROOT_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(make_page(intro_html, "About Ryan Shoyab | Who I Am & Skills", canonical_url="https://ryanshoyab.in/about.html"))

# Build services.html
services_page_content = f"{services_html}\n{tech_stack_html}\n{process_html}\n{testimonials_html}"
with open(os.path.join(ROOT_DIR, "services.html"), "w", encoding="utf-8") as f:
    f.write(make_page(services_page_content, "Services & Packages | Custom Web Design & AI Automation", canonical_url="https://ryanshoyab.in/services.html"))

# Build portfolio.html
with open(os.path.join(ROOT_DIR, "portfolio.html"), "w", encoding="utf-8") as f:
    f.write(make_page(portfolio_html, "Portfolio | Realized Automation & Custom Projects", canonical_url="https://ryanshoyab.in/portfolio.html"))

# Build lab.html
# Link cards inside lab.html directly to their pages!
# Replace buttons triggers in lab_html
from generate_articles import articles
lab_html_modified = lab_html
for art in articles:
    clean_id = art['id'].replace('article-', '')
    target_btn = f'<button class="lab-link-btn btn-read-article" data-article-id="{art["id"]}">READ FULL <i class="fa-solid fa-arrow-right"></i></button>'
    replacement_link = f'<a href="lab/{clean_id}.html" class="lab-link-btn btn-read-article">READ FULL <i class="fa-solid fa-arrow-right"></i></a>'
    lab_html_modified = lab_html_modified.replace(target_btn, replacement_link)

with open(os.path.join(ROOT_DIR, "lab.html"), "w", encoding="utf-8") as f:
    f.write(make_page(lab_html_modified, "The Lab | Technical Experiments & Blogs", canonical_url="https://ryanshoyab.in/lab.html"))

# Build 26 individual article pages inside lab/ folder
os.makedirs(os.path.join(ROOT_DIR, "lab"), exist_ok=True)

for art in articles:
    article_body = f"""
    <!-- ARTICLE SECTION -->
    <section class="section-light" style="padding: 100px 0; border-bottom: 3px solid #0A0A0A;">
        <div class="container">
            <div style="margin-bottom: 40px; font-family: var(--font-body); font-weight: 700; font-size: 0.9rem; text-transform: uppercase;">
                <a href="../index.html" style="color: var(--accent-purple); text-decoration: none;">HOME</a> &nbsp;/&nbsp; 
                <a href="../lab.html" style="color: var(--accent-purple); text-decoration: none;">LAB</a> &nbsp;/&nbsp; 
                <span style="color: #666;">{art["title"]}</span>
            </div>
            
            <article class="reader-body-article" style="max-width: 800px; background: #FFFFFF; border: 3px solid #0A0A0A; box-shadow: 8px 8px 0px #0A0A0A; border-radius: 24px; padding: 50px 40px;">
                <div class="reader-meta" style="margin-bottom: 25px;">
                    <span class="reader-tag" style="background: var(--bg-pink); border: 2px solid #0A0A0A; padding: 4px 12px; border-radius: 6px; font-weight: 700; text-transform: uppercase; font-size: 0.75rem;">{art["category"]}</span>
                    <span class="reader-date" style="margin-left: 15px; color: #666; font-weight: 600;">{art["date"]}</span>
                </div>
                <h1 class="reader-title" style="font-family: var(--font-playful-alt); font-size: 2.2rem; font-weight: 700; line-height: 1.2; text-transform: uppercase; color: var(--text-dark); margin-bottom: 35px; border-bottom: 3px solid #0A0A0A; padding-bottom: 20px;">{art["title"]}</h1>
                {art["body"]}
            </article>
        </div>
    </section>
    """
    
    page_filename = f"{art['id'].replace('article-', '')}.html"
    page_path = os.path.join(ROOT_DIR, "lab", page_filename)
    
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(make_page(article_body, f"{art['title']} | Ryan Shoyab Lab", is_sub=True, canonical_url=f"https://ryanshoyab.in/lab/{page_filename}"))


# ----------------------------------------------------
# 7. GENERATE RESOURCE HUB & PROMPT DETAILS PAGES
# ----------------------------------------------------
from generate_prompts import prompts

toast_html = """
    <!-- CUSTOM TOAST NOTIFICATION -->
    <div id="custom-toast" style="position: fixed; bottom: 30px; right: 30px; background: var(--accent-yellow); color: var(--text-dark); border: 3px solid #0A0A0A; box-shadow: 6px 6px 0px #0A0A0A; border-radius: 12px; padding: 15px 25px; font-family: var(--font-body); font-weight: 700; z-index: 9999; display: none; transform: translateY(100px); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
        <span id="toast-message">Copied! 📋</span>
    </div>
    
    <script>
        function copyPrompt(id) {
            const text = document.getElementById('prompt-text-' + id).value;
            navigator.clipboard.writeText(text).then(() => {
                showToast('Prompt copied to clipboard! 📋');
            }).catch(err => {
                const textarea = document.getElementById('prompt-text-' + id);
                textarea.style.display = 'block';
                textarea.select();
                document.execCommand('copy');
                textarea.style.display = 'none';
                showToast('Prompt copied! 📋');
            });
        }

        function sharePrompt(id, url, title) {
            const shareText = `Hey {Name}! Here is the "${title}" prompt. Click it, copy it, and enjoy!\\n\\nDon't forget to follow me on Instagram @ryan.shoyab. Thanks!\\n\\nLink: ${url}`;
            navigator.clipboard.writeText(shareText).then(() => {
                showToast('Share message copied! 🔗');
            }).catch(err => {
                showToast('Share link: ' + url);
            });
        }

        function showToast(message) {
            const toast = document.getElementById('custom-toast');
            const msgSpan = document.getElementById('toast-message');
            msgSpan.innerText = message;
            toast.style.display = 'block';
            toast.offsetHeight;
            toast.style.transform = 'translateY(0)';
            
            setTimeout(() => {
                toast.style.transform = 'translateY(100px)';
                setTimeout(() => {
                    toast.style.display = 'none';
                }, 300);
            }, 2000);
        }
    </script>
"""

cards_list_html = []
for p in prompts:
    img_tag = ""
    if p.get("image"):
        img_tag = f'<div style="width: 100%; height: 180px; overflow: hidden; border: 3px solid #0A0A0A; border-radius: 16px; margin-bottom: 15px;"><img src="{p["image"]}" alt="{p["title"]}" style="width: 100%; height: 100%; object-fit: cover;"></div>'
    
    prompt_clean = p["prompt"].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    excerpt = p["prompt"][:145].strip() + ("..." if len(p["prompt"]) > 145 else "")
    ref_img_btn = ""
    if p["id"] == "004":
        ref_img_btn = '<div style="margin-bottom: 15px;"><a href="ASSETS/prompts/neobrutalist-portfolio-ref.jpg" download style="display: block; width: 100%; text-align: center; background: var(--bg-pink); color: var(--text-dark); font-weight: 700; border: 2px solid #0A0A0A; box-shadow: 3px 3px 0px #0A0A0A; border-radius: 12px; padding: 10px; font-size: 0.85rem; text-decoration: none; font-family: var(--font-body);"><i class="fa-solid fa-download"></i> DOWNLOAD REFERENCE IMAGE</a></div>'

    card_html = f"""
    <div class="resource-card-neobrutalist reveal-element" style="background: #FFFFFF; border: 3px solid #0A0A0A; box-shadow: 8px 8px 0px #0A0A0A; border-radius: 24px; padding: 30px; display: flex; flex-direction: column; height: 100%; transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.25s ease;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 8px;">
            <div style="display: flex; gap: 8px; align-items: center;">
                <span style="background: var(--accent-yellow); border: 2px solid #0A0A0A; font-family: var(--font-playful-alt); font-weight: 700; font-size: 0.85rem; padding: 4px 12px; border-radius: 8px;">#{p["id"]}</span>
                <span style="background: var(--bg-pink); border: 2px solid #0A0A0A; font-family: var(--font-body); font-weight: 700; font-size: 0.75rem; padding: 4px 12px; border-radius: 8px; text-transform: uppercase;">{p["category"]}</span>
            </div>
            <span style="background: #EAEAEA; border: 2px solid #0A0A0A; font-family: var(--font-body); font-weight: 700; font-size: 0.75rem; padding: 4px 12px; border-radius: 8px; color: #333;">By Ryan Shoyab</span>
        </div>
        {img_tag}
        <h3 style="font-family: var(--font-playful-alt); font-size: 1.35rem; font-weight: 700; color: var(--text-dark); margin: 15px 0; line-height: 1.3; text-transform: uppercase;">{p["title"]}</h3>
        <p style="font-family: var(--font-body); font-size: 0.9rem; color: #555555; line-height: 1.5; margin-bottom: 25px; flex-grow: 1;">
            {excerpt}
        </p>
        {ref_img_btn}
        <textarea id="prompt-text-{p["id"]}" style="display: none;">{prompt_clean}</textarea>
        <div style="display: flex; gap: 12px; margin-top: auto;">
            <button onclick="copyPrompt('{p["id"]}')" class="lab-link-btn" style="flex: 1; justify-content: center; background: var(--accent-yellow); color: var(--text-dark); font-weight: 700; border: 2px solid #0A0A0A; box-shadow: 3px 3px 0px #0A0A0A; border-radius: 12px; padding: 12px; font-size: 0.85rem; display: flex; align-items: center; gap: 8px; cursor: pointer;">
                <i class="fa-solid fa-copy"></i> COPY
            </button>
            <button onclick="sharePrompt('{p["id"]}', 'https://ryanshoyab.in/prompts/{p["id"]}.html', '{p["title"]}')" class="lab-link-btn" style="flex: 1; justify-content: center; background: #FFFFFF; color: var(--text-dark); font-weight: 700; border: 2px solid #0A0A0A; box-shadow: 3px 3px 0px #0A0A0A; border-radius: 12px; padding: 12px; font-size: 0.85rem; display: flex; align-items: center; gap: 8px; cursor: pointer;">
                <i class="fa-solid fa-share-nodes"></i> SHARE
            </button>
        </div>
        <div style="text-align: center; margin-top: 20px;">
            <a href="prompts/{p["id"]}.html" style="font-family: var(--font-body); font-size: 0.85rem; font-weight: 700; color: var(--accent-purple); text-decoration: underline; text-transform: uppercase;">View Full Prompt</a>
        </div>
    </div>
    """
    cards_list_html.append(card_html)

resources_grid_content = "\n".join(cards_list_html)

resources_body_content = f"""
    <!-- RESOURCE HUB PAGE SECTION -->
    <section class="section-light" style="padding: 100px 0; border-bottom: 3px solid #0A0A0A; background-color: var(--bg-cream);">
        <div class="container">
            <div class="section-header reveal-element" style="text-align: center; margin-bottom: 70px;">
                <h2 class="title-playful" style="color: var(--text-dark); margin-bottom: 15px;">RESOURCE HUB</h2>
                <p style="font-family: var(--font-body); font-size: 1.1rem; color: #555555; max-width: 600px; margin: 0 auto; font-weight: 500;">
                    Free prompts, workflows & automation templates. Copy in a single click.
                </p>
            </div>
            
            <div class="resources-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 35px;">
                {resources_grid_content}
            </div>
        </div>
    </section>
    {toast_html}
"""

with open(os.path.join(ROOT_DIR, "resources.html"), "w", encoding="utf-8") as f:
    f.write(make_page(resources_body_content, "Resource Hub | Ryan Shoyab Prompts & Tools", canonical_url="https://ryanshoyab.in/resources.html"))

# Build individual prompts folder and pages
os.makedirs(os.path.join(ROOT_DIR, "prompts"), exist_ok=True)

for p in prompts:
    img_display_tag = ""
    if p.get("image"):
        img_display_tag = f'<div style="width: 100%; max-height: 400px; overflow: hidden; border: 3px solid #0A0A0A; border-radius: 20px; margin-bottom: 30px;"><img src="../{p["image"]}" alt="{p["title"]}" style="width: 100%; height: 100%; object-fit: cover;"></div>'
    
    ref_img_download = ""
    if p["id"] == "004":
        ref_img_download = '<div style="margin-bottom: 25px;"><a href="../ASSETS/prompts/neobrutalist-portfolio-ref.jpg" download style="display: flex; justify-content: center; align-items: center; gap: 8px; width: 100%; text-align: center; background: var(--bg-pink); color: var(--text-dark); font-weight: 700; border: 2px solid #0A0A0A; box-shadow: 4px 4px 0px #0A0A0A; border-radius: 12px; padding: 15px; font-size: 0.95rem; text-decoration: none; font-family: var(--font-body);"><i class="fa-solid fa-download"></i> DOWNLOAD REFERENCE IMAGE (HIGH-RES)</a></div>'

    prompt_clean = p["prompt"].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    
    prompt_body = f"""
    <!-- PROMPT READER SECTION -->
    <section class="section-light" style="padding: 100px 0; border-bottom: 3px solid #0A0A0A; background-color: var(--bg-cream);">
        <div class="container">
            <div style="margin-bottom: 40px; font-family: var(--font-body); font-weight: 700; font-size: 0.9rem; text-transform: uppercase;">
                <a href="../index.html" style="color: var(--accent-purple); text-decoration: none;">HOME</a> &nbsp;/&nbsp; 
                <a href="../resources.html" style="color: var(--accent-purple); text-decoration: none;">RESOURCE HUB</a> &nbsp;/&nbsp; 
                <span style="color: #666;">#{p["id"]} - {p["title"]}</span>
            </div>
            
            <div style="max-width: 800px; margin: 0 auto; background: #FFFFFF; border: 3px solid #0A0A0A; box-shadow: 8px 8px 0px #0A0A0A; border-radius: 24px; padding: 40px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; flex-wrap: wrap; gap: 10px;">
                    <div style="display: flex; gap: 10px; align-items: center;">
                        <span style="background: var(--accent-yellow); border: 2px solid #0A0A0A; font-family: var(--font-playful-alt); font-weight: 700; font-size: 0.85rem; padding: 4px 12px; border-radius: 8px;">#{p["id"]}</span>
                        <span style="background: var(--bg-pink); border: 2px solid #0A0A0A; font-family: var(--font-body); font-weight: 700; font-size: 0.75rem; padding: 4px 12px; border-radius: 8px; text-transform: uppercase;">{p["category"]}</span>
                    </div>
                    <span style="background: #EAEAEA; border: 2px solid #0A0A0A; font-family: var(--font-body); font-weight: 700; font-size: 0.75rem; padding: 4px 12px; border-radius: 8px; color: #333;">Created &amp; Curated by Ryan Shoyab</span>
                </div>
                
                <h1 style="font-family: var(--font-playful-alt); font-size: 2rem; font-weight: 700; line-height: 1.3; text-transform: uppercase; color: var(--text-dark); margin-bottom: 25px; border-bottom: 3px solid #0A0A0A; padding-bottom: 15px;">{p["title"]}</h1>
                
                {img_display_tag}
                {ref_img_download}
                
                <div style="margin-bottom: 25px; display: flex; gap: 15px;">
                    <button onclick="copyPrompt('{p["id"]}')" class="lab-link-btn" style="flex: 1; justify-content: center; background: var(--accent-yellow); color: var(--text-dark); font-weight: 700; border: 2px solid #0A0A0A; box-shadow: 4px 4px 0px #0A0A0A; border-radius: 12px; padding: 15px; font-size: 0.95rem; display: flex; align-items: center; gap: 8px; cursor: pointer;">
                        <i class="fa-solid fa-copy"></i> COPY FULL PROMPT
                    </button>
                    <button onclick="sharePrompt('{p["id"]}', 'https://ryanshoyab.in/prompts/{p["id"]}.html', '{p["title"]}')" class="lab-link-btn" style="flex: 1; justify-content: center; background: #FFFFFF; color: var(--text-dark); font-weight: 700; border: 2px solid #0A0A0A; box-shadow: 4px 4px 0px #0A0A0A; border-radius: 12px; padding: 15px; font-size: 0.95rem; display: flex; align-items: center; gap: 8px; cursor: pointer;">
                        <i class="fa-solid fa-share-nodes"></i> SHARE LINK
                    </button>
                </div>
                
                <textarea id="prompt-text-{p["id"]}" style="display: none;">{prompt_clean}</textarea>
                
                <div style="background: #F9F9FB; border: 2px solid #0A0A0A; border-radius: 16px; padding: 25px; margin-top: 30px; position: relative;">
                    <span style="position: absolute; top: -12px; left: 20px; background: var(--bg-dark); color: #FFF; font-size: 0.75rem; font-weight: 700; font-family: var(--font-body); padding: 4px 12px; border-radius: 6px; border: 2px solid #0A0A0A;">PROMPT TEXT</span>
                    <pre style="white-space: pre-wrap; font-family: 'Courier New', Courier, monospace; font-size: 0.95rem; line-height: 1.6; color: #333333; overflow-x: auto; margin-top: 10px;">{p["prompt"]}</pre>
                </div>
            </div>
        </div>
    </section>
    {toast_html}
    """
    
    page_filename = f"{p['id']}.html"
    page_path = os.path.join(ROOT_DIR, "prompts", page_filename)
    
    og_img = f"https://ryanshoyab.in/{p['image']}" if p.get('image') else "https://ryanshoyab.in/ASSETS/about-ryan.jpg"
    
    og_head_tags = f"""
    <!-- Open Graph / Facebook -->
    <meta property="og:site_name" content="Ryan Shoyab Prompts">
    <meta property="og:type" content="article">
    <meta property="og:title" content="#{p["id"]} - {p["title"]} | Ryan Shoyab Prompts">
    <meta property="og:description" content="Copy prompt '{p["title"]}' in one click. Developed by Ryan Shoyab Shaikh.">
    <meta property="og:image" content="{og_img}">
    <meta property="og:image:type" content="image/jpeg">
    <meta property="og:url" content="https://ryanshoyab.in/prompts/{page_filename}">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="#{p["id"]} - {p["title"]} | Ryan Shoyab Prompts">
    <meta name="twitter:description" content="Copy prompt '{p["title"]}' in one click.">
    <meta name="twitter:image" content="{og_img}">
    """
    
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(make_page(prompt_body, f"#{p['id']} - {p['title']} | Ryan Shoyab Prompts", is_sub=True, canonical_url=f"https://ryanshoyab.in/prompts/{page_filename}", custom_head=og_head_tags))

print("Re-generated all pages successfully with full SVG tiger cursor system and Resource Hub!")
