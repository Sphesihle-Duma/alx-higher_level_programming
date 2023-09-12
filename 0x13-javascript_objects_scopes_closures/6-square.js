#!/usr/bin/node
const ParentSquare = require('./5-square');
class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let row = 1; row <= this.height; row++) {
      let temp = '';
      for (let col = 1; col <= this.width; col++) {
        temp += c;
      }
      console.log(temp);
    }
  }
}
module.exports = Square;
