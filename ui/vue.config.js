const {defineConfig} = require('@vue/cli-service')
const glob = require('glob')

function getPages(globPath) {
    let entries = {}

    glob.sync(globPath).forEach(path => {
        const chunk = path.split('./src/pages/')[1].split('/main.ts')[0]
        entries[chunk] = {
            entry: path,
            template: 'public/index.html'
        }
    })
    return entries
}

const pages = getPages('./src/pages/**/main.ts')

module.exports = defineConfig({
    pages: pages,
    outputDir: '../analytics/statics',
    devServer: {
        proxy: {
            '^/': {
                target: 'http://localhost:8000/',
                hot: false,
                ws: false,
                liveReload: false,
                changeOrigin: true
            }
        }
    },
    transpileDependencies: true
})
