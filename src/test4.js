function braces(values) {
    let results = [];
    for (let i in values)
        results.push(check(values[i]));
    return results;
}

function check(str) {
    let arr = str.split('');
    let stack = new Stack();
    let allowed_chars = '({[]})';
    let index = -1;
    for (let j = 0; j < arr.length; j++) {
        let item = arr[j];
        index = allowed_chars.indexOf(item);
        if (index < 3) {
            stack.push(item)
        } else {
            let target = stack.pop();
            if (!target) {
                return 'NO';
            }
            if (target !== allowed_chars.charAt(allowed_chars.length - 1 - index)) {
                return 'NO';
            }
        }
    }
    if (stack.size()) {
        return 'NO'
    }
    return 'YES';
}

function Stack() {
    this.top = 0;
    this.dataStore = [];
    this.push = push;
    this.pop = pop;
    this.size = size;
}

function push(element) {
    this.dataStore[this.top++] = element;
}

function pop() {
    return this.dataStore[--this.top];
}

function size() {
    return this.top;
}