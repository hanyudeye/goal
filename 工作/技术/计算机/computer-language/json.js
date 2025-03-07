let aman = {
    "name": "张三",
    "age": 18,
    "gender": "male",
    "loves": ["apple", "banana", "orange"]
};

let amanString = JSON.stringify(aman);

console.log(amanString);

let amanObj = JSON.parse(amanString);

console.log(amanObj);

