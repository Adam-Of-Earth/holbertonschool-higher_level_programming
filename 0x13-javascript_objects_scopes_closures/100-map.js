#!/usr/bin/node
const list = require('./100-data').list;
const map = list.map(function (currentValue, index) { return currentValue * index; });
console.log(list);
console.log(map);
