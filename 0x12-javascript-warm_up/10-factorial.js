#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg, 10);

function factorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

console.log(factorial(num));
