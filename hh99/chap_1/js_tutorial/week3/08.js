// call
var func = function (a, b, c) {
  console.log(this, a, b, c);
};

// no binding
func(1, 2, 3);

// 명시적 binding
func.call({ x: 1 }, 4, 5, 6);

// apply
var func = function (a, b, c) {
  console.log(this, a, b, c);
};

// no binding
func(1, 2, 3);

// 명시적 binding
func.apply({ x: 1 }, [4, 5, 6]);
