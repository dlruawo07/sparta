const mongoose = require("mongoose");

mongoose
  .connect("mongodb://localhost:27017/todo-demo", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then((value) => console.log("Successfully conneceted to MongoDB"))
  .catch((reason) => console.log("Failed to connect to MongoDB"));

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));

module.exports = db;
