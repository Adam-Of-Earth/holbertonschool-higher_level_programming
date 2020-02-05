#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
}
const arg = [];
for (let i = 0; i < x; i++) {
  arg.push('X');
}
for (let i = 0; i < x; i++) {
  console.log(arg.join(''));
}
