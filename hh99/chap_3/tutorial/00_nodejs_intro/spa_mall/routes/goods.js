const express = require("express");
const router = express.Router();

const Cart = require("../schemas/cart.js");
router.post("/goods/:goodsId/cart", async (req, res) => {
  const { goodsId } = req.params;
  const { quantity } = req.body;

  const existsInCart = await Cart.find({ goodsId });
  if (existsInCart.length) {
    return res.status(400).json({
      success: false,
      message: "카트에 상품이 존재합니다.",
    });
  }

  await Cart.create({ goodsId, quantity });
  res.json({ result: "success" });
});

router.put("/goods/:goodsId/cart", async (req, res) => {
  const { goodsId } = req.params;
  const { quantity } = req.body;

  const existsInCart = await Cart.find({ goodsId });
  if (existsInCart.length) {
    await Cart.updateOne(
      // goodsId에 해당하는 값이 있을 때
      { goodsId: goodsId },
      // quantity를 quantity로 바꿔라
      { $set: { quantity: quantity } }
    );
  }
  res.status(200).json({ success: true });
});

router.delete("/goods/:goodsId/cart", async (req, res) => {
  const { goodsId } = req.params;

  const existsInCart = await Cart.find({ goodsId });
  if (existsInCart.length) {
    await Cart.deleteOne({ goodsId });
  }
  res.status(200).json({ success: true });
});

const Goods = require("../schemas/goods");
const cart = require("../schemas/cart");
router.post("/goods/", async (req, res) => {
  const { goodsId, name, thumbnailUrl, category, price } = req.body;

  const goods = await Goods.find({ goodsId });
  console.log(goods);
  if (goods.length) {
    return res
      .status(400)
      .json({ success: false, errorMessage: "이미 있는 데이터입니다." });
  }

  const createdGoods = await Goods.create({
    goodsId,
    name,
    thumbnailUrl,
    category,
    price,
  });

  res.json({ goods: createdGoods });
});

router.get("/goods", async (req, res) => {
  const goods = await Goods.find({});
  res.status(200).json({ goods });
});

router.get("/goods/:goodsId", async (req, res) => {
  const goods = await Goods.find({});
  const { goodsId } = req.params;

  const [result] = goods.filter((good) => good.goodsId === Number(goodsId));
  res.status(200).json({ detail: result });
});

module.exports = router;
