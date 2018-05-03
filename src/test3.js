function solution(S) {
    const priceDetails = {};
    // convert into price record object
    const priceRecords = S.split("\n")
        .map((record) => computeRecordPrice(record));
    // merge same user's records into object
    priceRecords.forEach((item) => {
        for (const key in item) {
            priceDetails[key] = priceDetails[key] ? priceDetails[key].concat(item[key]) : item[key]
        }
    });

    // calculate the total price
    const totalCost = getTotalPrice(priceDetails);
    const deductionPrice = getDeductionPrice(priceDetails);
    return totalCost - deductionPrice;
}

function getDeductionPrice(priceDetails) {
    // merge the same user records' duration and price
    for (const user in priceDetails) {
        priceDetails[user] = priceDetails[user].reduce((pre, next) => {
            console.log("PRE+NEXT:", pre.duration + next.duration)
            return {
                duration: pre.duration + next.duration,
                price: pre.price + next.price
            }
        })
    }

    // find the largest duration user and return
    let freeUser;
    for (const user in priceDetails) {
        if (!freeUser) {
            freeUser = priceDetails[user];
        } else {
            if (priceDetails[user].duration > freeUser.duration) {
                freeUser = priceDetails[user];
            }
        }
    }
    return freeUser.price;
}

function getTotalPrice(priceDetails) {
    let total = 0;
    for (const key in priceDetails) {
        total += getSingleTotalPrice(priceDetails[key]);
    }
    return total;
}

function getSingleTotalPrice(priceList) {
    if (priceList.length === 1) {
        return priceList[0].price;
    }
    return priceList.reduce((prev, next) => prev.price + next.price)
}

function computeRecordPrice(record) {
    const splits = record.split(",");
    const user = splits[1];
    const duration = getSecondWithEachCall(splits[0]);
    const price = getBillingBySeconds(duration);
    const res = {};
    res[user] = [{duration, price}];
    return res;
}

function getBillingBySeconds(second) {
    if (second < 5 * 60) {
        return second * 3;
    } else {
        return ((Math.floor(second / 60)) + (second % 60 > 0 ? 1 : 0)) * 150;
    }
}

function getSecondWithEachCall(time) {
    let callingTime = time.split(':');
    return callingTime[2] * 1 + callingTime[1] * 60 + callingTime[0] * 60 * 60;
}

solution(`00:01:07,400-234-090
          00:05:01,701-080-080
          00:05:00,400-234-090`);