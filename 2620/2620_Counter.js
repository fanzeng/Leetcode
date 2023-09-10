/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let m = n;
    return function() {
        m += 1;
        return m - 1;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
