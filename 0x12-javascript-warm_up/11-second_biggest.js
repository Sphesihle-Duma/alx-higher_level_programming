#!/usr/bin/node
const array = process.argv;
if (array.length === 2 || array.length === 3) {
  console.log(0);
} else {
  let max = parseInt(array[2]);
  let indexOfMax = 2;
  for (let i = 3; i < array.length; i++) {
    const temp = parseInt(array[i]);
    if (max < temp) {
      max = temp;
      indexOfMax = i;
    }
  }
  let secondMax = parseInt(array[2]);
  for (let i = 3; i < array.length; i++) {
    if (i === indexOfMax) {
      continue;
    }
    const temp = parseInt(array[i]);
    if (secondMax < temp) {
      secondMax = temp;
    }
  }
  console.log(secondMax);
}
