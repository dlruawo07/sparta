function solution(numer1, denom1, numer2, denom2) {
  let head = numer1 * denom2 + numer2 * denom1;
  let foot = denom1 * denom2;
  let answer = [head, foot];
  let GCD = [];
  for (let i = 2; i < Math.min(head, foot); i++) {
    if (head % i === 0 && foot % i === 0) {
      GCD.push(i);
    }
  }
  let realGCD = GCD.length > 0 ? Math.max.apply(null, GCD) : 1;
  answer = answer.map((a) => a / realGCD);
  if (answer[1] % answer[0] === 0) {
    answer[1] /= answer[0];
    answer[0] /= answer[0];
  }
  if (answer[1] === answer[0]) return [answer[0]];
  return answer;
}

console.log(solution(3, 6, 3, 6));
