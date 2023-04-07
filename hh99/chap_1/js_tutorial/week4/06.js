// obj
// 2가지 속성

var obj = {
  vals: [1, 2, 3],
  logValues: function (v, i) {
    console.log(">>> test starts");
    if (this !== global) console.log(this, v, i);
    console.log(">>> test ends");
  },
};

// method로서 호출
obj.logValues(1, 2);

console.log();

// obj에 있는 logValues 함수를 global에서 호출
// (위의 logValues에서 function (~~~) 부분을 넣은 것과 같음)
[4, 5, 6].forEach(obj.logValues);
