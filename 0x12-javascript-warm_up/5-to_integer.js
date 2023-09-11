#!/usr/bin/node
const array = process.argv;
const number = parseInt(array[2]);
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
