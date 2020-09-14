const finalPrices = require("./index");

test("finalPrices is a function", () => {
  expect(typeof finalPrices).toEqual("function");
});

test("finalPrices test - [8, 4, 6, 2, 3]", () => {
  expect(finalPrices([8, 4, 6, 2, 3])).toEqual([4, 2, 4, 2, 3]);
});

test("finalPrices test - [1, 2, 3, 4, 5]", () => {
  expect(finalPrices([1, 2, 3, 4, 5])).toEqual([1, 2, 3, 4, 5]);
});

test("finalPrices test - [10, 1, 1, 6]", () => {
  expect(finalPrices([10, 1, 1, 6])).toEqual([9, 0, 1, 6]);
});
