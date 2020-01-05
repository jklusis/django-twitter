const mix = require('laravel-mix');

const staticPath = 'static/build'
const resourcesPath = 'resources'

mix.setResourceRoot('/static/build')
mix.setPublicPath('static')

// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes('--browser-sync')) {
  mix.browserSync('localhost:8000')
}

mix.js(`${resourcesPath}/js/app.js`, `${staticPath}/js/app.js`)
mix.sass(`${resourcesPath}/sass/app.scss`, `${staticPath}/css/app.css`)