
// GET http://localhost:3000/api/user HTTP/1.1
let url='http://localhost:3000/api/user'
// console.log(fetch("https://api.randomuser.me/?nat=US&results=1"));

console.log(fetch(url));

fetch(url)
  .then(res => res.json())
  .then(json => json.results)
  .then(console.log)
  .catch(console.error);