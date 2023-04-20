function setTimeoutFunc(time) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(time + "ms가 지났습니다.");
      resolve();
    }, time);
  });
}

async function main() {
  console.log("시작되었습니다");
  await setTimeoutFunc(1000);
  console.log("종료되었습니다");
}

main();
