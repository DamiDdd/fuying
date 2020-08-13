module.exports = {
    configureWebpack: {
      resolve: {
        //   配置别名
        alias: {
          'components': '@/components',
          'content': 'components/content',
          'common': 'components/common',
          'assets': '@/assets',
          'network': '@/network',
          'views': '@/views',
        }
      }
    },
    chainWebpack: config => {
      const fileRule = config.module.rule('file')
      fileRule.uses.clear()
      fileRule
          .test(/\.pdf|ico$/)
          .use('file-loader')
          .loader('file-loader')
          .options({
              limit: 10000,
          })
    },
    publicPath: './'
  }
  