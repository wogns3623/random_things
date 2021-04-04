test = () => {
  let req = new XMLHttpRequest();
  req.onreadystatechange = (e) => {
    if (req.readyState == 4) {
      console.log(req.responseText);
    }
  }
  req.open("GET", "https://openapi.naver.com/v1/search/local.json?query=세종 남세종로 357&display=5&start=1&sort=random", true);
  req.setRequestHeader('Content-Type', 'application/json');
  req.setRequestHeader('X-Naver-Client-Id', 'hzTPPl0iFh1VRCzTYmw3');
  req.setRequestHeader('X-Naver-Client-Secret', 'iUYF2LuBRU');
  req.send();
}