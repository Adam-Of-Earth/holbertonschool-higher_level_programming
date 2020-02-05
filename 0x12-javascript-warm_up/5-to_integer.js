#!/usr/bin/node
const arg = process.argv;
const x = parseInt(arg[2]);
if (isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + x);
}
