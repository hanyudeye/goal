var Arr=(arr,index)=>{
    let fa=[];

    arr.map(item=>fa.push(item[index]));
    return fa;
}

console.log(Arr([[1,2,4],[2,5,6]],2));