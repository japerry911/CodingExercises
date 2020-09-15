/*
---Replace Elements with Greatest Element on Right Side---
Given an array arr, replace every element in that array with 
the greatest element among the elements to its right, and replace 
the last element with -1.

After doing so, return the array.
*/

const replaceElements = (arr) => {
  if (arr.length === 1) {
    return [-1];
  }

  const returnArray = [];

  for (let i = 0; i < arr.length; i++) {
    if (i === arr.length - 1) {
      returnArray.push(-1);
      return returnArray;
    }

    const subArray = arr.slice(i + 1);
    returnArray.push(
      subArray.reduce(
        (accumulator, element) =>
          element > accumulator ? element : accumulator,
        0
      )
    );
  }
};

module.exports = replaceElements;
