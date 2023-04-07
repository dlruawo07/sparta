// 인자에 대한 제어권
// map: 배열의 요소를 순회하며 가공하여 새로운 배열을 반환

const arr = [10, 20, 30];
let newArr = arr.map(function (index, currentValue) {
  console.log(index, currentValue);
  return index + 5;
});

console.log(newArr);
