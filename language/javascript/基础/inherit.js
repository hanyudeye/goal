// inherit 继承
// inherit() returns a newly created object that inherits 
// properties from the prototype object p. 

function inherit(p) {
    if (p == null) throw TypeError(); //p must be a non-null object
    if (Object.create)
        return Object.create(p); //返回原型p 的对象
    var t=typeof p; // 获取p 的类型
    if(t !=="object" && t!=="function") throw TypeError();
    function f(){};
    f.prototype=p;
    return new f();  // 使用 f() 创建 an  p 的继承对象
}

