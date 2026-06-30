# generate_prompts.py
# Compiled & Authored by Ryan Shoyab - AI & Automation Authority

prompts = [
    {
        "id": "001",
        "category": "Web Design",
        "title": "Neobrutalist UI/UX Code Generator Prompt",
        "image": "ASSETS/prompts/001.jpg",
        "prompt": """Act as a Senior Frontend Engineer. Build a high-converting single-page landing page featuring a bold Neobrutalist design language. 

DESIGN SPECS:
- Base Background: #F5F4F0 (Warm Cream)
- Card Accents: #FFE500 (Vibrant Yellow) and #FFC2E2 (Pastel Pink)
- Typography: Use Google Fonts 'Anton' for Display headings and 'Space Grotesk' for body copy.
- Borders: All elements (cards, headers, buttons) must have a thick '4px solid #0A0A0A' border.
- Shadows: Flat hard drop-shadows 'box-shadow: 8px 8px 0px #0A0A0A' that translate on hover to '12px 12px 0px #0A0A0A'.

SECTIONS:
1. Nav: Header logo left, Nav links center, CTA button right.
2. Hero: Heavy typography title '{HERO_TITLE}', sub-headline '{HERO_SUB}', and primary action button.
3. Services: 3-column card layout displaying services.
4. Contact Form: Input fields with bold borders and hover state transformations."""
    },
    {
        "id": "002",
        "category": "Automation",
        "title": "Self-Healing Multi-System Webhook Handler",
        "image": None,
        "prompt": """Act as a Lead Backend Developer. Build a Node.js Express webhook listener endpoint that acts as a fail-safe router syncing incoming lead payloads to multiple targets: active database, HubSpot CRM, and Slack alerts channel.

REQUIREMENTS:
- Implement a retry circuit breaker using exponential backoff (max 5 retries).
- If any target fails (e.g. CRM API is down), serialize the payload and push it to a local SQLite 'dead_letter_queue' table.
- Schedule a secondary cron run every 15 minutes to scan the local SQLite queue, attempt re-transmission of queued payloads, and notify sysadmin via email if failure persists beyond 24 hours."""
    },
    {
        "id": "003",
        "category": "AI Systems",
        "title": "Multimodal Semantic Extraction System",
        "image": "ASSETS/prompts/003.jpg",
        "prompt": """Act as a Senior AI Architect. Build a Python workflow using Gemini 1.5 Pro to extract semantic key-value details from unstructured documents.

INPUT: Accept PDF documents, scanned JPEGs, or text invoices.
OUTPUT: Extract raw vendor name, registered tax ID, detailed line-items array, total tax, and invoice total. Output formatting must be strictly valid JSON.
EXTRACTION PROTOCOL:
- If a value (like tax ID) is missing, do not guess; output 'UNKNOWN'.
- Run a validator check comparing line-item calculations to the total invoice amount before returning the JSON output. If they do not match, flag in a metadata block."""
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

TECH RULES: Pure HTML, CSS (inlined in &lt;style&gt;), and JavaScript (inlined at bottom in &lt;script&gt;). Single, fully self-contained HTML page output. Strict mobile-responsiveness. Keep layouts clean, semantic, and commented.

INSTRUCTIONS FOR USER:
1. Replace all curly bracket parameters {YOUR_NAME, YOUR_ROLE, etc.} in this prompt with your information.
2. Download the high-res screenshot attached to this post.
3. Attach the screenshot and paste the prompt into your AI coding tool to build your custom portfolio clone!"""
    },
    {
        "id": "005",
        "category": "AI Systems",
        "title": "Autonomous RAG Knowledge Graph Pipeline Builder",
        "image": "ASSETS/prompts/005.jpg",
        "prompt": """Act as a Graph Database & Semantic AI Specialist. Write a Python script using LangChain and Neo4j to ingest raw markdown directories and construct an entity-relationship Knowledge Graph.

FLOW STEPS:
1. Parse raw text files into chunks using semantic chunking configurations (keeping headers as node metadata).
2. Query LLM to extract entities (Persons, Concepts, Technologies) and relationships (CONTRIBUTES_TO, INTEGRATES_WITH).
3. Insert nodes and edges into Neo4j graph db, validating data format.
4. Implement hybrid retrieval combining Graph Cypher queries with vector search embeddings (Cosine Similarity) for question answering."""
    },
    {
        "id": "006",
        "category": "Web Design",
        "title": "Vibrant Neobrutalist Digital Agency Template",
        "image": "ASSETS/prompts/006.jpg",
        "prompt": """Build a premium, high-impact landing page design tailored for a modern Creative Agency. Use a loud, vibrant Neobrutalist design system.

STYLING GUIDELINES:
- Dark background accents: #121214 with thick contrasting margins.
- Accent blocks: Bright Lime Green (#00FF66), Hot Cyan (#00E5FF), and Neon Purple (#9D4EDD).
- Grid layout: Horizontal sections separated by thick 5px solid black rules.
- Typography: Display titles styled with font-family 'Bebas Neue' at massive sizes (e.g. 5rem). Monospaced metadata details using 'Share Tech Mono'.
- Interactive elements: Tilt cards that pop up by translating -8px on hover, casting dark offsets."""
    },
    {
        "id": "007",
        "category": "Automation",
        "title": "Serverless Telemetry Sync Postgres to Redis Router",
        "image": "ASSETS/prompts/007.jpg",
        "prompt": """Write a Node.js AWS Lambda serverless function triggered by a PostgreSQL database logical replication stream (via Supabase Webhooks or pg_recvlogical).

FUNCTIONAL FLOW:
1. Parse incoming write stream event (INSERT, UPDATE, DELETE) payloads.
2. Sanitize and structure metrics into telemetry objects.
3. Write clean key-value caches to Redis using EXPIRE rules (default 24 hours).
4. Run telemetry validator checking write transaction confirmation and return JSON feedback."""
    },
    {
        "id": "008",
        "category": "AI Systems",
        "title": "Agentic Coding Assistant Instruction Prompt System",
        "image": "ASSETS/prompts/008.jpg",
        "prompt": """Act as a Prompt Engineer. Build a master System Instruction prompt for an autonomous AI coding assistant.

GUIDING CONSTRAINTS:
- Establish a senior pair-programmer persona that focuses on clean, modular, tested, and self-documenting code formats.
- Force assistant to outline architectural plans BEFORE writing code.
- Prevent helper library imports unless explicitly approved by user query.
- Format all source modifications as complete, drop-in replacements, using clear Git-style diff notation."""
    },
    {
        "id": "009",
        "category": "Web Design",
        "title": "SaaS Glassmorphism Dashboard Interface CSS Schema",
        "image": "ASSETS/prompts/009.jpg",
        "prompt": """Build a responsive, modern admin dashboard styled with high-end glassmorphism and semi-transparent panels.

CSS REQUIREMENTS:
- Background: Dynamic smooth dark gradient (#1E1E2F to #0F0F1B).
- Panel styling: backdrop-filter: blur(12px), background: rgba(255, 255, 255, 0.03), and border: 1px solid rgba(255, 255, 255, 0.1).
- Card layouts: Grid container utilizing grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) for responsive metrics charts.
- Interaction: Smooth hover scaling and neon glow box-shadow transition effect."""
    },
    {
        "id": "010",
        "category": "Automation",
        "title": "N8N Lead Processing & Routing Workflow Configuration",
        "image": "ASSETS/prompts/010.jpg",
        "prompt": """Act as an Automation Architect. Design a detailed JSON workflow template schema for n8n that automates lead processing.

NODE CONNECTIONS:
1. Webhook Trigger: Captures incoming lead details.
2. Filter Gate: Routes leads by company size.
3. Enrichment Block: Queries Clearbit API for target data.
4. Database Write: Inserts enriched leads into Postgres.
5. Notification Sender: Pushes Slack alert block containing company size and clear CTA action buttons."""
    },
    {
        "id": "011",
        "category": "AI Systems",
        "title": "Semantic Embeddings Search Engine Vector Sync",
        "image": "ASSETS/prompts/011.jpg",
        "prompt": """Act as a Machine Learning Developer. Write a Python script utilizing Pinecone vector database and OpenAI embeddings to construct a semantic search system.

PIPELINE:
1. Load document strings and generate 1536-dimensional embeddings using text-embedding-ada-002.
2. Upsert vector records into Pinecone namespace, appending metadata blocks (author, timestamp, context tags).
3. Expose query API fetching top-k nearest neighbor matches with cosine similarity scores.
4. Provide fallback checks handling API exceptions cleanly."""
    },
    {
        "id": "012",
        "category": "Web Design",
        "title": "High-Converting Minimalist Realtor Portfolio UI",
        "image": "ASSETS/prompts/012.jpg",
        "prompt": """Build a responsive, high-converting portfolio website for a Luxury Real Estate Broker.

THEME SPECS:
- Palette: Soft Off-White (#FBFBFC), Muted Charcoal (#1C1D1F), and Warm Gold highlight (#D4AF37).
- Gallery Grid: Display listings cards featuring full-bleed images, clean price tags, and hover reveal animation overlays.
- Typography: Google Fonts 'Playfair Display' for luxury headings, and 'Inter' for descriptions and specifications.
- Lead CTA: Dedicated sliding contact side-drawer component."""
    },
    {
        "id": "013",
        "category": "Automation",
        "title": "Database Failover Notification & Status Telemetry",
        "image": None,
        "prompt": """Build a Python daemon script monitoring database pool connections. If network connectivity drops or query latency exceeds 1200ms, trigger alert updates to PagerDuty API and post system telemetry data to an admin dashboard status page. Maintain local cache of failures using SQLite."""
    },
    {
        "id": "014",
        "category": "AI Systems",
        "title": "Fine-Tuning Dataset Synthesizer & Validator",
        "image": None,
        "prompt": """Write a Python automation system that reads documentation files and synthesizes dataset pairs (instruction, input, response) tailored for fine-tuning LLMs. Programmatically parse and filter out any PII, validate JSON structure, and output standard HuggingFace dataset JSONL files."""
    },
    {
        "id": "015",
        "category": "Web Design",
        "title": "Retro Cyberpunk Portfolio Layout CSS Schema",
        "image": None,
        "prompt": """Design a single-file retro-futuristic Cyberpunk web layout. Use a solid black background, neon green (#39FF14) and neon pink (#FF007F) borders, monospaced font family 'Courier New', retro CRT scanline effects using CSS linear-gradients, and glitch text animations on titles."""
    },
    {
        "id": "016",
        "category": "Automation",
        "title": "Stripe Billing Ingestion & Webhook Sync Engine",
        "image": None,
        "prompt": """Build a Node.js server endpoint handling Stripe checkout.session.completed webhooks. Verify Stripe signatures, parse user details, sync pricing metadata blocks to the Postgres DB database, write active cache limits to Redis, and send HTML invoice receipts via Nodemailer."""
    },
    {
        "id": "017",
        "category": "AI Systems",
        "title": "Function-Calling LLM Tool Router Code Generator",
        "image": None,
        "prompt": """Act as a Software Architect. Write a Python application that uses LLM function-calling capabilities to route natural language requests to corresponding Python helper tools (e.g. database query, web fetch, weather API) and parse results back to readable strings."""
    },
    {
        "id": "018",
        "category": "Web Design",
        "title": "Sleek Monospaced Developer Portfolio Prompt",
        "image": None,
        "prompt": """Build a minimal monospaced portfolio theme for software engineers. Color base: #0D1117 (dark charcoal) and #58A6FF (light blue accent). Use monospaced font 'Fira Code' throughout. Include terminal-style project view boxes and interactive contact forms styled as CLI inputs."""
    },
    {
        "id": "019",
        "category": "Automation",
        "title": "GitHub Actions Automated CI/CD Deploy Monitor",
        "image": None,
        "prompt": """Write a GitHub Action YAML workflow file configured to run on pushes to the production branch. Build dependencies, run test suites, deploy production bundle to Vercel/AWS, and trigger Discord/Slack alerts reporting deploy latency, branch info, and logs link."""
    },
    {
        "id": "020",
        "category": "AI Systems",
        "title": "Semantic Guardrails & PII Masking Router Agent",
        "image": None,
        "prompt": """Act as an AI Security Specialist. Build a Python routing middleware that parses user inputs to LLM applications. Use regular expressions and semantic embeddings to detect and mask sensitive information (SSN, credit cards, emails) before forwarding payloads to external APIs."""
    }
]
