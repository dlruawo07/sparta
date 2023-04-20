async function main() {
  function first() {
    console.log("set timeout이 실행되었습니다.");
  }
  console.log("코드가 실행되었습니다.");
  // 1초 뒤에 first 호출
  setTimeout(first, 1000);
  console.log("코드가 종료되었습니다.");
}

main();
