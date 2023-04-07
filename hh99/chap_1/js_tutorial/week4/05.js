Array.prototype.myMap = function (callback, thisArg) {
  // map 함수에서 return할 결과 배열
  var mappedArr = [];
  console.log(thisArg);

  // 이 함수의 호출 주체는 [1, 2, 3] 배열이기 때문에 this는 배열.
  for (let i = 0; i < this.length; i++) {
    // this 바인딩을 위한 call 함수 호출
    // mappedValue에 this[i]을 할당
    // 콜백 함수 내부에서 this를 명시적으로 바인딩하기 때문에 가능
    let mappedValue = callback.call(thisArg || global, this[i]);
    mappedArr[i] = mappedValue;
  }
  return mappedArr;
};

console.log(
  [1, 2, 3].myMap(function (number) {
    return number * 2;
  })
);
