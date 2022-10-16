function generate() {
    const whurl = 'https://discord.com/api/webhooks/1031024264649908304/16IWYDv_DOMHRVke_L1vP5Tkw5QsYyw8Ktu1tj2lBTDjy6w9EwUC_JREMMR5kIAtMUWI'
    getMsg = document.querySelector('.prompt-input').innerHTML
    collName = document.querySelector('.name-input').innerHTML
    nftName = document.querySelector('.nft-input').innerHTML
    getMsg = '/imagine prompt:' + getMsg
    msg = {
        'content': getMsg
    }
    fetch(whurl, {'method': 'POST', 'headers': {'content-type': 'application/json'},
                   'body': JSON.stringify(msg)})

    document.querySelector('.nft6-h1').innerHTML = nftName
    document.querySelector('.nft6-coll').innerHTML = collName
    document.querySelector('.nft6-img').src = "./../static/assets/new.png"
}

$(function () {
    $(".generate-btn").on("click", function (e) {
      console.log("Called");
      const dict_values = {collName, nftName}; //Pass the javascript variables to a dictionary.
      const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
      $.ajax({
        url: "/test",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(s),
      });
    });
  });
  