#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 1; row <= this.height; row++) {
      let temp = '';
      for (let col = 1; col <= this.width; col++) {
        temp += 'X';
      }
      console.log(temp);
    }
  }
}
module.exports = Rectangle;
