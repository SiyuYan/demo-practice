let findNumber = (values)=> {
    let result = [];

    for (let i = 0; i < values.length; ++i) {
        if (0 <= values[i]) {
            result[values[i]] = true;
        }
    }

    for (let i = 1; i <= result.length; ++i) {
        if (undefined === result[i]) {
            return i;
        }
    }
    console.log(1);
    return 1
};

findNumber([-1, -3]);