var obj1 = {
  name: "obj1",
  func: function () {
    var self = this;
    return function () {
      console.log(self.name);
    };
  },
};

var callback = obj1.func();
setTimeout(callback, 1000);

var obj2 = { name: "obj2" };
var callback2 = obj1.func.call(obj2);
setTimeout(callback2, 2000);
