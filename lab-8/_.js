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
  // what does this do?
  submitEvent.preventDefault();
  // why is it called prevent default?

  // Question: What is the default action for clicking the "submit" button?

  // Get form attributes by name.
  var a = form.elements['a'].value;
  var b = form.elements['b'].value;
  var op = form.elements['op'].value;

  // Question: what does form.elements['op'] give you?
  // Question: what does form.elements['op'].value you give you?
  //           use the drop-down on the webpage to change the operation
  //           now what does form.elements['op'].value

  // Question: how do GET requests send parameters? Do they send parameters
  // in the request body or by some other means?

  // Question: What's the difference between
  //
  // "op=" + op
  // and "op=" + encodeURIComponent(op)?
  //
  // Which one is correct? Why is the other one incorrect?
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
