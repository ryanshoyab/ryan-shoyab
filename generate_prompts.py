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

STRICT REFERENCE: Follow the uploaded screenshot reference image EXACTLY for:
- Layout structure (full-width sections, large bold typography)
- Black & cream/off-white color base
- Bold chunky display fonts (Anton/Space Grotesk)
- Yellow accent color (#FFE500) for highlights/badges
- Card-based services & pricing section
- Testimonials section with cards
- Work process numbered steps section

MUST HAVE ANIMATIONS:
- Smooth scroll reveal animations on every section
- Glassmorphism cards (backdrop-filter: blur, semi-transparent background)
- Magnetic hover effect on buttons
- Text scramble/glitch animation on hero name
- Parallax scrolling on hero section
- Floating animation on accent elements
- Card tilt effect on hover (project cards)
- Marquee/ticker scrolling text strip (e.g. "AVAILABLE FOR WORK • {YOUR_TAG_1} • {YOUR_TAG_2}")
- Counter animation for stats
- Cursor custom effect

SECTIONS (in this exact order):
1. Navbar – {YOUR_NAME} with nav links: About, Services, Portfolio, Contact
2. Hero – Giant bold name "{YOUR_NAME}" with badge "{YOUR_ROLE}", 
   sub-tags: {YOUR_TAG_1} • {YOUR_TAG_2} • {YOUR_TAG_3}
   + my photo on right side
3. Marquee strip – scrolling text "{YOUR_TAG_1} • {YOUR_TAG_2} • {YOUR_TAG_3}"
4. My Introduction – bold large heading + short para about me + photo
5. About Me – "WHO I AM" section with my story: {YOUR_STORY_DETAILS}
6. Services & Pricing – card grid with:
   - {SERVICE_1_TITLE} – starting from {SERVICE_1_PRICE}
   - {SERVICE_2_TITLE} – starting from {SERVICE_2_PRICE}
   - {SERVICE_3_TITLE} – starting from {SERVICE_3_PRICE}
   - {SERVICE_4_TITLE} – starting from {SERVICE_4_PRICE}
7. Portfolio/Projects – cards for custom projects: {YOUR_PROJECT_1}, {YOUR_PROJECT_2}, etc.
8. Work Process – 4 steps: 01 Discovery, 02 Design, 03 Build, 04 Deploy
9. Testimonials – card layout (placeholder cards)
10. Contact – "LET'S BUILD TOGETHER" with WhatsApp button + email form

TECH: Pure HTML, CSS, JavaScript – single file
FONTS: Use Google Fonts – "Space Grotesk" for body, "Bebas Neue" or "Anton" for display headings
COLOR PALETTE:
- Background: #0A0A0A
- Cards: rgba(255,255,255,0.05) with blur (glassmorphism)
- Accent: #FFE500
- Text: #FFFFFF and #CCCCCC
- Borders: rgba(255,255,255,0.1)

IMPORTANT RULES:
- Mobile responsive
- NO frameworks, NO React – pure HTML/CSS/JS only
- All animations must be CSS + vanilla JS (Intersection Observer for scroll reveal)
- Image placeholders where I will drop my assets
- Code must be clean and commented
- Single HTML file output

INSTRUCTIONS FOR USER:
1. Download the site screenshot reference image attached to this post.
2. Replace all curly bracket parameters {YOUR_NAME, YOUR_ROLE, etc.} in this prompt text with your personal details.
3. Paste the modified prompt and attach the downloaded screenshot image to Antigravity (or another AI coding assistant) and run it! Your custom portfolio will be created instantly."""
    }
]
