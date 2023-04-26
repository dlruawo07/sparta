// User 부모 클래스
class User {
  // 부모 클래스 생성자
  constructor(name, age, tech) {
    this.name = name;
    this.age = age;
    this.tech = tech;
  }
  // 부모 클래스 getTech 메서드
  getTech() {
    return this.tech;
  }
}

// Employee 자식 클래스
class Employee extends User {
  // 자식 클래스 생성자
  constructor(name, age, tech, year) {
    super(name, age, tech);
    this.year = year;
  }
}

const employee = new Employee("이용우", "28", "Node.js", 2);
console.log(employee.name); // 이용우
console.log(employee.age); // 28
console.log(employee.year);
console.log(employee.getTech()); // 부모 클래스의 getTech 메서드 호출: Node.js
