async function promiseThen() {
  const timerPromise = new Promise((resolve, reject) => {
    // 이곳에 정의된 함수가 executor
    setTimeout(() => {
      console.log("First");
      resolve("Resolve!");
    }, 1000);
  });

  // 이 시점에서 timerPromise는 Fulfilled Promise라고 부를 수 있다.

  timerPromise.then((data) => {
    console.log("Middle");
    console.log(data);
    console.log("Last");
  });

  // Print: First
  // Middle
  // Last
}

async function promiseCatch() {
  const errorPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("First");
      reject("Error!!");
    }, 1000);
  });

  errorPromise
    .then(() => {
      console.log("Middle");
      console.log("Last");
    })
    .catch((error) => {
      console.log("에러 발생!", error);
    });
}

// promiseThen();
// promiseCatch();

// const firstPromise = Promise.resolve("first");
// firstPromise.then(console.log);

const countPromise = Promise.resolve(0);
function increment(value) {
  return value + 1;
}
const resultPromise = countPromise
  .then(increment)
  .then(increment)
  .then(increment);
resultPromise.then(console.log);
