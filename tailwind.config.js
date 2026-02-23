/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./*.html"],
    darkMode: 'class',
    theme: {
        extend: {
            fontFamily: {
                sans: ['"Inter Tight"', 'sans-serif'],
                mono: ['"JetBrains Mono"', 'monospace'],
            },
            colors: {
                acid: {
                    DEFAULT: '#CCFF00',
                    dim: 'rgba(204, 255, 0, 0.1)',
                },
                zinc: {
                    950: '#09090B',
                    900: '#18181B',
                    800: '#27272A',
                    700: '#3F3F46',
                    600: '#52525B',
                    500: '#71717A',
                    400: '#A1A1AA',
                    300: '#D4D4D8',
                },
                white: {
                    off: '#EDEDED',
                }
            },
            backgroundImage: {
                'grid-pattern': "linear-gradient(to right, #27272A 1px, transparent 1px), linear-gradient(to bottom, #27272A 1px, transparent 1px)",
            },
        }
    },
    plugins: [],
}
