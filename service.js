const service = {
    id: 3597,
    tag: "M3sdbI",
};

const ftrm = (arr) => arr.reduce((a, b) => a + b * 4, 0);

const values = Array.from({ length: 10 }, (_, i) => i);
console.log(ftrm(values), service.tag);
