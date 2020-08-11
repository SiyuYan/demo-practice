// you can write to stdout for debugging purposes, e.g. // console.log('this is a debug message');  
function solution(S) {
    const SENTENCE_PATTERN = /^[A-Za-z.?!\s]+$/;
    const SPLITTER_PATTERN = /[.?!]+/;
    const SPACE = ' ';
    if (S.length < 1 || S.length > 100) {
        throw new Error("the length of S is within the range [1..100]")
    }
    // check the input match regex pattern
    if (!SENTENCE_PATTERN.test(S)) {
        throw new Error("String S consist only of letters (a-z, A-Z), " +
            "spaces, dots(.), question marks(? and exclamation marks(i)")
    }
    // split input into sentences
    return S.split(SPLITTER_PATTERN)
    // map sentence to sentence length
        .map((sentence) => sentence
            .split(SPACE)
            .filter((word) => word !==SPACE.trim()).length)
        // find the maximize length
        .reduce((pre, next) => Math.max(pre, next));
}

// const res = solution("we solution coders. Given us a try?");
// const res = solution("Forget. CVs..save time . x x");
const res = solution("Forget. CVs..save time .   x x");
console.log(res);