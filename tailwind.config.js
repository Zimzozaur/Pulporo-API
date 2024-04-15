/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'dark-grey': '#201F1F',
        'middle-grey': "#9D9C9C",
        'light-grey': '#D9D9D9',
        'main-grey': 'rgba(78, 76, 76, 0.75)',
        'purple': '#BAB0F8',
        'popup-bg': 'rgba(0, 0, 0, 0.5)',
        'close-bg': 'rgba(157, 156, 156, 0.15)',
        'menu-light-grey': '#CECECE',

      }
    },
  },
  plugins: [
      require('@tailwindcss/forms')
  ],
}

