#!/usr/bin/node

exports.esrever = function (list) {
  const ret = [];
  while (list.length) {
    ret.push(list.pop());
  }
  return ret;
};
