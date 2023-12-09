// ==UserScript==
// @name         github some page hide
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  隐藏 github 网站的 右边的 about 项目  
// @author       aming
// @match        https://github.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=greasyfork.org
// @require      https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js
// @grant        unsafeWindow
// ==/UserScript==

(function () {
    'use strict';

    if (typeof jQuery != 'undefined') {
        alert("已经加载")
    } else {

        alert("没有加载")
    }
    $('.Layout-sidebar').hide();
    // Your code here...
})();