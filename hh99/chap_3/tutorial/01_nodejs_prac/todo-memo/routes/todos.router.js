const express = require("express");
const router = express.Router();

const Todo = require("../models/todo");

router.get("/", (req, res) => {
  res.send("Hi");
});

router.post("/todos", async (req, res) => {
  const { value } = req.body;
  const latestTodo = await Todo.findOne().sort("-order").exec();

  const order = latestTodo ? latestTodo.order + 1 : 1;

  const todo = new Todo({ value, order });
  await todo.save();

  res.send({ todo });
});

router.get("/todos", async (req, res) => {
  const todos = await Todo.find().sort("-order").exec();
  res.send({ todos });
});

router.patch("/todos/:todoId", async (req, res) => {
  const { todoId } = req.params;
  const { order } = req.body;

  const currentTodo = await Todo.findById(todoId);

  if (!currentTodo) {
    return res
      .status(400)
      .json({ errorMessage: "존재하지 않는 할 일 입니다." });
  }

  if (order) {
    const targetTodo = await Todo.findOne({ order }).exec();
    if (targetTodo) {
      targetTodo.order = currentTodo.order;
      await targetTodo.save();
    }
    currentTodo.order = order;
    await currentTodo.save();
  }
  res.send();
});

router.delete("/todos/:todoId", async (req, res) => {
  const { todoId } = req.params;
  const todo = await Todo.findById(todoId);

  await Todo.deleteOne({ _id: todoId });
  res.send("deleted");
});

module.exports = router;

// http://localhost:8080/api/todos/643f49cfddf63701dc96a3e9
