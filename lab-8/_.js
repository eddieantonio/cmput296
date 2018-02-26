// open up console.

// q1.
var title = document.getElementById('main-title');
title.innerText;
// #=> "AJAX calculator"


// observe what happens when you click the submit button.

// do "preventDefault" stuff first!
//  - make it do an alert.

var output = document.getElementById('the-answer');

var form = document.getElementById('input-form');


form.addEventListener('submit', function (submitEvent) {
  submitEvent.preventDefault();

  // Get form attributes by name.
  var a = form.elements['a'].value;
  var b = form.elements['b'].value;
  var op = form.elements['op'].value;

  // Construct the URL.
  var url = 'http://localhost:8000/calc/';
  url += '?a=' + encodeURIComponent(a);
  url += '&b=' + encodeURIComponent(b);
  url += '&op=' + encodeURIComponent(op);

  var xhr = new XMLHttpRequest();
  xhr.open('GET', url , true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.onload = function (_loadEvent) {
    // alternative to xhr: loadEvent.target
    var resp = JSON.parse(xhr.responseText);
    output.innerText = resp['answer'];
    output.innerText = resp.answer;
    //output.innerText = xhr.responseText;
  };
  xhr.send();
});
