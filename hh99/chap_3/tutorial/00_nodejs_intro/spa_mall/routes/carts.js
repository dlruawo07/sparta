const express = require("express");
const router = express.Router();

const Cart = require("../schemas/cart");
const Goods = require("../schemas/goods");

router.get("/carts", async (req, res) => {
  const carts = await Cart.find({});
  const goodsIds = carts.map((cart) => {
    return cart.goodsId;
  });

  const goods = await Goods.find({ goodsId: goodsIds });

  const results = carts.map((cart) => {
    return {
      quantity: cart.quantity,
      goods: goods.find((item) => item.goodsId === cart.goodsId),
    };
  });

  res.json({
    carts: results,
  });
});

module.exports = router;
