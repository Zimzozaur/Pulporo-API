/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'dark-grey': '#201F1F',
        'light-grey': '#D9D9D9',
        'purple': '#BAB0F8',
      }
    },
  },
  plugins: [
      require('@tailwindcss/forms')
  ],
}

