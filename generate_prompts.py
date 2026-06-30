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
    }
]
