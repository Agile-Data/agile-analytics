module.exports = {
    purge: {
        content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
        options: {
            safelist: ['font-sans', 'bg-gray-200', 'antialiased'],
        }
    },
    theme: {
        fontFamily: {
            'sans': 'Inter var,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji'
        },
        darkMode: false
    }
}