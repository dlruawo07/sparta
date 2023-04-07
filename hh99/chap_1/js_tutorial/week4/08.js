var obj1 = {
  name: "obj1",
  func: function () {
    console.log(this.name);
  },
};

var obj3 = { name: "obj3" };
setTimeout(obj1.func.bind(obj3), 1000);
