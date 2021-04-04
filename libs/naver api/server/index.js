const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();

let port = 3000;

app.use(bodyParser.json());
app.use('/', express.static(__dirname + '/../src'));
app.use('/test', () => {
  let loc = encodeURIComponent("세종 금송로 687");
  axios.get(`https://openapi.naver.com/v1/search/local.json?query=${loc}&display=5&start=1&sort=random`, {
    headers: {
      'Content-Type': 'application/json',
      'X-Naver-Client-Id': 'hzTPPl0iFh1VRCzTYmw3',
      'X-Naver-Client-Secret': 'iUYF2LuBRU',
    },
  }).then((Response)=>{
    console.log(Response.data);
  }).catch((Error)=>{
    console.log(Error);
  })

//   fetch(`https://openapi.naver.com/v1/search/local.json?query=${loc}&display=5&start=1&sort=random`, {
//     method: 'get',
//     headers: {
//       'Content-Type': 'application/json',
//       'X-Naver-Client-Id': 'hzTPPl0iFh1VRCzTYmw3',
//       'X-Naver-Client-Secret': 'iUYF2LuBRU',
//     },

//   })
//     .then(res => res.json())
//     .then(json => console.log(json))
//     .catch(error => console.error('Error: ', error));
});

const server = app.listen(port, () => {
    console.log('Express listening on port', port);
});