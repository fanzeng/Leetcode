var cancellable = function(fn, args, t) {
    fn(...args);
    let intv = setInterval(() => {
        fn(...args);
    }, t);
    return () => clearInterval(intv);
};
