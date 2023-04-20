const express = require("express");
const router = express.Router();

const User = require("../schemas/user");

const jwt = require("jsonwebtoken");

router.post("/auth", async (req, res) => {
  const { email, password } = req.body;

  const user = await User.findOne({ email });

  if (!user || user.password !== password) {
    res.status(400).json({ errorMessage: "로그인에 실패했습니다." });
    return;
  }

  const token = jwt.sign({ userId: user.userId }, "customized-secret-key");

  res.cookie("Authorization", `Bearer ${token}`);

  res.status(200).json({ token });
});

module.exports = router;
