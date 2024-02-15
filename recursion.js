function product(nums) {
  return nums.reduce((acc, curr) => acc * curr, 1);
}

function longest(words) {
  return Math.max(...words.map(word => word.length));
}

function everyOther(str) {
  let result = '';
  for (let i = 0; i < str.length; i += 2) {
    result += str[i];
  }
  return result;
}

function isPalindrome(str) {
  return str === str.split('').reverse().join('');
}

function findIndex(arr, val) {
  return arr.indexOf(val);
}

function revString(str) {
  return str.split('').reverse().join('');
}

function gatherStrings(obj) {
  let strings = [];
  for (let key in obj) {
    if (typeof obj[key] === 'string') {
      strings.push(obj[key]);
    } else if (typeof obj[key] === 'object') {
      strings = strings.concat(gatherStrings(obj[key]));
    }
  }
  return strings;
}

function binarySearch(arr, val) {
  let low = 0, high = arr.length - 1;
  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    if (arr[mid] < val) {
      low = mid + 1;
    } else if (arr[mid] > val) {
      high = mid - 1;
    } else {
      return mid;
    }
  }
  return -1;
}

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};
