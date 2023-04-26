const express = require("express");
const router = express.Router();

const Goods = require("../schemas/goods");
const Cart = require("../schemas/cart");

const authMiddleware = require("../middlewares/auth-middleware");

router.get("/goods/cart", authMiddleware, async (req, res) => {
  const { userId } = res.locals.user;
  const carts = await Cart.find({ userId });

  const goodsIds = carts.map((cart) => {
    return cart.goodsId;
  });

  const goods = await Goods.find({ goodsId: goodsIds });

  const results = carts.map((cart) => {
    return {
      // userId: userId,
      quantity: cart.quantity,
      goods: goods.find((item) => item.goodsId === cart.goodsId),
    };
  });

  res.json({
    carts: results,
  });
});

router.get("/goods", async (req, res) => {
  const { category } = req.query;
  const goods = await Goods.find(category ? { category } : {})
    .sort("-date")
    .exec();

  const results = goods.map((good) => {
    return {
      goodsId: good.goodsId,
      name: good.name,
      price: good.price,
      thumbnailUrl: good.thumbnailUrl,
      category: good.category,
    };
  });
  res.status(200).json({ goods: results });
});

router.get("/goods/:goodsId", async (req, res) => {
  const { goodsId } = req.params;
  const goods = await Goods.findOne({ goodsId }).sort("-date").exec();

  const result = {
    goodsId: goods.goodsId,
    name: goods.name,
    price: goods.price,
    thumbnailUrl: goods.thumbnailUrl,
    category: goods.category,
  };
  res.status(200).json({ goods: result });
});

// 장바구니 등록 API
router.post("/goods/:goodsId/cart", authMiddleware, async (req, res) => {
  const { userId } = res.locals.user;
  const { goodsId } = req.params;
  const { quantity } = req.body;

  const existsCarts = await Cart.find({ userId, goodsId });
  if (existsCarts.length) {
    return res.status(400).json({
      success: false,
      errorMessage: "이미 장바구니에 해당하는 상품이 존재합니다.",
    });
  }

  await Cart.create({ userId, goodsId, quantity });

  res.json({ result: "success" });
});

// 장바구니 수정 API
router.put("/goods/:goodsId/cart", authMiddleware, async (req, res) => {
  const { userId } = res.locals.user;
  const { goodsId } = req.params;
  const { quantity } = req.body;

  const existsCarts = await Cart.find({ userId, goodsId });
  if (existsCarts.length) {
    await Cart.updateOne(
      { userId, goodsId: goodsId },
      { $set: { quantity: quantity } }
    );
  }
  res.status(200).json({ success: true });
});

// 장바구니 삭제 API
router.delete("/goods/:goodsId/cart", authMiddleware, async (req, res) => {
  const { userId } = res.locals.user;
  const { goodsId } = req.params;

  const existsCarts = await Cart.find({ userId, goodsId });
  if (existsCarts.length) {
    await Cart.deleteOne({ userId, goodsId });
  }

  res.json({ result: "success" });
});

router.post("/goods", async (req, res) => {
  const { goodsId, name, thumbnailUrl, category, price } = req.body;

  const goods = await Goods.find({ goodsId });

  if (goods.length) {
    return res.status(400).json({
      success: false,
      errorMessage: "이미 존재하는 GoodsId입니다.",
    });
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

module.exports = router;
