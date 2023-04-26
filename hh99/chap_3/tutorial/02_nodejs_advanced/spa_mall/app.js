const express = require("express"); // express 모듈 불러오기
const { Server } = require("http"); // http 모듈 불러오기
const socketIo = require("socket.io"); // socket 모듈 불러오기

const cookieParser = require("cookie-parser");
const goodsRouter = require("./routes/goods.js");
const usersRouter = require("./routes/users.js");
const authRouter = require("./routes/auth.js");
const connect = require("./schemas");

const app = express();
const http = Server(app); // express를 http로 감싸주기
const io = socketIo(http); // socket.io를 만들고 http를 할당해주기

const port = 3000;

connect(); // mongoose를 연결합니다.

// 소켓 사용자가 접속했을 때, 해당하는 콜백 함수가 실행된다
io.on("connection", (sock) => {
  console.log("새로운 소켓이 연결되었습니다.");

  // 클라이언트가 상품을 구매했을 때(BUY 소켓 이벤트) 실행된다
  sock.on("BUY", (data) => {
    console.log("구매한 정보입니다.");
    console.log(data);

    // 구매한 정보를 바탕으로 BUY_GOODS 메시지를 전달해야한다
    const emitData = {
      nickname: data.nickname,
      goodsId: data.goodsId,
      goodsName: data.goodsName,
      date: new Date().toISOString(),
    };
    // sock.emit을 쓰면 하나의 소켓에만 보내주는 것이기 때문에
    // io를 사용해서 소켓에 접속한 모든 사용자에게 보내준다
    io.emit("BUY_GOODS", emitData);
  });

  // 현재 접속한 소켓 사용자가 종료했을 때 실행된다
  sock.on("disconnect", () => {
    console.log(`${sock.id}에 해당하는 사용자가 연결을 종료했습니다.`);
  });
});

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static("assets"));
app.use("/api", [goodsRouter, usersRouter, authRouter]);

app.get("/", (req, res) => {
  res.send("Hello World!");
});

http.listen(port, () => {
  console.log(port, "포트로 서버가 열렸어요!");
});
