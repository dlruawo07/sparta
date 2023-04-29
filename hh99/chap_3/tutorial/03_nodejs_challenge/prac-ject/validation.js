module.exports = {
  isEmail: (value) => {
    // value가 이메일 형식에 맞으면 true, 형식에 맞지 않으면 false를 return 하도록 구현해보세요
    // '입력한 이메일 주소에는 "@" 문자가 1개만 있어야 이메일 형식이다.'
    // "입력한 이메일 주소에 공백(스페이스)이 존재하면 이메일 형식이 아니다."
    // "입력한 이메일 주소 맨 앞에 하이픈(-)이 있으면 이메일 형식이 아니다."
    // "입력한 이메일 주소중, 로컬 파트(골뱅이 기준 앞부분)에는 영문 대소문자와 숫자, 특수문자는 덧셈기호(+), 하이픈(-), 언더바(_) 3개 외에 다른 값이 존재하면 이메일 형식이 아니다."
    // "입력한 이메일 주소중, 도메인(골뱅이 기준 뒷부분)에는 영문 대소문자와 숫자, 하이픈(-) 외에 다른 값이 존재하면 이메일 형식이 아니다."

    const email = value || "";
    const [localPart, domain, ...etc] = email.split("@");

    if (!localPart || !domain || etc.length !== 0) {
      return false;
    } else if (email.includes(" ")) {
      return false;
    } else if (email[0] === "-") {
      return false;
    } else if (!/^[a-z0-9+_-]+$/gi.test(localPart)) {
      return false;
    } else if (!/^[a-z0-9.-]+$/gi.test(domain)) {
      return false;
    }

    return true;
  },
};
