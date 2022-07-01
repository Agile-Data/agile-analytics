const {defineConfig} = require('@vue/cli-service')
const glob = require('glob')
const path = require("path");

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
    parallel: 8,
    transpileDependencies: true,
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
    chainWebpack: config => {
        config.module.rules.delete("svg");
        config.module.rule('svg-sprite-loader').test(/\.svg$/)
            .include
            .add(path.resolve('./src/assets/svg'))
            .end()
            .use('svg-sprite-loader')
            .loader('svg-sprite-loader')
            .options({
                symbolId: 'icon-[name]'
            })
    },
})
