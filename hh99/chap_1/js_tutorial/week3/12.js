var numbers = [10, 20, 3, 26, 45];

var max = Math.max.apply(null, numbers);
var min = Math.min.apply(null, numbers);

console.log(Math.max(...numbers));

var max = Math.max(numbers);
var min = Math.min(numbers);

// var max = (min = numbers[0]);

// numbers.forEach(function (number) {
//   if (number > max) max = number;
//   if (number < min) min = number;
// });

console.log(max, min);
