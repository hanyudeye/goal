// ==UserScript==
// @name         B站仅保留搜索框
// @namespace    http://tampermonkey.net/
// @version      2023-12-20
// @description  try to take over the world!
// @author       You
// @match        https://www.bilibili.com/
// @match        https://www.bilibili.com/?spm_id_from=*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=bilibili.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
var allCurrentUsernames = document.getElementsByClassName("bili-feed4-layout");
console.log(allCurrentUsernames[0])
allCurrentUsernames[0].setAttribute("style","display:none;");



})();