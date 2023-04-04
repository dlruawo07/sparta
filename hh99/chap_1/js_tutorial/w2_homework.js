function solution(strings, n) {
  let result = strings;

  for (let i = 0; i < result.length; i++) {
    result[i] = result[i][n] + result[i];
  }
  result.sort();
  for (let i = 0; i < result.length; i++) {
    result[i] = result[i].substr(1);
  }

  return result;
}
