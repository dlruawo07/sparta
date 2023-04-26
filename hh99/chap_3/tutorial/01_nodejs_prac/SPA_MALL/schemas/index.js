const mongoose = require("mongoose");

const connect = () => {
  mongoose
    .set("strictQuery", true)
    .connect("mongodb://localhost:27017/spa_mall")
    .then(() => console.log("Successfully connected to MongoDB"))
    .catch((err) => console.log(err));
};

mongoose.connection.on("error", (err) => {
  console.error("Failed to connect to MongoDB", err);
});

module.exports = connect;
