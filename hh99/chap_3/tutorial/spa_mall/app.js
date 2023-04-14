const express = require("express");
const app = express();
const port = 3000;
const goodsRouter = require("./routes/goods.js");

// req.body를 사용하기 위함 (bodyParser를 쓰기 위한 문법)
// app.use(express.json());
app.use("/api", [goodsRouter]);

app.listen(port, () => {
  console.log(port, "포트로 서버가 열렸어요!");
});
