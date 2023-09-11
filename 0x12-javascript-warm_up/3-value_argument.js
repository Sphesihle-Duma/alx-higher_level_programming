#!/usr/bin/node
const array = process.argv;
if (array.length === 2) {
  console.log('No argument');
} else {
  console.log(array[2]);
}
