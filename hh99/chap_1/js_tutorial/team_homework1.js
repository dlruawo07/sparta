const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function getThreeDigitRandomNumber() {
  let ret = new Set();
  while (ret.size !== 3) {
    ret.add(Math.floor(Math.random() * 10));
  }
  return Array.from(ret).join("");
}

function checkNumber(answer, guess) {
  if (isNaN(guess) || guess.length !== 3) return "3자리 숫자를 입력하세요";

  if ([...new Set(guess.split(""))].length < 3)
    return "서로 다른 숫자 3개를 입력하세요";

  if (answer === guess) return "3S";

  let countS = 0;
  let countB = 0;

  for (let i = 0; i < guess.length; i++) {
    if (answer[i] === guess[i]) countS++;
    else if (answer.indexOf(guess[i]) !== -1) countB++;
  }

  return countB === 3 ? "3B" : `${countB}B${countS}S`;
}

let trial = 1;
let answer = getThreeDigitRandomNumber();
// console.log(answer);

console.log("컴퓨터가 숫자를 생성하였습니다. 답을 맞춰보세요!");

var recursiveAsyncReadLine = function () {
  rl.question(`${trial++}번째 시도 : `, (guess) => {
    result = checkNumber(answer, guess);
    console.log(result);
    if (guess === answer) {
      console.log(`${trial - 1}번만에 맞히셨습니다.\n게임을 종료합니다.`);
      return rl.close();
    }
    recursiveAsyncReadLine();
  });
};

recursiveAsyncReadLine();
