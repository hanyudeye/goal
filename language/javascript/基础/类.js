class Range {
    // 构建函数
    constructor(from, to) {
        this.from = from;
        this.to = to;
    }

    // 是否包含在范围（Range）里面，需要数字
    includes(x) { return this.from <= x && x <= this.to; }

    // 生成器
    *[Symbol.iterator]() {
        for (let x = Math.ceil(this.from); x <= this.to; x++)
            yield x;
    }

    //返回字符串表示
    toString(){return `(${this.from}...${this.to})`};
}


let r=new Range(1,5);
console.log(r.includes(3));
console.log(r.toString());
// 通过迭代器转化为数组
console.log([...r]);