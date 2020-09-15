const replaceElements = require("./index");

test("replaceElements is a function", () => {
  expect(typeof replaceElements).toEqual("function");
});

test("replaceElements test 1 - [17, 18, 5, 4, 6, 1]", () => {
  expect(replaceElements([17, 18, 5, 4, 6, 1])).toEqual([18, 6, 6, 6, 1, -1]);
});
