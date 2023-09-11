#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 1; row <= size; row++) {
    let temp = '';
    for (let col = 1; col <= size; col++) {
      temp += 'X';
    }
    console.log(temp);
  }
}
