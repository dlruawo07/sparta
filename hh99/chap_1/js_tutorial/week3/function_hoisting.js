var getSum = (x, y) => x + y;

console.log(getSum(1, 2));
console.log(getSum("1", "2"));

var getSum = (x, y) => `${x} + ${y} = ${x + y}`;

console.log(getSum(1, 2));
console.log(getSum("1", "2"));
