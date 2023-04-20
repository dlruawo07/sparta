const express = require("express");
const app = express();

const cookieParser = require("cookie-parser");
app.use(cookieParser());

app.get("/set-cookie", (req, res) => {
  let expires = new Date();
  expires.setMinutes(expires.getMinutes() + 60); // 만료 시간을 60분으로 설정합니다.

  res.cookie("name", "sparta", {
    expires: expires,
  });
  return res.status(200).end();
});

app.get("/get-cookie", (req, res) => {
  const cookies = req.cookies;
  console.log(cookies);
  return res.status(200).json({ cookies });
});

let session = {};
app.get("/set-session", (req, res) => {
  const name = "sparta";
  const uniqueInt = Date.now();
  session[uniqueInt] = name;

  res.cookie("sessionKey", uniqueInt);
  return res.status(200).end();
});

app.get("/get-session", (req, res) => {
  const { sessionKey } = req.cookies;

  const sessionItem = session[sessionKey];
  console.log(sessionItem);

  return res.status(200).json({ sessionItem });
});

app.listen(5002, () => {
  console.log("Server listening on 5002");
});
