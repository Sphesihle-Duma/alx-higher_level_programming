#!/usr/bin/node
function add (a, b) {
  let sum = 0;
  if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
  } else {
    sum = parseInt(a) + parseInt(b);
    console.log(sum);
  }
}
const array = process.argv;
add(array[2], array[3]);
