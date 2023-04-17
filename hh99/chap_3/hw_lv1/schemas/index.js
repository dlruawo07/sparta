const mongoose = require("mongoose");

const connect = () => {
  mongoose
    .connect("mongodb://54.180.145.46:27017/hw_lv1")
    .then(() => {
      console.log("Successfully connected to Mongo");
    })
    .catch((err) => console.log(err));
};

mongoose.connection.on("error", (err) => {
  console.error("몽고디비 연결 에러", err);
});

module.exports = connect;
