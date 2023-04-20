class Person {
  // 3
  constructor(name, age, gender) {
    // this: 이 클래스를 통해 만들어질 객체
    // _name/_age/_gender: 객체의 key
    // name/age/gender: 객체 생성 시 할당받는 값(value)
    this._name = name;
    this._age = age;
    this._gender = gender;
  }
}

// 4                       // 2
const person1 = new Person("david", 30, "M");
const person2 = new Person("mary", 20, "F");
console.log(person1._name);

const person3 = { name: "david", age: 30, gender: "M" };
const person4 = { name: "mary", age: 20, gender: "F" };

console.log(person1, person2);
console.log(person3, person4);
