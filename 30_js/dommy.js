// Ray Onishi & Maggie Zhao
// SoftDev1 pd7
// K#30 -- Sequential Progression III: Season of the Witch
// 2018-12-20


// Global variable for number of times the fibonacci button is clicked
var fibclick = 1;

var fibonacci = function(n) {
  'Find the nth Fibonacci number'
  //base case 1: the number is 0 -> return 0
	if ( n == 0 ) {
		return 0;
	}
  //base case 2: the number is 1 -> return 1
	if ( n == 1 ) {
		return 1;
	}
  //use recursion: find the n-1th and n-2th Fibonacci numbers and add them
	else {
		return fibonacci(n-1) + fibonacci(n-2);
	}
};

var addItem = function() {
  'Adds element to the existing list'
  var list = document.getElementById("thelist");
  var newItem = document.createElement("li");
  //newItem.setAttribute("li", )
  newItem.innerHTML = "WORD";
  list.appendChild(newItem);
}

var addFib = function() {
  'Adds element to the fibonacci list'
  var list = document.getElementById("fiblist");
  var newItem = document.createElement("li");
  //newItem.setAttribute("li", )
  newItem.innerHTML = fibonacci(fibclick);
  fibclick += 1;
  list.appendChild(newItem);
}

var but1 = document.getElementById("b");
var result1 = b.addEventListener('click', addItem);

var but2 = document.getElementById("fb");
var result2 = fb.addEventListener('click', addFib);
