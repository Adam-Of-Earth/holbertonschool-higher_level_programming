#!/usr/bin/node
const Dict = require('./101-data').dict;
const NewDict = {};
const Val = Object.values(Dict);
const SetVal = [...new Set(Val)];
for (let i = 0; i < SetVal.length; i++) {
  NewDict[SetVal[i]] = [];
}
for (const key in Dict) {
  NewDict[Dict[key]].push(key);
}
console.log(NewDict);
