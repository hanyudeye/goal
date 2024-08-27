let url='http://localhost:3000/api/welcome'

const getFakePerson = async () => {
//   let res = await fetch("https://api.randomuser.me/?nat=US&results=1");
  let res = await fetch(url);
  let { results } = res.json();
  console.log(results);
};

getFakePerson();