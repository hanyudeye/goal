import * as cheerio from 'cheerio';

const $ = cheerio.load('<h2 class="title">Hello world</h2>');

let text=$('h2.title').text();
console.log(text);