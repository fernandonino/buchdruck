var { Readability } = require('@mozilla/readability');
var { JSDOM } = require('jsdom');
const axios = require('axios');

exports.parseArticle = (url) => {
  return axios.get(url)
    .then(function (response) {
      return response.data;
    })
    .then(function (html) {
      var doc = new JSDOM(html, {
        url: url
      });
      let reader = new Readability(doc.window.document);
      return reader.parse()
    })
    .catch(function (err) {
      console.log("ERROR: " + err);
    });
}

exports.addHeaders = () => {
  return "<html><head><stylesheets></head>";
}

exports.convertToPdf = (hypertext) => {

}

exports.send = (pdf) => {

}

exports.print = (context, urls) => {
  // initialize stream/buffer
  var hypertext = ""
  // include headers (css, etc)
  hypertext += this.addHeaders()

  hypertext += "<body>"
  
  // get html content from each url
  urls.forEach(url => {
    var parsedArticle = await parseArticle(url);
    let title = "<h2>" + parsedArticle.title + "</h2>"
    hypertext += title + parsedArticle.content
    hypertext += "<br>"
  });
  
  hypertext += "</body></html>"

  // convert to pdf
  let pressed_edition = this.convertToPdf(hypertext);
  
  // send it off!
  this.send(pressed_edition);
}