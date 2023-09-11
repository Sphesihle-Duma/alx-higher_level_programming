#!/usr/bin/node
const array = process.argv;
if (array.length === 2) {
  console.log('No arguments');
} else {
  console.log(array[2]);
}
