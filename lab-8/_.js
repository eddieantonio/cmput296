// open up console.

// q1.
var title = document.getElementById('main-title');
title.innerText;
// #=> "AJAX calculator"

// observe what happens when you click the submit button.

// do "preventDefault" stuff first!
//  - make it do an alert.

var form = document.getElementById('input-form');
form.addEventListener('submit', function (event) {
  // what does this do?
  event.preventDefault();
  // why is it called prevent default?

  // What is the default action for clicking the "submit" button?

  // USE ids for this instead
  //var a = form.elements.a.value;
  //var b = form.elements.b.value;
  //var op = form.elements.op.value;

  // question: how do GET requests send parameters? Do they send parameters
  // in the request body or by some other means?
  var url = 'http://localhost:8000/calc/';
  url += '?a=' + encodeURIComponent(a);
  url += '&b=' + encodeURIComponent(b);
  url += '&op=' + encodeURIComponent(op);

  var output = document.getElementById('the-answer');

  var xhr = new XMLHttpRequest();
  xhr.open('GET', url , true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.onload = function () {
    var resp = JSON.parse(xhr.responseText);
    output.innerText = resp['answer'];
    output.innerText = resp.answer;
    //output.innerText = xhr.responseText;
  };
  xhr.send();
});
