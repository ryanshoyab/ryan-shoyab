/* ------------------------------------------
           A. TEXT SCRAMBLE / GLITCH ANIMATION
           ------------------------------------------ */
        class TextScramble {
            constructor(el) {
                this.el = el;
                this.chars = '!<>-_\\/[]{}—=+*^?#________';
                this.update = this.update.bind(this);
            }
            setText(newText) {
                const oldText = this.el.innerText;
                const length = Math.max(oldText.length, newText.length);
                const promise = new Promise((resolve) => this.resolve = resolve);
                this.queue = [];
                for (let i = 0; i < length; i++) {
                    const from = oldText[i] || '';
                    const to = newText[i] || '';
                    const start = Math.floor(Math.random() * 40);
                    const end = start + Math.floor(Math.random() * 40);
                    this.queue.push({ from, to, start, end });
                }
                cancelAnimationFrame(this.frameRequest);
                this.frame = 0;
                this.update();
                return promise;
            }
            update() {
                let output = '';
                let complete = 0;
                for (let i = 0, n = this.queue.length; i < n; i++) {
                    let { from, to, start, end, char } = this.queue[i];
                    if (this.frame >= end) {
                        complete++;
                        output += to;
                    } else if (this.frame >= start) {
                        if (!char || Math.random() < 0.28) {
                            char = this.randomChar();
                            this.queue[i].char = char;
                        }
                        output += `<span class="scramble-char">${char}</span>`;
                    } else {
                        output += from;
                    }
                }
                this.el.innerHTML = output;
                if (complete === this.queue.length) {
                    this.resolve();
                } else {
                    this.frameRequest = requestAnimationFrame(this.update);
                    this.frame++;
                }
            }
            randomChar() {
                return this.chars[Math.floor(Math.random() * this.chars.length)];
            }
        }

        // Trigger scramble and page loader on page load
        document.addEventListener('DOMContentLoaded', () => {
            // Page loader building letters
            const loaderLogo = document.getElementById('loader-logo-text');
            if (loaderLogo) {
                const brandName = "RYAN SHOYAB";
                brandName.split("").forEach((char, index) => {
                    const span = document.createElement('span');
                    span.className = 'loader-letter';
                    span.innerHTML = char === " " ? "&nbsp;" : char;
                    span.style.animationDelay = `${index * 0.08}s`;
                    loaderLogo.appendChild(span);
                });
            }

            // Fade out loader after 2s
            setTimeout(() => {
                const loader = document.getElementById('page-loader');
                if (loader) loader.classList.add('fade-out');

                // Trigger scramble animation after loader fades
                const firstWord = document.getElementById('hero-name-first');
                const lastWord = document.getElementById('hero-name-last');
                if (firstWord) {
                    const fx1 = new TextScramble(firstWord);
                    fx1.setText('RYAN');
                }
                if (lastWord) {
                    const fx2 = new TextScramble(lastWord);
                    fx2.setText('SHOYAB');
                }
            }, 2000);
        });

        /* ------------------------------------------
           B. CUSTOM TIGER CURSOR SYSTEM
           ------------------------------------------ */
        const tigerCursor = document.getElementById('custom-tiger-cursor');
        const tigerFollower = document.getElementById('custom-tiger-follower');

        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;
        let followerX = window.innerWidth / 2;
        let followerY = window.innerHeight / 2;

        let lastMouseX = mouseX;
        let lastMouseY = mouseY;
        let facing = 1;
        let jumpY = 0;

        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;

            // Render main cursor face instantly
            if (tigerCursor) {
                tigerCursor.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
            }

            // Spawn paw print trail every 85px of movement
            const dist = Math.hypot(mouseX - lastMouseX, mouseY - lastMouseY);
            if (dist > 85) {
                createPawPrint(mouseX, mouseY);
                lastMouseX = mouseX;
                lastMouseY = mouseY;
            }
        });

        // Linear interpolation function (lerp)
        function lerp(start, end, amt) {
            return start + (end - start) * amt;
        }

        function animateCursorSystem() {
            // Distance from baby tiger to cursor pointer
            const dist = Math.hypot(mouseX - followerX, mouseY - followerY);

            // Lag behind: target offset sits 70px behind the mouse pointer
            const angle = Math.atan2(mouseY - followerY, mouseX - followerX);
            const targetFollowX = mouseX - Math.cos(angle) * 70;
            const targetFollowY = mouseY - Math.sin(angle) * 70;

            // Slowed down catch-up lag (0.05 lerp)
            followerX = lerp(followerX, targetFollowX, 0.05);
            followerY = lerp(followerY, targetFollowY, 0.05);

            // Handle Jump decay physics
            jumpY = lerp(jumpY, 0, 0.12);

            if (tigerFollower) {
                // Determine walking, running or idle states based on distance
                if (dist > 160) {
                    tigerFollower.className = "custom-tiger-follower baby-running";
                } else if (dist > 50) {
                    tigerFollower.className = "custom-tiger-follower baby-walking";
                } else {
                    tigerFollower.className = "custom-tiger-follower baby-idle";
                }

                // Smoothly determine direction (flip scaleX)
                if (mouseX > followerX + 8) {
                    facing = 1;
                } else if (mouseX < followerX - 8) {
                    facing = -1;
                }

                // Render follower baby tiger with ground shadow synced
                let transformStr = `translate3d(${followerX}px, ${followerY + jumpY}px, 0) scaleX(${facing})`;
                tigerFollower.style.transform = transformStr;
            }

            requestAnimationFrame(animateCursorSystem);
        }
        requestAnimationFrame(animateCursorSystem);

        // Click Star Burst Effect
        window.addEventListener('click', (e) => {
            createStarBurst(e.clientX, e.clientY);

            // Baby tiger physics jump trigger
            jumpY = -30;
        });

        function createStarBurst(x, y) {
            for (let i = 0; i < 8; i++) {
                const star = document.createElement('div');
                star.className = 'click-star';

                // Random angle and distance
                const angle = Math.random() * Math.PI * 2;
                const distance = Math.random() * 40 + 20;

                const tx = Math.cos(angle) * distance;
                const ty = Math.sin(angle) * distance;

                star.style.setProperty('--tx', `${tx}px`);
                star.style.setProperty('--ty', `${ty}px`);

                star.style.left = `${x}px`;
                star.style.top = `${y}px`;

                document.body.appendChild(star);
                setTimeout(() => star.remove(), 500);
            }
        }

        // Paw print trail builder
        function createPawPrint(x, y) {
            const print = document.createElement('div');
            print.className = 'paw-print-trail';
            print.style.left = `${x}px`;
            print.style.top = `${y}px`;

            // Inline SVG code for the paw print
            print.innerHTML = `
                <svg width="14" height="12" viewBox="0 0 14 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <ellipse cx="7" cy="8" rx="4.5" ry="3.5" fill="#FF8C00"/>
                    <circle cx="2" cy="3" r="1.5" fill="#FF8C00"/>
                    <circle cx="5" cy="1.5" r="1.5" fill="#FF8C00"/>
                    <circle cx="9" cy="1.5" r="1.5" fill="#FF8C00"/>
                    <circle cx="12" cy="3" r="1.5" fill="#FF8C00"/>
                </svg>
            `;

            document.body.appendChild(print);
            setTimeout(() => print.remove(), 800);
        }

        // Hover States
        // 1. Excited bounce on buttons & links
        const excitedElements = document.querySelectorAll('a, button, select, #burger-menu');
        excitedElements.forEach(el => {
            el.addEventListener('mouseenter', () => {
                if (tigerFollower) tigerFollower.classList.add('baby-excited-bounce');
                if (tigerCursor) {
                    tigerCursor.classList.add('mouth-open');
                    tigerCursor.style.transform += " scale(1.5)";
                }
            });
            el.addEventListener('mouseleave', () => {
                if (tigerFollower) tigerFollower.classList.remove('baby-excited-bounce');
                if (tigerCursor) tigerCursor.classList.remove('mouth-open');
            });
        });

        // 2. Paw swipe on portfolio card hover
        const portfolioCards = document.querySelectorAll('.project-card-neobrutalist, .tilt-card');
        portfolioCards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                if (tigerFollower) tigerFollower.classList.add('paw-swipe');
            });
            card.addEventListener('mouseleave', () => {
                if (tigerFollower) tigerFollower.classList.remove('paw-swipe');
            });
        });

        // 3. Tilt head / Sits looking up on contact form
        const contactFormSection = document.getElementById('contact');
        if (contactFormSection) {
            contactFormSection.addEventListener('mouseenter', () => {
                if (tigerFollower) tigerFollower.classList.add('head-look-up');
            });
            contactFormSection.addEventListener('mouseleave', () => {
                if (tigerFollower) tigerFollower.classList.remove('head-look-up');
            });
        }

        /* ------------------------------------------
           C. NAVBAR COLOR SCROLL SHIFT
           ------------------------------------------ */
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 80) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        /* ------------------------------------------
           D. HAMBURGER MENU TOGGLE
           ------------------------------------------ */
        const burger = document.getElementById('burger-menu');
        const navLinks = document.querySelector('.nav-links');
        const navItems = document.querySelectorAll('.nav-link');

        burger.addEventListener('click', () => {
            burger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        navItems.forEach(item => {
            item.addEventListener('click', () => {
                burger.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });

        /* ------------------------------------------
           E. PARALLAX ON HERO IMAGE
           ------------------------------------------ */
        const heroImg = document.getElementById('parallax-hero-img');
        window.addEventListener('scroll', () => {
            if (window.innerWidth > 991 && heroImg) {
                const scrolled = window.scrollY;
                heroImg.style.transform = `translateY(${scrolled * 0.15}px)`;
            }
        });

        /* ------------------------------------------
           F. MAGNETIC BUTTON EFFECT
           ------------------------------------------ */
        const magneticBtns = document.querySelectorAll('.magnetic-btn');
        magneticBtns.forEach(btn => {
            btn.addEventListener('mousemove', (e) => {
                const rect = btn.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
            });
            btn.addEventListener('mouseleave', () => {
                btn.style.transform = 'translate(0px, 0px)';
            });
        });

        /* ------------------------------------------
           G. 3D CARD TILT EFFECT (PORTFOLIO)
           ------------------------------------------ */
        const tiltCards = document.querySelectorAll('.tilt-card');
        tiltCards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;

                const xc = rect.width / 2;
                const yc = rect.height / 2;

                const angleX = (yc - y) / 15;
                const angleY = (x - xc) / 15;

                card.style.transform = `perspective(1000px) rotateX(${angleX}deg) rotateY(${angleY}deg) scale3d(1.02, 1.02, 1.02)`;
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
            });
        });

        /* ------------------------------------------
           H. STATS COUNTER ANIMATION
           ------------------------------------------ */
        const stats = document.querySelectorAll('.stat-number');
        const animateCounters = () => {
            stats.forEach(stat => {
                const target = +stat.getAttribute('data-target');
                const count = +stat.innerText;
                const speed = 200; // Alter rate here

                const inc = target / speed;

                if (count < target) {
                    stat.innerText = Math.ceil(count + inc);
                    setTimeout(animateCounters, 15);
                } else {
                    stat.innerText = target + (stat.getAttribute('data-target') === '99' ? '%' : '+');
                }
            });
        };

        /* ------------------------------------------
           I. INTERSECTION OBSERVER (SCROLL REVEAL)
           ------------------------------------------ */
        const revealElements = document.querySelectorAll('.reveal-element, .reveal-left, .reveal-right, .reveal-zoom');

        const revealCallback = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');

                    // Specific trigger if stats section is in view
                    if (entry.target.querySelector('.stat-number')) {
                        animateCounters();
                    }
                    observer.unobserve(entry.target);
                }
            });
        };

        const revealObserver = new IntersectionObserver(revealCallback, {
            root: null,
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px'
        });

        revealElements.forEach(el => {
            revealObserver.observe(el);
        });

        /* ------------------------------------------
           K. BACK-TO-TOP TRIGGER
           ------------------------------------------ */
        const backToTopBtn = document.getElementById('back-to-top');
        if (backToTopBtn) {
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTopBtn.classList.add('visible');
                } else {
                    backToTopBtn.classList.remove('visible');
                }
            });
            backToTopBtn.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        }

        /* ------------------------------------------
           J. Formspree AJAX Submission Handler & Interactive Tiger System
           ------------------------------------------ */

        // Confetti Generator
        function triggerConfetti() {
            const canvas = document.getElementById('confetti-canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;

            let particles = [];
            const colors = ['#FFE500', '#FF6B9D', '#0A0A0A', '#FFFFFF'];

            for (let i = 0; i < 70; i++) {
                particles.push({
                    x: canvas.width / 2,
                    y: canvas.height - 30,
                    vx: (Math.random() - 0.5) * 10,
                    vy: -Math.random() * 9 - 5,
                    r: Math.random() * 6 + 4,
                    color: colors[Math.floor(Math.random() * colors.length)],
                    opacity: 1
                });
            }

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                let alive = false;
                particles.forEach(p => {
                    if (p.opacity > 0) {
                        ctx.beginPath();
                        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                        ctx.fillStyle = p.color;
                        ctx.globalAlpha = p.opacity;
                        ctx.fill();
                        p.x += p.vx;
                        p.y += p.vy;
                        p.vy += 0.25; // gravity
                        p.opacity -= 0.015;
                        alive = true;
                    }
                });
                if (alive) {
                    requestAnimationFrame(draw);
                }
            }
            draw();
        }

        // DOMContentLoaded attachments for Tiger Character
        document.addEventListener('DOMContentLoaded', () => {
            const tigerImg = document.getElementById('tiger-character-img');
            const contactForm = document.getElementById('portfolio-contact-form');
            if (!tigerImg || !contactForm) return;

            const formInputs = contactForm.querySelectorAll('input, textarea, select');
            const submitBtn = contactForm.querySelector('.form-submit-btn');

            // 1. Focus / Typing Interaction
            formInputs.forEach(input => {
                input.addEventListener('focus', () => {
                    if (!tigerImg.classList.contains('tiger-celebration')) {
                        tigerImg.src = "ASSETS/tiger-seeing.png";
                        tigerImg.classList.remove('tiger-scale-bounce');
                        tigerImg.classList.add('tiger-tilt-bounce');
                    }
                });

                input.addEventListener('blur', () => {
                    if (!tigerImg.classList.contains('tiger-celebration')) {
                        setTimeout(() => {
                            const activeEl = document.activeElement;
                            if (!activeEl || !contactForm.contains(activeEl)) {
                                tigerImg.src = "ASSETS/tiger-sitting.png";
                                tigerImg.classList.remove('tiger-tilt-bounce');
                            }
                        }, 50);
                    }
                });

                input.addEventListener('input', () => {
                    if (!tigerImg.classList.contains('tiger-celebration')) {
                        tigerImg.src = "ASSETS/tiger-seeing.png";
                        tigerImg.classList.remove('tiger-scale-bounce');
                        tigerImg.classList.add('tiger-tilt-bounce');
                    }
                });
            });

            // 2. Submit Button Hover Interaction
            if (submitBtn) {
                submitBtn.addEventListener('mouseenter', () => {
                    if (!tigerImg.classList.contains('tiger-celebration')) {
                        tigerImg.src = "ASSETS/tiger-happy.png";
                        tigerImg.classList.remove('tiger-tilt-bounce');
                        tigerImg.classList.add('tiger-scale-bounce');
                    }
                });

                submitBtn.addEventListener('mouseleave', () => {
                    if (!tigerImg.classList.contains('tiger-celebration')) {
                        const activeEl = document.activeElement;
                        if (activeEl && contactForm.contains(activeEl)) {
                            tigerImg.src = "ASSETS/tiger-seeing.png";
                            tigerImg.classList.add('tiger-tilt-bounce');
                        } else {
                            tigerImg.src = "ASSETS/tiger-sitting.png";
                            tigerImg.classList.remove('tiger-tilt-bounce');
                        }
                        tigerImg.classList.remove('tiger-scale-bounce');
                    }
                });
            }
        });

        function handleFormSubmit(event) {
            event.preventDefault();
            const form = event.target;
            const loadingOverlay = document.getElementById('form-loading-overlay');
            const successOverlay = document.getElementById('form-success-overlay');
            const tigerImg = document.getElementById('tiger-character-img');

            // 1. Activate Paw Loading Spinner
            if (loadingOverlay) {
                loadingOverlay.classList.add('active');
            }

            // 2. Swap Tiger to sitting during loading state
            if (tigerImg) {
                tigerImg.src = "ASSETS/tiger-sitting.png";
                tigerImg.className = "tiger-character-img tiger-tilt-bounce";
            }

            // Wait exactly 2 seconds (simulate load)
            setTimeout(() => {
                // Hide Loading overlay
                if (loadingOverlay) {
                    loadingOverlay.classList.remove('active');
                }

                // 3. SUCCESS STATE: Show Success Overlay
                if (successOverlay) {
                    successOverlay.classList.add('active');
                }

                // Trigger Tiger celebration & confetti
                if (tigerImg) {
                    tigerImg.src = "ASSETS/tiger-happy.png";
                    tigerImg.className = "tiger-character-img tiger-celebration";
                }

                triggerConfetti();

                form.reset();

                // Clear overlays and reset animations after 6 seconds
                setTimeout(() => {
                    if (successOverlay) successOverlay.classList.remove('active');
                    if (tigerImg) {
                        tigerImg.src = "ASSETS/tiger-sitting.png";
                        tigerImg.className = "tiger-character-img";
                    }
                }, 6000);
            }, 2000);
        };

        /* ------------------------------------------
           L. THE LAB: SEARCH, FILTER & SORTING MECHANICS
           ------------------------------------------ */
        document.addEventListener('DOMContentLoaded', () => {
            const searchInput = document.getElementById('lab-search');
            const sortSelect = document.getElementById('lab-sort');
            const filterTags = document.querySelectorAll('.btn-filter-tag');
            const labGrid = document.getElementById('lab-grid');
            const labCards = document.querySelectorAll('.lab-card-neobrutalist');
            const emptyState = document.getElementById('lab-empty-state');

            let currentCategory = 'all';
            let searchQuery = '';

            function updateLabGrid() {
                let visibleCount = 0;

                labCards.forEach(card => {
                    const title = card.querySelector('.lab-card-title').innerText.toLowerCase();
                    const excerpt = card.querySelector('.lab-card-excerpt').innerText.toLowerCase();
                    const tag = card.getAttribute('data-category').toLowerCase();

                    const matchesSearch = title.includes(searchQuery) || excerpt.includes(searchQuery);
                    const matchesCategory = currentCategory === 'all' || tag === currentCategory;

                    if (matchesSearch && matchesCategory) {
                        card.style.display = 'flex';
                        visibleCount++;
                    } else {
                        card.style.display = 'none';
                    }
                });

                if (visibleCount === 0) {
                    if (emptyState) emptyState.style.display = 'block';
                } else {
                    if (emptyState) emptyState.style.display = 'none';
                }
            }

            // Search trigger
            if (searchInput) {
                searchInput.addEventListener('input', (e) => {
                    searchQuery = e.target.value.toLowerCase().trim();
                    updateLabGrid();
                });
            }

            // Category filter trigger
            filterTags.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterTags.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    currentCategory = btn.getAttribute('data-filter').toLowerCase();
                    updateLabGrid();
                });
            });

            // Sorting logic
            if (sortSelect && labGrid) {
                sortSelect.addEventListener('change', () => {
                    const sortBy = sortSelect.value; // 'latest' or 'views'
                    const cardsArray = Array.from(labCards);

                    cardsArray.sort((a, b) => {
                        if (sortBy === 'latest') {
                            const dateA = new Date(a.getAttribute('data-date'));
                            const dateB = new Date(b.getAttribute('data-date'));
                            return dateB - dateA; // descending
                        } else {
                            const viewsA = parseInt(a.getAttribute('data-views'));
                            const viewsB = parseInt(b.getAttribute('data-views'));
                            return viewsB - viewsA; // descending
                        }
                    });

                    // Re-append items to grid
                    cardsArray.forEach(card => {
                        labGrid.appendChild(card);
                    });
                });
            }

            // Article Modal Reader triggers
            const readButtons = document.querySelectorAll('.btn-read-article');
            const readerOverlay = document.getElementById('article-reader-modal-overlay');
            const readerContent = document.getElementById('reader-modal-content');
            const closeReaderBtn = document.getElementById('btn-reader-close');

            readButtons.forEach(btn => {
                btn.addEventListener('click', () => {
                    const articleId = btn.getAttribute('data-article-id');
                    const articleSource = document.getElementById(articleId);

                    if (articleSource && readerContent && readerOverlay) {
                        // Clone the article element HTML content into modal container
                        readerContent.innerHTML = articleSource.innerHTML;
                        
                        // Add lock body scroll
                        document.body.classList.add('modal-open-lock');

                        // Show Overlay
                        readerOverlay.classList.add('active');
                    }
                });
            });

            function closeReaderModal() {
                if (readerOverlay) {
                    readerOverlay.classList.remove('active');
                }
                setTimeout(() => {
                    if (readerContent) readerContent.innerHTML = '';
                    document.body.classList.remove('modal-open-lock');
                }, 300); // match transition speed
            }

            if (closeReaderBtn) {
                closeReaderBtn.addEventListener('click', closeReaderModal);
            }

            if (readerOverlay) {
                // Close when clicking background outside modal content
                readerOverlay.addEventListener('click', (e) => {
                    if (e.target === readerOverlay) {
                        closeReaderModal();
                    }
                });

                // Close on ESC key
                window.addEventListener('keydown', (e) => {
                    if (e.key === 'Escape' && readerOverlay.classList.contains('active')) {
                        closeReaderModal();
                    }
                });
            }
        });