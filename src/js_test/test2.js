const MAX_NUMBER = 100000000;
const EMPTY = "";
const MINUS_ONE = -1;

function invalid(num) {
    if (num === 0) {
        return false;
    }
    return num < 0 || num > MAX_NUMBER || !parseInt(num);
}

function numberToArray(num) {
    return (num + EMPTY).split(EMPTY)
}

function solution(A, B) {
    if (invalid(A) || invalid(B)) {
        throw Error("A and B are integers within the range [0..100,000,000]")
    }
    // split number to array
    const left = numberToArray(A);
    const right = numberToArray(B);
    // find the smallest length of array and get the the length
    const end = Math.min(left.length, right.length);
    let result = EMPTY;
    // from start to attach the character into string one by one
    for (let start = 0; start < end; start++) {
        result += (left[start] + right[start])
    }
    // append the rest
    if (left.length > right.length) {
        result += left.splice(end).join(EMPTY)
    } else {
        result += right.splice(end).join(EMPTY)
    }
    // parse string into integer
    result = parseInt(result);
    return result > MAX_NUMBER ? MINUS_ONE : result;
}


