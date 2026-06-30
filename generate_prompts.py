# -*- coding: utf-8 -*-

prompts = [
    {
        "id": "001",
        "category": "Web Design",
        "title": "Neobrutalist UI/UX Code Generator Prompt",
        "image": "ASSETS/prompts/001.jpg",
        "prompt": """You are an expert frontend developer specializing in Neobrutalist web design.
Generate responsive, high-performance HTML and inline CSS code for a layout based on these parameters:
- Core Colors: Light cream backgrounds (#F5F4F0), vibrant yellow buttons (#FFE500), deep black borders (#0A0A0A).
- Border styles: Thick, solid borders (3px solid #0A0A0A) and sharp hard drop-shadows (8px 8px 0px #0A0A0A).
- Typography: Inter or Space Grotesk for body, Anton for headings.
- Mobile Layout: Strict single-column stack, all components must wrap perfectly without causing horizontal overflow.

Provide clean, valid markup containing no external frameworks except FontAwesome icons."""
    },
    {
        "id": "002",
        "category": "Automation",
        "title": "Self-Healing Multi-System Webhook Handler",
        "image": None,
        "prompt": """You are a senior workflow integration engineer.
Write a script or workflow structure for n8n or Make.com that implements a self-healing webhook receiver:
- Payload Ingestion: Receive custom lead parameters from a client contact form.
- Sanitization: Validate email string and format phone numbers to standard E.164.
- Integration: Sync leads data directly with HubSpot API and Salesforce REST API.
- Error Handling: On any REST connection timeout, retry 3 times with exponential backoff (initial delay: 5s).
- Alerting: If all retries fail, post structured error details to Slack alert webhook and cache payload in a local SQLite failover db."""
    },
    {
        "id": "003",
        "category": "AI Systems",
        "title": "Multimodal Semantic Extraction System",
        "image": "ASSETS/prompts/003.jpg",
        "prompt": """You are a lead AI research engineer working with multimodal LLMs.
Design an instruction prompt for Gemini 1.5 Pro to extract structured metadata from raw invoice images:
- Goal: Extract vendor name, tax ID, line-item table details, and total amount.
- Output Format: Strictly output valid JSON adhering to a specified schema. Do not enclose the output in backticks or add markdown text.
- Fallbacks: If tax ID is missing, set value to 'UNKNOWN_OR_NOT_PRESENT'.
- Zero-Shot Examples: Include three distinct test case structures to guide semantic analysis."""
    },
    {
        "id": "004",
        "category": "Web Design",
        "title": "Neobrutalist Clone Generator Prompt (With Placeholders)",
        "image": "ASSETS/prompts/004.jpg",
        "prompt": """LETS MAKE A SAME EXACT DESIGN WEBSITE SAME FONT SAME COLOR BUT FOR ME. You are building a personal portfolio website for {YOUR_NAME} – a {YOUR_AGE}-year-old {YOUR_ROLE} from {YOUR_CITY}.

STRICT REFERENCE: Follow the uploaded screenshot reference image EXACTLY for layout structure, spacing hierarchy, Neobrutalist design grids, and typography styling.

### 🎨 DESIGN SYSTEM & STYLING SPECIFICATIONS
1. COLOR PALETTE:
   - Background (Dark Mode sections): #0A0A0A (solid near-black)
   - Background (Light Mode sections): #F5F4F0 (clean, warm cream)
   - Accent Yellow: #FFE500 (solid bright warning yellow)
   - Accent Pink: #FFC2E2 (bubblegum pastel pink)
   - Accent Purple: #8B5CF6 (neon purple)
   - Text Colors: #0A0A0A (dark typography elements) and #FFFFFF / #CCCCCC (light typography elements)
   - Borders: Thick solid black '3px solid #0A0A0A' on all cards, header navbars, inputs, and button elements.
2. NEOBRUTALIST CARDS & COMPONENT DESIGN:
   - Background: #FFFFFF inside light sections, rgba(255,255,255,0.05) with backdrop-filter: blur(10px) (glassmorphism) inside dark sections.
   - Shadow Schema: Flat hard drop-shadow offset 'box-shadow: 8px 8px 0px #0A0A0A'.
   - Hover Action: Transform cards by translating (-6px, -6px) and increasing drop-shadow offset to '14px 14px 0px #0A0A0A' via transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.25s ease.
3. TYPOGRAPHY & FONT ASSIGNMENTS:
   - Primary Display Titles: Google Fonts 'Anton' or 'Bebas Neue' (uppercase, massive weight displays)
   - Accent Subheads & Badges: 'Unbounded' or 'Fredoka' (bold geometric/blocky styles)
   - Body Paragraphs & Form Fields: 'Space Grotesk' (modern monospace-feeling sans-serif)

### ✨ INTERACTIVE ANIMATIONS & JS SCRIPTS
1. SITE-WIDE NOISE OVERLAY:
   - Render a fixed .noise-overlay div with a repeating inline SVG noise pattern to produce a premium grainy grit/texture across all sections.
2. CUSTOM TIGER CURSOR SYSTEM:
   - Render a custom SVG tiger head inside `#custom-tiger-cursor` div.
   - Render a paw print '🐾' inside `#custom-tiger-follower` div.
   - Implement vanilla JS lag/easing: tiger head coordinates map to mouse movement instantly, while paw print lags behind using linear interpolation calculations (x += (targetX - x) * 0.15).
3. PAGE LOADER:
   - An overlay screen fading out after 2 seconds, displaying a letter-building scramble animation of the display name text.
4. TEXT SCRAMBLE / GLITCH ANIMATION:
   - A custom JS function cycling randomly through characters ('@#$&%?!*') and resolving letters one-by-one to create a reveal effect on hover or loading for headings.
5. MAGNETIC HOVER BUTTONS:
   - Add magnetic hover calculation script to '.magnetic-btn' elements. If mouse cursor distance to button centroid < 60px, shift button offset slightly towards mouse position.
6. PARALLAX CARD TILT:
   - Apply mouse-parallax 3D rotation transforms to project cards on hover using JavaScript ('transform: perspective(1000px) rotateX(...) rotateY(...)').
7. STAT COUNTERS INCREMENTER:
   - Automatically increment numeric metrics (Projects, Clients) using a JS counter script triggered via Intersection Observer when scrolled into view.
8. INFINITE SCROLLING TICKERS:
   - Infinite horizontal marquee tickers running with CSS keyframe animation. Text should read: '{YOUR_ROLE_TAGS} • {YOUR_CITY} • AVAILABLE FOR WORK •' separated by rotating neobrutalist stars.

### 🧩 LAYOUT & SECTIONS (In Exact Order)
1. NAVBAR: Logo text '{YOUR_NAME}' left, navigation links right: About, Services, Portfolio, Contact.
2. HERO SECTION:
   - Left Panel: Warning pill tag 'Currently Available for Work', giant Display Name '{YOUR_NAME}', sub-roles marquee list, CTA buttons ('Let's Work Together', 'View My Work').
   - Right Panel: Hero image matching layout profile inside a thick Neobrutalist frame with offset shadow.
3. MARQUEE STRIP: Infinite scrolling text strip using Neobrutalist layout separators.
4. INTRODUCTION: Large bold header + short intro text + stats counter grid (e.g. Projects Built, Happy Clients, Coffee Drunk).
5. ABOUT ME: Section detailing story and backgrounds in split-pane grid.
6. SERVICES & PRICING: Neobrutalist cards listing detailed packages:
   - Service 1: {SERVICE_1_TITLE} – Starting from {SERVICE_1_PRICE}
   - Service 2: {SERVICE_2_TITLE} – Starting from {SERVICE_2_PRICE}
   - Service 3: {SERVICE_3_TITLE} – Starting from {SERVICE_3_PRICE}
   - Service 4: {SERVICE_4_TITLE} – Starting from {SERVICE_4_PRICE}
7. PORTFOLIO / PROJECTS: Neobrutalist cards with image previews, tags, titles, descriptions, and custom mouse-hover tilt scripts.
8. WORK PROCESS: A numbered horizontal process timeline showing steps: 01 Discovery, 02 Design, 03 Build, 04 Deploy.
9. TESTIMONIALS: User reviews carousel styled in yellow/pink Neobrutalist aesthetic.
10. CONTACT: Form 'LET'S BUILD TOGETHER' with email input, message textarea, and Neobrutalist submit button, alongside a WhatsApp floating chat widget.

TECH RULES: Pure HTML, CSS (inlined in <style>), and JavaScript (inlined at bottom in <script>). Single, fully self-contained HTML page output. Strict mobile-responsiveness. Keep layouts clean, semantic, and commented.

INSTRUCTIONS FOR USER:
1. Replace all curly bracket parameters {YOUR_NAME, YOUR_ROLE, etc.} in this prompt with your information.
2. Download the high-res screenshot attached to this post.
3. Attach the screenshot and paste the prompt into your AI coding tool to build your custom portfolio clone!"""
    }
]
