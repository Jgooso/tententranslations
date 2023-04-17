const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  outputDir: 'template',
  assetsDir: '../static',
  publicPath: process.env.NODE_ENV === 'production'
    ? '../static/'
    : '/'
})
