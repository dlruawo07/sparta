const express = require("express");

const router = express.Router();

const User = require("../schemas/user");

const authMiddleware = require("../middlewares/auth-middleware");

router.post("/users", async (req, res) => {
  const { nickname, email, password, confirmPassword } = req.body;

  if (password !== confirmPassword) {
    res
      .status(400)
      .json({ errorMessage: "비밀번호와 비밀번호 확인이 일치하지 않습니다." });
    return;
  }

  const userExists = await User.findOne({ $or: [{ nickname }, { email }] });
  if (userExists) {
    res
      .status(400)
      .json({ errorMessage: "이미 사용 중인 닉네임 또는 이메일입니다." });
    return;
  }

  const user = new User({ nickname, email, password });
  await user.save();

  return res.status(201).json({ errorMessage: "회원가입이 완료되었습니다." });
});

router.get("/users/me", authMiddleware, async (req, res) => {
  const { email, nickname } = res.locals.user;

  res.status(200).json({ user: { email, nickname } });
});

module.exports = router;
