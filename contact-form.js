/**
 * contact-form.js
 * ─────────────────────────────────────────────
 * Unified contact form handler for all pages.
 * Uses Web3Forms API for serverless form submission.
 * ─────────────────────────────────────────────
 */

(function () {
    'use strict';

    const CONFIG = {
        accessKey: '4bd8b9ae-f6fd-4711-b315-38ce98fe5d61',
        endpoint: 'https://api.web3forms.com/submit',
        redirectUrl: 'gracias.html',
        subjectPrefix: '[jordi.trespuntos-lab.com]',
    };

    document.addEventListener('DOMContentLoaded', () => {
        const form = document.getElementById('contact-form');
        if (!form) return;

        // ── Inject access key ──
        const accessKeyInput = document.createElement('input');
        accessKeyInput.type = 'hidden';
        accessKeyInput.name = 'access_key';
        accessKeyInput.value = CONFIG.accessKey;
        form.appendChild(accessKeyInput);

        // ── Anti-spam honeypot ──
        const honeypot = document.createElement('input');
        honeypot.type = 'checkbox';
        honeypot.name = 'botcheck';
        honeypot.style.display = 'none';
        honeypot.tabIndex = -1;
        honeypot.autocomplete = 'off';
        form.appendChild(honeypot);

        // ── Form submission ──
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const btn = form.querySelector('button[type="submit"]');
            const span = btn.querySelector('span');
            if (!btn || !span) return;

            // ── Generic Validation for all [required] fields ──
            let isValid = true;
            const requiredFields = form.querySelectorAll('[required]');

            for (const field of requiredFields) {
                if (field.type === 'checkbox') {
                    if (!field.checked) {
                        isValid = false;
                        if (field.name === 'privacy') {
                            const checkboxWrapper = field.closest('.custom-checkbox') || field;
                            shakeElement(checkboxWrapper);
                            highlightCheckbox(checkboxWrapper, true);
                            field.addEventListener('change', () => {
                                if (field.checked) highlightCheckbox(checkboxWrapper, false);
                            }, { once: true });
                        }
                    }
                } else if (!field.value.trim()) {
                    isValid = false;

                    // Handle custom select container if it's the hidden select
                    if (field.tagName === 'SELECT') {
                        const container = field.closest('.custom-select-container');
                        if (container) shakeElement(container);
                    } else {
                        shakeElement(field);
                        field.style.borderColor = '#EF4444';
                        field.addEventListener('input', () => {
                            if (field.value.trim()) field.style.borderColor = '';
                        }, { once: true });
                    }
                }
            }

            if (!isValid) return;

            // ── Loading state ──
            const originalText = span.textContent;
            const originalHTML = btn.innerHTML;
            span.textContent = 'TRANSMITIENDO...';
            btn.disabled = true;
            btn.style.opacity = '0.7';
            btn.style.pointerEvents = 'none';

            try {
                const formData = new FormData(form);

                // Remove privacy checkbox from submission (not needed in email)
                formData.delete('privacy');

                // Read input fields for dynamic email customization
                const userName = formData.get('name') || 'Desconocido';
                const projectType = formData.get('type') || 'Sin Modalidad';
                const userMessage = formData.get('message') || '';

                // Set Web3Forms specific email configuration
                formData.set('from_name', 'JordiExposito.com | LEAD🤖');
                formData.set('subject', `⚡ SEÑAL RECIBIDA: ${userName} — ${projectType}`);

                // Rename fields for a cleaner email body layout (Web3Forms uses the FormData keys as labels)
                formData.delete('name');
                formData.delete('type');
                formData.delete('message');
                formData.delete('page_title');
                formData.delete('page_url');

                // We add them back with descriptive labels
                formData.set('Nombre_Organización', userName);
                formData.set('Modalidad_Seleccionada', projectType);
                formData.set('Reto_Técnico', userMessage);
                formData.set('Página_Origen', document.title + ' (' + window.location.pathname + ')');

                const response = await fetch(CONFIG.endpoint, {
                    method: 'POST',
                    body: formData,
                });

                const result = await response.json();

                if (result.success) {
                    // ── Success → redirect ──
                    span.textContent = 'SEÑAL_ENVIADA ✓';
                    btn.style.background = '#CCFF00';
                    btn.style.color = '#000';
                    btn.style.borderColor = '#CCFF00';

                    setTimeout(() => {
                        window.location.href = CONFIG.redirectUrl;
                    }, 800);
                } else {
                    throw new Error(result.message || 'Error en el envío');
                }
            } catch (error) {
                console.error('Form submission error:', error);

                // ── Error state ──
                span.textContent = 'ERROR_TRANSMISIÓN';
                btn.style.background = '#EF4444';
                btn.style.color = '#FFF';
                btn.style.borderColor = '#EF4444';

                setTimeout(() => {
                    span.textContent = originalText;
                    btn.disabled = false;
                    btn.style.opacity = '1';
                    btn.style.pointerEvents = 'auto';
                    btn.style.background = '';
                    btn.style.color = '';
                    btn.style.borderColor = '';
                }, 3000);
            }
        });
    });

    // ── Shake animation for validation ──
    function shakeElement(el) {
        el.style.transition = 'transform 0.1s ease';
        el.style.transform = 'translateX(-6px)';
        setTimeout(() => { el.style.transform = 'translateX(6px)'; }, 100);
        setTimeout(() => { el.style.transform = 'translateX(-4px)'; }, 200);
        setTimeout(() => { el.style.transform = 'translateX(4px)'; }, 300);
        setTimeout(() => { el.style.transform = 'translateX(0)'; }, 400);
    }

    // ── Highlight checkbox error ──
    function highlightCheckbox(wrapper, hasError) {
        const checkmark = wrapper.querySelector('.checkmark');

        // Remove any previous error message
        // We inserted it after the wrapper, so its nextSibling might be the error message
        const nextEl = wrapper.nextElementSibling;
        if (nextEl && nextEl.classList.contains('checkbox-error-msg')) {
            nextEl.remove();
        }

        if (hasError) {
            // Red border on the checkmark box
            if (checkmark) {
                checkmark.style.borderColor = '#EF4444';
                checkmark.style.boxShadow = '0 0 0 2px rgba(239,68,68,0.25)';
            }
            // Red tint on the label text
            wrapper.style.color = '#EF4444';

            // Inject error message below checkbox
            const msg = document.createElement('p');
            msg.className = 'checkbox-error-msg';
            msg.style.cssText = 'font-family:"JetBrains Mono",monospace;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:#EF4444;margin-top:6px;';
            msg.textContent = '⚠ Debes aceptar las condiciones para continuar';
            wrapper.insertAdjacentElement('afterend', msg);
        } else {
            // Revert to normal
            if (checkmark) {
                checkmark.style.borderColor = '';
                checkmark.style.boxShadow = '';
            }
            wrapper.style.color = '';
        }
    }

})();
