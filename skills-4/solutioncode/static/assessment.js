'use strict';

// const noValue;

//
// PROMPT 1
//
// When a user clicks on the button that says "Log In", its text should
// update and say "Log out".
//
// If a user clicks on the button again, its text should switch from "Log Out"
// to "Log In".
document.querySelector('#login-button').addEventListener('click', (evt) => {
  const loginBtn = evt.target;

  if (loginBtn.innerHTML === 'Log In') {
    loginBtn.innerHTML = 'Log Out';
  } else {
    loginBtn.innerHTML = 'Log In';
  }

  // Or:
  // loginBtn.innerHTML = loginBtn.innerHTML === 'Log Out' ? 'Log In' : 'Log Out';
});

//
// PROMPT 2
//
// This form will send an alert to a user via the built-in alert function.
//
// A user should be able to enter what they want the alert to say in the
// text box. Then, they can submit the form to trigger the alert.
document.querySelector('form').addEventListener('submit', (evt) => {
  evt.preventDefault();

  alert(document.querySelector('#alert-text').value);
});

//
// PROMPT 3
//
// This is a pretty silly feature -- when a user clicks on the
// button (the one that says "Click to add item"), a new list
// item should appear.
//
// In other words, whenever a user clicks on the button, just
// add another <li>Item</li>. So, a user has clicked on the
// button once, the list should look like this:
//
//   <ul id="list">
//     <li>Item</li>  <!-- This list item was already here -->
//     <li>Item</li>  <!-- This was added after double-clicking -->
//   </ul>


document.querySelector('#list-adder').addEventListener('click', (evt) => {
  document.querySelector('#list').insertAdjacentHTML('beforeend', '<li>Item</li>');
});


// .querySelector versus .getElementByID -> querySelector is newer, more flexible and
// uses CSS selectors. getElementbyID only used for IDs. Ultimately personal preference
// and situational choice.


//
// PROMPT 4
//
// Users should be able to change the color of any element with the
// class, "changes-colors", by clicking on the "Turn Stuff Red" button
// or "Turn Stuff Blue" button.
//
// Clicking on "Turn Stuff Red" should make text red and clicking on "Turn
// Stuff Blue" should make text blue.

function changeColorsTo(color) {
  const elementsToChange = document.querySelectorAll('.changes-colors');
  for (const element of elementsToChange) {
    element.style.color = color;
  }
}

document.querySelector('#red-changer').addEventListener('click', () => {
  changeColorsTo('red');
});

document.querySelector('#blue-changer').addEventListener('click', () => {
  changeColorsTo('blue');
});

//
// PROMPT 5
//
// Display names of 20 berries from Pokemon (a video game franchise). To
// do this, you'll make a GET request to the Pokemon RESTful API to
// retrieve data on Pokemon berries, parse the results, then add
// the names of berries to the paragraph. The paragraph should look
// something like:
//
//   <ol id="berries">
//     cheri, chesto, pecha, rawst, aspear, leppa, oran, persim,
//     lum, sitrus, figy, wiki, mago, aguav, iapapa, razz, bluk,
//     nanab, wepear, pinap
//   </ol>
//
// The Pokemon RESTful API supplies data about various items, creatures,
// and other components of Pokemon video games. It's meant to be used as an
// educational resource to help developers practice working with REST APIs.
// You don't need to sign up for a developer key to use it and it's
// completely free!
//
// We recommend that you visit their website at https://pokeapi.co/ and
// check out the example on the homepage. This will give you an idea of
// how the API works, but you'll likely need more detailed information.
// For that, head over to their API documentation at https://pokeapi.co/docs/v2.
//
// The sections that will help you out the most for this prompt are:
// "Resources Lists/Pagination" (the first section you land on when you go
// to their API docs) and "Berries" (this is the section about berries).
fetch("https://pokeapi.co/api/v2/berry/")
  .then(response => response.json())
  .then(apiResponse => {
    console.log(apiResponse.results);
    for (const berry of apiResponse.results) {
      document
        .querySelector("#berries")
        .insertAdjacentHTML("beforeend", `<li>${berry.name}</li>`);
    }
  });
//
// PROMPT 6
//
// The factorial of a number is the product of an integer and all the integers
// below it. For example, the factorial of 4 is equal to 4 * 3 * 2 * 1 = 24. The
// factorial of 6 is 6 * 5 * 4 * 3 * 2 * 1 = 720.
//
// Write the following code to calculate the factorial of a positive integer (you
// don't need to worry about negative numbers).
//
// Write a function that calculates the factorial of a positive number Add an
// event listener that catches when someone clicks on the "calculate" button and:
//   - gets whatever number is inside the "number" input field
//   - calls your function that calculates a factorial
//   - puts the result of the function inside the "result" span
//
// **DO NOT update any of the HTML provided!!!**
document.querySelector('#prompt-6 form').addEventListener('submit', (evt) => {
  evt.preventDefault();

  const num = Number(document.querySelector("#num").value);

  let result = num;
  for (let n = num - 1; n >= 1; n-- ) {
    result = result * n;
  }

  document.querySelector('#factorial-result').innerText = result;
});


// // MULTIPLE CHOICE QUESTION 7 //

// // ANSWER A
// fetch('http://172.25.2.246:5000/items/2')
//   .then(response => response.text())
//   .then(data => {
//     console.log(data)
//   });

// // ANSWER B
// fetch('http://172.25.2.246:5000/items?idx=2')
//   .then(response => response.text())
//   .then(data => {
//     console.log(data)
//   });


// // ANSWER C
//   fetch('http://172.25.2.246:5000/items?index=2')
//   .then(response => response.text())
//   .then(data => {
//     console.log(data)
//   });

// // ANSWER C
// fetch('http://172.25.2.246:5000/items?index=2')
//   .then(response => console.log(response))