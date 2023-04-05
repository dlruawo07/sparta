var func = function (x) {
  console.log(this, x);
};

func(1);

var obj = { method: func };

obj.method(2);

var obj = {
  methodA: function () {
    console.log(this);
  },
  inner: {
    methodB: function () {
      console.log(this);
    },
  },
};

obj.methodA();
obj["methodA"]();

obj.inner.methodB();
obj.inner["methodB"]();
obj["inner"].methodB();
obj["inner"]["methodB"]();
