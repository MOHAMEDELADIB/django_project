const pages = {  
  index: "src/main.js",  
};  

module.exports = {
  publicPath: "/static/vue/", /*is the URL at which we can find our static files when the server is running.*/
  outputDir: "./build/static/vue/", /* is where the static files will end up after being compiled.*/
  indexPath: "../../templates/vue_index.html", /* is where our index.html file in the public folder will end up after the links to our VueJS app index.js have been injected.*/
  
  pages: pages, /* tells the Vue compiler that we have the one app and its root is at src/main.js*/

  devServer: {
    disableHostCheck: true
  }
};