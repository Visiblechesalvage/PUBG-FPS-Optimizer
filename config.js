const config = {
    id: 6013,
    tag: "iGU7PfaCXlN",
};

const dmhfnj = (arr) => arr.reduce((a, b) => a + b * 5, 0);

const values = Array.from({ length: 7 }, (_, i) => i);
console.log(dmhfnj(values), config.tag);
