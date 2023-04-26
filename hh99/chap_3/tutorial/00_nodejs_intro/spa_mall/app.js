const express = require("express");
const app = express();
const port = 3000;

const goodsRouter = require("./routes/goods");
const cartsRouter = require("./routes/carts.js");
const connect = require("./schemas");

connect();
// post, put 전달된 body 데이터를 req.body로 사용할 수 있도록 만드는 bodyparser
app.use(express.json());

app.use((req, res, next) => {
  console.log("Request URL:", req.originalUrl, " - ", new Date());
  next();
});

// API가 사용되기 위한 라우터 등록
app.use("/api", [goodsRouter, cartsRouter]);

app.listen(port, () => {
  console.log(port, "포트로 서버가 열렸어요!");
});
