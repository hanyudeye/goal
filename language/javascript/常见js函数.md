基于thinkphp5小功能设计与实现 
https://www.kancloud.cn/zhiqiang/helper/262735


## 常见的js函数
### 短信验证函数
html代码

  <div class="weui_cell">
      <div class="weui_cell_hd"><label class="weui_label">手机验证码</label></div>
      <div class="weui_cell_bd weui_cell_primary">
          <input class="weui_input" type="number" placeholder="" name='phone_code'/>
      </div>
      <p class="bk_important bk_phone_code_send">发送验证码</p>
      <div class="weui_cell_ft">
      </div>
  </div>
</div>
js代码
```html
<script type="text/javascript">
  var enable = true;
  $('.bk_phone_code_send').click(function(event) {
    if(enable == false) {
      return;
    }

    var phone = $('input[name=phone]').val();
    // 手机号不为空
    if(phone == '') {
      $('.bk_toptips').show();
      $('.bk_toptips span').html('请输入手机号');
      setTimeout(function() {$('.bk_toptips').hide();}, 2000);
      return;
    }
    // 手机号格式
    if(phone.length != 11 || phone[0] != '1') {
      $('.bk_toptips').show();
      $('.bk_toptips span').html('手机格式不正确');
      setTimeout(function() {$('.bk_toptips').hide();}, 2000);
      return;
    }

    $(this).removeClass('bk_important');
    $(this).addClass('bk_summary');
    enable = false;
    var num = 60;
    var interval = window.setInterval(function() {
      $('.bk_phone_code_send').html(--num + 's 重新发送');
      if(num == 0) {
        $('.bk_phone_code_send').removeClass('bk_summary');
        $('.bk_phone_code_send').addClass('bk_important');
        enable = true;
        window.clearInterval(interval);
        $('.bk_phone_code_send').html('重新发送');
      }
    }, 1000);

    $.ajax({
      url: '/service/validate_phone/send',
      dataType: 'json',
      cache: false,
      data: {phone: phone},
      success: function(data) {
        if(data == null) {
          $('.bk_toptips').show();
          $('.bk_toptips span').html('服务端错误');
          setTimeout(function() {$('.bk_toptips').hide();}, 2000);
          return;
        }
        if(data.status != 0) {
          $('.bk_toptips').show();
          $('.bk_toptips span').html(data.message);
          setTimeout(function() {$('.bk_toptips').hide();}, 2000);
          return;
        }

        $('.bk_toptips').show();
        $('.bk_toptips span').html('发送成功');
        setTimeout(function() {$('.bk_toptips').hide();}, 2000);
      },
      error: function(xhr, status, error) {
        console.log(xhr);
        console.log(status);
        console.log(error);
      }
    });
  });
</script>
```

### 上下收缩菜单
html代码

	<div class="treebox">
		<ul class="menu">
			<li class="level1">
				<a href="#none"><em class="ico ico1"></em>导航一<i class="down"></i></a>
				<ul class="level2">
					<li><a href="javascript:;">导航选项</a></li>
					<li><a href="javascript:;">导航选项</a></li>
					<li><a href="javascript:;">导航选项</a></li>
					<li><a href="javascript:;">导航选项</a></li>
				</ul>
			</li>



             <li class="level1">
				<a href="#none"><em class="ico ico5"></em>导航一<i></i></a>
				<ul class="level2">
					<li><a href="javascript:;">导航选项</a></li>
					<li><a href="javascript:;">导航选项</a></li>
					<li><a href="javascript:;">导航选项</a></li>
					<li><a href="javascript:;">导航选项</a></li>
				</ul>
			</li>
		</ul>
	</div>
css代码

	<style>
		 .menu li ul.level2{ display: none }
	</style>
js代码

<script src="scripts/jquery1.8.3.min.js" type="text/javascript"></script>
<script src="scripts/easing.js"></script>
<script>
//等待dom元素加载完毕.
	$(function(){
		$(".treebox .level1>a").click(function(){
			$(this).addClass('current')   //给当前元素添加"current"样式
			.find('i').addClass('down')   //小箭头向下样式
			.parent().next().slideDown('slow','easeOutQuad')  //下一个元素显示
			.parent().siblings().children('a').removeClass('current')//父元素的兄弟元素的子元素去除"current"样式
			.find('i').removeClass('down').parent().next().slideUp('slow','easeOutQuad');//隐藏
			 return false; //阻止默认事件
		});
	})
</script>

js下载地址
http://gsgd.co.uk/sandbox/jquery/easing/jquery.easing.1.3.js

### jQuery 树插件zTree

文件准备
<link rel="stylesheet" href="zTreeStyle/zTreeStyle.css" type="text/css">
<script type="text/javascript" src="jquery-1.4.2.js"></script>
<script type="text/javascript" src="jquery.ztree.core-3.x.js"></script>

编写 html 页面（本地数据）
``` html
<script>
var zTreeObj;
// zTree 的参数配置，深入使用请参考 API 文档（setting 配置详解）
var setting = {};
// zTree 的数据属性，深入使用请参考 API 文档（zTreeNode 节点数据详解）
var zNodes = [
   {name:"test1", open:true, children:[
      {name:"test1_1"}, {name:"test1_2"}]},
   {name:"test2", open:true, children:[
      {name:"test2_1"}, {name:"test2_2"}]}
   ];
   
$(document).ready(function(){
   zTreeObj = $.fn.zTree.init($("#treeDemo"), setting, zNodes);
   });
</script>
```
编写 html 页面（服务端数据）
``` js
    $(document).ready(function(){
        /**
         * 加载树形授权菜单
         */
        var _id = $("#group_id").val();
        var tree = $("#tree");
        var zTree;

        // zTree 配置项
        var setting = {
            check: {
                enable: true
            },
            view: {
                dblClickExpand: false,
                showLine: true,
                showIcon: false,
                selectedMulti: false
            },
            data: {
                simpleData: {
                    enable: true,
                    idKey: "id",
                    pIdKey: "pid",
                    rootpid: ""
                },
                key: {
                    name: "title"
                }
            }
        };

        $.ajax({
            url: "/index.php/admin/auth_group/getJson",
            type: "post",
            dataType: "json",
            cache: false,
            data: {
                id: _id
            },
            success: function (data) {
                zTree = $.fn.zTree.init(tree, setting, data);
            }
        });
```
### 页面刷新跳转
页面刷新
 history.go(0) 
 location.reload() 
 location=location 
 location.assign(location) 
 document.execCommand('Refresh') 
 window.navigate(location) 
 location.replace(location) 
 document.URL=location.href
1.页面自动刷新：把如下代码加入区域中

<meta http-equiv="refresh" content="20">
//其中20指每隔20秒刷新一次页面.
2.页面自动跳转：把如下代码加入区域中

<meta http-equiv="refresh" content="20;url=http://www.kancloud.cn/">
返回并刷新页面
 history.go(-1)，或 history.back();
页面跳转
	self.location='http://www.kancloud.cn/'
    
###    jquery导出报表
    <!-- morris -->
    <script src="__PUBLIC__/js/plugins/tableexport/Blob.js"></script>
    <script src="__PUBLIC__/js/plugins/tableexport/FileSaver.js"></script>
    <script src="__PUBLIC__/js/plugins/tableexport/tableExport.js"></script>
        <!-- 导出xls -->
    <script>
    var export_btn  = $("#export-btn");
    if (export_btn) {
            var $exportLink = document.getElementById('export-btn');
            $exportLink.addEventListener('click', function(e){
                e.preventDefault();
                console.log(e.target.getAttribute('data-table'));
                if(e.target.nodeName === "A"){
                    tableExport(e.target.getAttribute('data-table'), '{$title}', e.target.getAttribute('data-type'));
                }
            }, false);
    };
    </script>
  <div class="col-sm-2" id="export-btn">
                         <a data-type="xls" data-table="repayment_table" href="javascript:;" type="button" class="btn btn-danger btn-sm">导出xls</a>
                 </div>
<div class="table-responsive">
                    <table class="table table-striped table-bordered table-hover dataTables-example" id="repayment_table">
                        <thead>
                            <tr>
                                <th></th>
                                <th>编号</th>
                                <th>借款序号</th>
                                <th>借款人</th>
                                <th>还款金额</th>
                                <th>应还款时间</th>
                                <th>实际还款时间</th>
                                <th>是否已还</th>
                                <th>是否逾期</th>
                                <th>逾期费用</th>
                                <th>操作</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                </div>
### js实现定时效果
setTimeout(function () {
                        location.href = info.url;
      }, 1000);
      
###   获取当前经纬度
获取当前经纬度

function showError(error){ 
    switch(error.code) { 
        case error.PERMISSION_DENIED: 
            alert("定位失败,用户拒绝请求地理定位"); 
            break; 
        case error.POSITION_UNAVAILABLE: 
            alert("定位失败,位置信息是不可用"); 
            break; 
        case error.TIMEOUT: 
            alert("定位失败,请求获取用户位置超时"); 
            break; 
        case error.UNKNOWN_ERROR: 
            alert("定位失败,定位系统失效"); 
            break; 
    } 
} 
function showPosition(position){ 
    var lat = position.coords.latitude; //纬度 
    var lag = position.coords.longitude; //经度 
    alert('纬度:'+lat+',经度:'+lag); 
} 
function getLocation(){ 
    if (navigator.geolocation){ 
        navigator.geolocation.getCurrentPosition(showPosition,showError); 
    }else{ 
        alert("浏览器不支持地理定位。"); 
    } 
}     

### JQuery实现图片大小自适应
$("img").each(function(){
	if($(this).width() > $(this).parent().width()) {
		$(this).width("100%");
	}
});

### 网站运行时间
<script src="http://www.jq22.com/jquery/jquery-1.10.2.js"></script>
<script type="text/javascript">
//网站运行时间
function show_date_time(){
    window.setTimeout("show_date_time()", 1000);
    BirthDay=new Date("01/09/2013 00:00:00");//这个日期是可以修改的
    today=new Date();
    timeold=(today.getTime()-BirthDay.getTime());
    sectimeold=timeold/1000
    secondsold=Math.floor(sectimeold);
    msPerDay=24*60*60*1000
    e_daysold=timeold/msPerDay
    daysold=Math.floor(e_daysold);
    e_hrsold=(e_daysold-daysold)*24;
    hrsold=Math.floor(e_hrsold);
    e_minsold=(e_hrsold-hrsold)*60;
    minsold=Math.floor((e_hrsold-hrsold)*60);
    seconds=Math.floor((e_minsold-minsold)*60);
    var siteDate = "已运行"+daysold+"天"+hrsold+"小时"+minsold+"分"+seconds+"秒";
    $("#show_date_time").html(siteDate);
}
show_date_time()
</script>
 <span id="show_date_time"  ></span>
效果图所示

### 百度推送
    //百度推送
    (function () {
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
            bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
            bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
    })();

### js对指定数据进行排序
var arr = [
    {name:'腾讯',age:0},
    {name:'百度',age:18},
    {name:'京东',age:8}
];



降序

var newarr=arr.sort(function(a,b){return b['age']-a['age']})

升序

var newarr=arr.sort(function(a,b){return a['age']-b['age']})

### 常见工具方法
原文 ：https://segmentfault.com/a/1190000022736837

1.邮箱

export const isEmail = (s) => {
    return /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((.[a-zA-Z0-9_-]{2,3}){1,2})$/.test(s)
}
2.手机号码

export const isMobile = (s) => {
    return /^1[0-9]{10}$/.test(s)
}
3.电话号码

export const isPhone = (s) => {
    return /^([0-9]{3,4}-)?[0-9]{7,8}$/.test(s)
}
4.是否url地址

export const isURL = (s) => {
    return /^http[s]?:\/\/.*/.test(s)
}
5.是否字符串

export const isString = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'String'
}
6.是否数字

export const isNumber = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Number'
}
7.是否boolean

export const isBoolean = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Boolean'
}
8.是否函数

export const isFunction = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Function'
}
9.是否为null

export const isNull = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Null'
}
10.是否undefined

export const isUndefined = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Undefined'
}
11.是否对象

export const isObj = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Object'
}
12.是否数组

export const isArray = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Array'
}
13.是否时间

export const isDate = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Date'
}
14.是否正则

export const isRegExp = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'RegExp'
}
15.是否错误对象

export const isError = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Error'
}
16.是否Symbol函数

export const isSymbol = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Symbol'
}
17.是否Promise对象

export const isPromise = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Promise'
}
18.是否Set对象

export const isSet = (o) => {
    return Object.prototype.toString.call(o).slice(8, -1) === 'Set'
}
export const ua = navigator.userAgent.toLowerCase();
19.是否是微信浏览器

export const isWeiXin = () => {
    return ua.match(/microMessenger/i) == 'micromessenger'
}
20.是否是移动端

export const isDeviceMobile = () => {
    return /android|webos|iphone|ipod|balckberry/i.test(ua)
}
21.是否是QQ浏览器

export const isQQBrowser = () => {
    return !!ua.match(/mqqbrowser|qzone|qqbrowser|qbwebviewtype/i)
}
22.是否是爬虫

export const isSpider = () => {
    return /adsbot|googlebot|bingbot|msnbot|yandexbot|baidubot|robot|careerbot|seznambot|bot|baiduspider|jikespider|symantecspider|scannerlwebcrawler|crawler|360spider|sosospider|sogou web sprider|sogou orion spider/.test(ua)
}
23.是否ios

export const isIos = () => {
    var u = navigator.userAgent;
    if (u.indexOf('Android') > -1 || u.indexOf('Linux') > -1) {  //安卓手机
        return false
    } else if (u.indexOf('iPhone') > -1) {//苹果手机
        return true
    } else if (u.indexOf('iPad') > -1) {//iPad
        return false
    } else if (u.indexOf('Windows Phone') > -1) {//winphone手机
        return false
    } else {
        return false
    }
}
24.是否为PC端

export const isPC = () => {
    var userAgentInfo = navigator.userAgent;
    var Agents = ["Android", "iPhone",
        "SymbianOS", "Windows Phone",
        "iPad", "iPod"];
    var flag = true;
    for (var v = 0; v < Agents.length; v++) {
        if (userAgentInfo.indexOf(Agents[v]) > 0) {
            flag = false;
            break;
        }
    }
    return flag;
}
25.去除html标签

export const removeHtmltag = (str) => {
    return str.replace(/<[^>]+>/g, '')
}
26.获取url参数

export const getQueryString = (name) => {
    const reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
    const search = window.location.search.split('?')[1] || '';
    const r = search.match(reg) || [];
    return r[2];
}
27.动态引入js

export const injectScript = (src) => {
    const s = document.createElement('script');
    s.type = 'text/javascript';
    s.async = true;
    s.src = src;
    const t = document.getElementsByTagName('script')[0];
    t.parentNode.insertBefore(s, t);
}
28.根据url地址下载

export const download = (url) => {
    var isChrome = navigator.userAgent.toLowerCase().indexOf('chrome') > -1;
    var isSafari = navigator.userAgent.toLowerCase().indexOf('safari') > -1;
    if (isChrome || isSafari) {
        var link = document.createElement('a');
        link.href = url;
        if (link.download !== undefined) {
            var fileName = url.substring(url.lastIndexOf('/') + 1, url.length);
            link.download = fileName;
        }
        if (document.createEvent) {
            var e = document.createEvent('MouseEvents');
            e.initEvent('click', true, true);
            link.dispatchEvent(e);
            return true;
        }
    }
    if (url.indexOf('?') === -1) {
        url += '?download';
    }
    window.open(url, '_self');
    return true;
}
29.el是否包含某个class

export const hasClass = (el, className) => {
    let reg = new RegExp('(^|\\s)' + className + '(\\s|$)')
    return reg.test(el.className)
}
30.el添加某个class

export const addClass = (el, className) => {
    if (hasClass(el, className)) {
        return
    }
    let newClass = el.className.split(' ')
    newClass.push(className)
    el.className = newClass.join(' ')
}
31.el去除某个class

export const removeClass = (el, className) => {
    if (!hasClass(el, className)) {
        return
    }
    let reg = new RegExp('(^|\\s)' + className + '(\\s|$)', 'g')
    el.className = el.className.replace(reg, ' ')
}
32.获取滚动的坐标

export const getScrollPosition = (el = window) => ({
    x: el.pageXOffset !== undefined ? el.pageXOffset : el.scrollLeft,
    y: el.pageYOffset !== undefined ? el.pageYOffset : el.scrollTop
});
33.滚动到顶部

export const scrollToTop = () => {
    const c = document.documentElement.scrollTop || document.body.scrollTop;
    if (c > 0) {
        window.requestAnimationFrame(scrollToTop);
        window.scrollTo(0, c - c / 8);
    }
}
34.el是否在视口范围内

export const elementIsVisibleInViewport = (el, partiallyVisible = false) => {
    const { top, left, bottom, right } = el.getBoundingClientRect();
    const { innerHeight, innerWidth } = window;
    return partiallyVisible
        ? ((top > 0 && top < innerHeight) || (bottom > 0 && bottom < innerHeight)) &&
        ((left > 0 && left < innerWidth) || (right > 0 && right < innerWidth))
        : top >= 0 && left >= 0 && bottom <= innerHeight && right <= innerWidth;
}
35.洗牌算法随机

export const shuffle = (arr) => {
    var result = [],
        random;
    while (arr.length > 0) {
        random = Math.floor(Math.random() * arr.length);
        result.push(arr[random])
        arr.splice(random, 1)
    }
    return result;
}
36.劫持粘贴板

export const copyTextToClipboard = (value) => {
    var textArea = document.createElement("textarea");
    textArea.style.background = 'transparent';
    textArea.value = value;
    document.body.appendChild(textArea);
    textArea.select();
    try {
        var successful = document.execCommand('copy');
    } catch (err) {
        console.log('Oops, unable to copy');
    }
    document.body.removeChild(textArea);
}
37.判断类型集合

export const checkStr = (str, type) => {
    switch (type) {
        case 'phone':   //手机号码
            return /^1[3|4|5|6|7|8|9][0-9]{9}$/.test(str);
        case 'tel':     //座机
            return /^(0\d{2,3}-\d{7,8})(-\d{1,4})?$/.test(str);
        case 'card':    //身份证
            return /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/.test(str);
        case 'pwd':     //密码以字母开头，长度在6~18之间，只能包含字母、数字和下划线
            return /^[a-zA-Z]\w{5,17}$/.test(str)
        case 'postal':  //邮政编码
            return /[1-9]\d{5}(?!\d)/.test(str);
        case 'QQ':      //QQ号
            return /^[1-9][0-9]{4,9}$/.test(str);
        case 'email':   //邮箱
            return /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/.test(str);
        case 'money':   //金额(小数点2位)
            return /^\d*(?:\.\d{0,2})?$/.test(str);
        case 'URL':     //网址
            return /(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?/.test(str)
        case 'IP':      //IP
            return /((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))/.test(str);
        case 'date':    //日期时间
            return /^(\d{4})\-(\d{2})\-(\d{2}) (\d{2})(?:\:\d{2}|:(\d{2}):(\d{2}))$/.test(str) || /^(\d{4})\-(\d{2})\-(\d{2})$/.test(str)
        case 'number':  //数字
            return /^[0-9]$/.test(str);
        case 'english': //英文
            return /^[a-zA-Z]+$/.test(str);
        case 'chinese': //中文
            return /^[\\u4E00-\\u9FA5]+$/.test(str);
        case 'lower':   //小写
            return /^[a-z]+$/.test(str);
        case 'upper':   //大写
            return /^[A-Z]+$/.test(str);
        case 'HTML':    //HTML标记
            return /<("[^"]*"|'[^']*'|[^'">])*>/.test(str);
        default:
            return true;
    }
}
38.严格的身份证校验

export const isCardID = (sId) => {
    if (!/(^\d{15}$)|(^\d{17}(\d|X|x)$)/.test(sId)) {
        console.log('你输入的身份证长度或格式错误')
        return false
    }
    //身份证城市
    var aCity = { 11: "北京", 12: "天津", 13: "河北", 14: "山西", 15: "内蒙古", 21: "辽宁", 22: "吉林", 23: "黑龙江", 31: "上海", 32: "江苏", 33: "浙江", 34: "安徽", 35: "福建", 36: "江西", 37: "山东", 41: "河南", 42: "湖北", 43: "湖南", 44: "广东", 45: "广西", 46: "海南", 50: "重庆", 51: "四川", 52: "贵州", 53: "云南", 54: "西藏", 61: "陕西", 62: "甘肃", 63: "青海", 64: "宁夏", 65: "新疆", 71: "台湾", 81: "香港", 82: "澳门", 91: "国外" };
    if (!aCity[parseInt(sId.substr(0, 2))]) {
        console.log('你的身份证地区非法')
        return false
    }

    // 出生日期验证
    var sBirthday = (sId.substr(6, 4) + "-" + Number(sId.substr(10, 2)) + "-" + Number(sId.substr(12, 2))).replace(/-/g, "/"),
        d = new Date(sBirthday)
    if (sBirthday != (d.getFullYear() + "/" + (d.getMonth() + 1) + "/" + d.getDate())) {
        console.log('身份证上的出生日期非法')
        return false
    }

    // 身份证号码校验
    var sum = 0,
        weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2],
        codes = "10X98765432"
    for (var i = 0; i < sId.length - 1; i++) {
        sum += sId[i] * weights[i];
    }
    var last = codes[sum % 11]; //计算出来的最后一位身份证号码
    if (sId[sId.length - 1] != last) {
        console.log('你输入的身份证号非法')
        return false
    }

    return true
}
39.随机数范围

export const random = (min, max) => {
    if (arguments.length === 2) {
        return Math.floor(min + Math.random() * ((max + 1) - min))
    } else {
        return null;
    }
}
40.将阿拉伯数字翻译成中文的大写数字

export const numberToChinese = (num) => {
    var AA = new Array("零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十");
    var BB = new Array("", "十", "百", "仟", "萬", "億", "点", "");
    var a = ("" + num).replace(/(^0*)/g, "").split("."),
        k = 0,
        re = "";
    for (var i = a[0].length - 1; i >= 0; i--) {
        switch (k) {
            case 0:
                re = BB[7] + re;
                break;
            case 4:
                if (!new RegExp("0{4}//d{" + (a[0].length - i - 1) + "}$")
                    .test(a[0]))
                    re = BB[4] + re;
                break;
            case 8:
                re = BB[5] + re;
                BB[7] = BB[5];
                k = 0;
                break;
        }
        if (k % 4 == 2 && a[0].charAt(i + 2) != 0 && a[0].charAt(i + 1) == 0)
            re = AA[0] + re;
        if (a[0].charAt(i) != 0)
            re = AA[a[0].charAt(i)] + BB[k % 4] + re;
        k++;
    }

    if (a.length > 1) // 加上小数部分(如果有小数部分)
    {
        re += BB[6];
        for (var i = 0; i < a[1].length; i++)
            re += AA[a[1].charAt(i)];
    }
    if (re == '一十')
        re = "十";
    if (re.match(/^一/) && re.length == 3)
        re = re.replace("一", "");
    return re;
}
41.将数字转换为大写金额

export const changeToChinese = (Num) => {
    //判断如果传递进来的不是字符的话转换为字符
    if (typeof Num == "number") {
        Num = new String(Num);
    };
    Num = Num.replace(/,/g, "") //替换tomoney()中的“,”
    Num = Num.replace(/ /g, "") //替换tomoney()中的空格
    Num = Num.replace(/￥/g, "") //替换掉可能出现的￥字符
    if (isNaN(Num)) { //验证输入的字符是否为数字
        //alert("请检查小写金额是否正确");
        return "";
    };
    //字符处理完毕后开始转换，采用前后两部分分别转换
    var part = String(Num).split(".");
    var newchar = "";
    //小数点前进行转化
    for (var i = part[0].length - 1; i >= 0; i--) {
        if (part[0].length > 10) {
            return "";
            //若数量超过拾亿单位，提示
        }
        var tmpnewchar = ""
        var perchar = part[0].charAt(i);
        switch (perchar) {
            case "0":
                tmpnewchar = "零" + tmpnewchar;
                break;
            case "1":
                tmpnewchar = "壹" + tmpnewchar;
                break;
            case "2":
                tmpnewchar = "贰" + tmpnewchar;
                break;
            case "3":
                tmpnewchar = "叁" + tmpnewchar;
                break;
            case "4":
                tmpnewchar = "肆" + tmpnewchar;
                break;
            case "5":
                tmpnewchar = "伍" + tmpnewchar;
                break;
            case "6":
                tmpnewchar = "陆" + tmpnewchar;
                break;
            case "7":
                tmpnewchar = "柒" + tmpnewchar;
                break;
            case "8":
                tmpnewchar = "捌" + tmpnewchar;
                break;
            case "9":
                tmpnewchar = "玖" + tmpnewchar;
                break;
        }
        switch (part[0].length - i - 1) {
            case 0:
                tmpnewchar = tmpnewchar + "元";
                break;
            case 1:
                if (perchar != 0) tmpnewchar = tmpnewchar + "拾";
                break;
            case 2:
                if (perchar != 0) tmpnewchar = tmpnewchar + "佰";
                break;
            case 3:
                if (perchar != 0) tmpnewchar = tmpnewchar + "仟";
                break;
            case 4:
                tmpnewchar = tmpnewchar + "万";
                break;
            case 5:
                if (perchar != 0) tmpnewchar = tmpnewchar + "拾";
                break;
            case 6:
                if (perchar != 0) tmpnewchar = tmpnewchar + "佰";
                break;
            case 7:
                if (perchar != 0) tmpnewchar = tmpnewchar + "仟";
                break;
            case 8:
                tmpnewchar = tmpnewchar + "亿";
                break;
            case 9:
                tmpnewchar = tmpnewchar + "拾";
                break;
        }
        var newchar = tmpnewchar + newchar;
    }
    //小数点之后进行转化
    if (Num.indexOf(".") != -1) {
        if (part[1].length > 2) {
            // alert("小数点之后只能保留两位,系统将自动截断");
            part[1] = part[1].substr(0, 2)
        }
        for (i = 0; i < part[1].length; i++) {
            tmpnewchar = ""
            perchar = part[1].charAt(i)
            switch (perchar) {
                case "0":
                    tmpnewchar = "零" + tmpnewchar;
                    break;
                case "1":
                    tmpnewchar = "壹" + tmpnewchar;
                    break;
                case "2":
                    tmpnewchar = "贰" + tmpnewchar;
                    break;
                case "3":
                    tmpnewchar = "叁" + tmpnewchar;
                    break;
                case "4":
                    tmpnewchar = "肆" + tmpnewchar;
                    break;
                case "5":
                    tmpnewchar = "伍" + tmpnewchar;
                    break;
                case "6":
                    tmpnewchar = "陆" + tmpnewchar;
                    break;
                case "7":
                    tmpnewchar = "柒" + tmpnewchar;
                    break;
                case "8":
                    tmpnewchar = "捌" + tmpnewchar;
                    break;
                case "9":
                    tmpnewchar = "玖" + tmpnewchar;
                    break;
            }
            if (i == 0) tmpnewchar = tmpnewchar + "角";
            if (i == 1) tmpnewchar = tmpnewchar + "分";
            newchar = newchar + tmpnewchar;
        }
    }
    //替换所有无用汉字
    while (newchar.search("零零") != -1)
        newchar = newchar.replace("零零", "零");
    newchar = newchar.replace("零亿", "亿");
    newchar = newchar.replace("亿万", "亿");
    newchar = newchar.replace("零万", "万");
    newchar = newchar.replace("零元", "元");
    newchar = newchar.replace("零角", "");
    newchar = newchar.replace("零分", "");
    if (newchar.charAt(newchar.length - 1) == "元") {
        newchar = newchar + "整"
    }
    return newchar;
}
42.判断一个元素是否在数组中

export const contains = (arr, val) => {
    return arr.indexOf(val) != -1 ? true : false;
}
43.数组排序，{type} 1：从小到大 2：从大到小 3：随机

export const sort = (arr, type = 1) => {
    return arr.sort((a, b) => {
        switch (type) {
            case 1:
                return a - b;
            case 2:
                return b - a;
            case 3:
                return Math.random() - 0.5;
            default:
                return arr;
        }
    })
}
44.去重

export const unique = (arr) => {
    if (Array.hasOwnProperty('from')) {
        return Array.from(new Set(arr));
    } else {
        var n = {}, r = [];
        for (var i = 0; i < arr.length; i++) {
            if (!n[arr[i]]) {
                n[arr[i]] = true;
                r.push(arr[i]);
            }
        }
        return r;
    }
}
45.求两个集合的并集

export const union = (a, b) => {
    var newArr = a.concat(b);
    return this.unique(newArr);
}
46.求两个集合的交集

export const intersect = (a, b) => {
    var _this = this;
    a = this.unique(a);
    return this.map(a, function (o) {
        return _this.contains(b, o) ? o : null;
    });
}
47.删除其中一个元素

export const remove = (arr, ele) => {
    var index = arr.indexOf(ele);
    if (index > -1) {
        arr.splice(index, 1);
    }
    return arr;
}
48.将类数组转换为数组

export const formArray = (ary) => {
    var arr = [];
    if (Array.isArray(ary)) {
        arr = ary;
    } else {
        arr = Array.prototype.slice.call(ary);
    };
    return arr;
}
49.最大值

export const max = (arr) => {
    return Math.max.apply(null, arr);
}
50.最小值

export const min = (arr) => {
    return Math.min.apply(null, arr);
}
51.求和

export const sum = (arr) => {
    return arr.reduce((pre, cur) => {
        return pre + cur
    })
}
52.平均值

export const average = (arr) => {
    return this.sum(arr) / arr.length
}
53.去除空格,type: 1-所有空格 2-前后空格 3-前空格 4-后空格

export const trim = (str, type) => {
    type = type || 1
    switch (type) {
        case 1:
            return str.replace(/\s+/g, "");
        case 2:
            return str.replace(/(^\s*)|(\s*$)/g, "");
        case 3:
            return str.replace(/(^\s*)/g, "");
        case 4:
            return str.replace(/(\s*$)/g, "");
        default:
            return str;
    }
}
54.字符转换，type: 1:首字母大写 2：首字母小写 3：大小写转换 4：全部大写 5：全部小写

export const changeCase = (str, type) => {
    type = type || 4
    switch (type) {
        case 1:
            return str.replace(/\b\w+\b/g, function (word) {
                return word.substring(0, 1).toUpperCase() + word.substring(1).toLowerCase();

            });
        case 2:
            return str.replace(/\b\w+\b/g, function (word) {
                return word.substring(0, 1).toLowerCase() + word.substring(1).toUpperCase();
            });
        case 3:
            return str.split('').map(function (word) {
                if (/[a-z]/.test(word)) {
                    return word.toUpperCase();
                } else {
                    return word.toLowerCase()
                }
            }).join('')
        case 4:
            return str.toUpperCase();
        case 5:
            return str.toLowerCase();
        default:
            return str;
    }
}
55.检测密码强度

export const checkPwd = (str) => {
    var Lv = 0;
    if (str.length < 6) {
        return Lv
    }
    if (/[0-9]/.test(str)) {
        Lv++
    }
    if (/[a-z]/.test(str)) {
        Lv++
    }
    if (/[A-Z]/.test(str)) {
        Lv++
    }
    if (/[\.|-|_]/.test(str)) {
        Lv++
    }
    return Lv;
}
56.函数节流器

export const debouncer = (fn, time, interval = 200) => {
    if (time - (window.debounceTimestamp || 0) > interval) {
        fn && fn();
        window.debounceTimestamp = time;
    }
}
57.在字符串中插入新字符串

export const insertStr = (soure, index, newStr) => {
    var str = soure.slice(0, index) + newStr + soure.slice(index);
    return str;
}
58.判断两个对象是否键值相同

export const isObjectEqual = (a, b) => {
    var aProps = Object.getOwnPropertyNames(a);
    var bProps = Object.getOwnPropertyNames(b);

    if (aProps.length !== bProps.length) {
        return false;
    }

    for (var i = 0; i < aProps.length; i++) {
        var propName = aProps[i];

        if (a[propName] !== b[propName]) {
            return false;
        }
    }
    return true;
}
59.16进制颜色转RGBRGBA字符串

export const colorToRGB = (val, opa) => {

    var pattern = /^(#?)[a-fA-F0-9]{6}$/; //16进制颜色值校验规则
    var isOpa = typeof opa == 'number'; //判断是否有设置不透明度

    if (!pattern.test(val)) { //如果值不符合规则返回空字符
        return '';
    }

    var v = val.replace(/#/, ''); //如果有#号先去除#号
    var rgbArr = [];
    var rgbStr = '';

    for (var i = 0; i < 3; i++) {
        var item = v.substring(i * 2, i * 2 + 2);
        var num = parseInt(item, 16);
        rgbArr.push(num);
    }

    rgbStr = rgbArr.join();
    rgbStr = 'rgb' + (isOpa ? 'a' : '') + '(' + rgbStr + (isOpa ? ',' + opa : '') + ')';
    return rgbStr;
}
60.追加url参数

export const appendQuery = (url, key, value) => {
    var options = key;
    if (typeof options == 'string') {
        options = {};
        options[key] = value;
    }
    options = $.param(options);
    if (url.includes('?')) {
        url += '&' + options
    } else {
        url += '?' + options
    }
    return url;
}

## 技术文章
### 高级PHP工程师所应该具备哪些技能
一、平静的心态

和所有程序员一样，要写一手好的程序，没有好的心态是不行的。
　　遇事不可急躁，不可轻言放弃。
　　在程序开发过程中，尤其是初中级程序员，写出的程序或架构会遇到很多问题，其中一些问题比较弱智，而有些问题根本没有碰到过，于是不可太过急躁，应该逐个排查问题的最初源泉，将其干掉。急躁的心态去开发系统是对项目的一种不负责。急躁会让人学会将就，让人学会逃避。而我个人北京两年的简单生活，给我其中一个最大的历练也就是：我的心态更加平静了。
　　相信，这样的心态也会有助于你其他方面的处事能力。
　　为什么将心态列入其中，我是想说明：他不同于销售的职能，需要很大激情澎湃，而是需要静静的思考。

二、一套烂熟于心的问题解决思路

曾经有位程序开发的同事在QQ签名中写到：每解决一个bug，就给自己一个提升。的确，没有真正解决过无数的bug或问题的程序员，谈不上专家，谈不上高级程序员。而一个高级程序员正是从这种解决问题的过程中不断的历练自己，形成一套烂熟于心的问题解决思路，要自己强大的。
　　我也简单说说PHP程序员成长过程中经常遇到的一些问题，如果你一个也没遇到或很少遇到，那么您就是两个极端的人：要么初级入门，要么高级了，哈哈。

1，编码问题

2，PHP和SQL数据库执行效率问题

3，Session和Cookie域和加密解析问题

4，程序的执行顺序问题

5，程序编写的多环境适用问题

6，分类的构建和结构设计问题

7，字符串处理问题：正则表达式处理或简单PHP字符串处理函数来处理

8，各种模板引擎的编写局限性问题

9，PHP和web端数据交互问题（如ajax，接口调用等）

三、过硬的PHP基础知识

没有过硬的PHP基础知识，哪怕心态再好，问题解决的能力再强，也只能纸上谈兵。
　　过硬的基础知识会让你在项目开发过程中游刃有余。
　　我也简单说说哪些属于PHP工程师所应具备的基础知识（其实这些在招聘需求中很常见）：

1，语法规则，这个不说了，这个不会，就没入门，赶紧买本书或找个网站补补

2，MYSQL各种sql语句的写法，增删改查基本的不说了，in(),union,left(),left join,as,replace,alter table,where的字段排序,各种索引建立的方法要特别熟悉

3，会自己搭建LAMP环境和WAMP环境，用集成软件一键式安装的不算。开发程序，对于自己开发的环境构建结构都不清楚，怎么排查问题？所以至少要会用对立的msi文件来安装自己需要的开发环境。安装3-5遍成功，这个算还行，还得会安装各种扩展，配置apache服务，知道各种参数设置的地方以及知道怎么设置各种参数；会linux操作系统的基本命令。

4，熟悉web方面的其他程序，因为PHP不是一个完全独立的东西，他是一个和其他语言和要素配合来完成一个项目的，如果对其他语言和要素不太熟悉，在团队协作过程中会非常吃力。这些其他要素包括：html，javascript，jquery，xml，http协议，正则表达式等

四、综合的互联网应用及项目管理知识和素养

1，见识广博，擅于学习

只顾自己专研，不看看、学学人家的做法，会像井底之蛙，难以看到广阔的天空的；所以，不要只顾着天天编程，学会抽点时间去看看一些大型开源系统的架构思路，以及大型商务网站的构建方式。向他们学习，补充自己的不足。
　　比如至少该晓得不同类型的开源系统有哪些吧，比如Uchome,dede,phpcms,wordpress,discuz,帝国等等
　　看多了，你也会总结发现一些常规性的思路，比如缓存的机制，比如模板机制，比如静态页面生成等等。

2，项目解决方案选型
　　不同需求，用不同的机构和选型。也就是常说的“水来土掩，兵来将挡”，有些架构固然强大，但是用于小型项目也会很吃力，就是杀机不用牛刀。根据需求来选型很重要。
　　选型不是随口就能定的，需要一个PHP程序员用于良好的储备，个人觉得至少需要以下储备，才具备选型能力：
　　熟练应用至少一个PHP框架，两-三个PHP开源系统；拥有自己的一套应用系统。

3，良好的项目管理素养

项目不是一直开发过程中，项目也会进入运营期，维护期，这样，具备良好的项目管理素养会使项目更加稳定，可控。
　　良好的项目管理素养包括：
　　良好的项目开发及维护习惯，记住：千万别为了一时的省力，造成后面多次的重复劳动。时时提醒自己将工作流程化，流程规划化，规范简单化。
　　良好的多人合作管理意识：项目不是一个人的，是多人协作的产物，也是服务于大众的，因而，要提升协作意识，让相关人员一同来完善项目。

4，丰富的项目开发应用经验
　　学理论，去考试或考核是学校里面的事儿，没有项目经验，就像满肚子经文，吐也难吐出。
　　这就需要实际的项目将自己的知识去学会转化为需求实现。

5，良好的开发规范

代码可读性强：对象，方法，函数的注释；一套成熟的命名规范；
　　代码冗余度底：程序和文件的重用性大，高内聚，低耦合
　　执行效率高：用最简单的程序流程实现应用需求，勿扰大弯子
　　代码安全性好：做一名警惕的程序员，任何有用户输入和上传文件的地方都得额外谨慎，也许一个程序员一时的疏忽就会导致一个系统顷刻间崩溃。
　　另外，多废话几句，PHP高级工程师，其实对于一个稍微能坚持，并喜欢PHP的来说不太难；难的是学会用工具来实现想法，不管是自己的想法还是他人的需求，学会转化。
　　这样，不防多了解些互联网发展的趋势，项目开发管理流程等等

### 最简洁的PHP程序员学习路线及建议
我们要有一个循序渐进的学习过程，这里先把学习PHP的过程做一下概括，这和很多学习PHP的爱好者是不谋而合的：

(1) 熟悉HTML/CSS/JS、、网页基本元素，完成阶段可自行制作简单的网页，对元素属性相对熟悉

(2) 理解动态语言的概念和运做机制，熟悉基本的PHP语法

(3) 学习如何将PHP与HTML结合起来，完成简单的动态页面

(4) 接触学习MySQL，开始设计数据库

(5) 不断巩固PHP语法，熟悉大部分的PHP常用函数，理解面向对象编程，MySQL优化，以及一些模板和框架

(6) 最终完成一个功能齐全的动态站点

新手不要看到上面的概括就以为PHP学习是很简单的，编程是需要你认真的思考和不断的实践。 下面具体解释一下PHP的学习线路。 首先，任何网站全都是由网页组成的，也就是说想完成一个网站，必须先学会做网页，掌握静态网页的制作技术是学习开发网站的先决条件。 因此我们要学习HTML，为今后制作网站打下基础。 学习HTML应该边学边做，HTML中的任何元素都要亲自实践，只有明白了什么元素会起到什么效果之后，才能深刻记忆，一味的看书是不行的

假设你已经可以完成一个静态页面了，那么就该开始了解动态语言，刚一接触动态语言，可能很多人都会拥有很多不解，代码不是作为直接输出的，而是要经过处理的，HTML是经过HTML解析器，而PHP也要通过PHP解析器，跟学习HTML一样的道理，想让任何的解析器工作，就必须使用它专用的语法结构

学习PHP，你应该感到幸运，因为如果你学过其他语言，你就会发现PHP还是相对简单的，这一阶段，你要搞清楚HTML和PHP的概念，你现在完全可以让PHP给你算算一加一、、于几，然后在浏览器输出。 不要觉得幼稚，这虽然是很小的一段代码，但是对于你的编程之路，可是迈出了一大步。 不过现在，你还是一个菜鸟

接下来就要学习数据库了，MySQL可以说是PHP的黄金搭档，我们要征服这个数据库，在你理解了数据库的概念之后，就要尝试通过PHP来连接数据库，进而会用PHP成功的插入，删除和更新数据

这个时候，你可能会处于这种状态：你会HTML吗？会，我能编好几个表格排板的网页呢！你会PHP吗？会，我会把一加一的运算写在函数里，然后调用！你会MySQL吗？会，我可以把数据库里的数据插入删除啦！

那接下来该做什么呢？尝试着做个小的留言本吧，这同样是新手面临的一道关卡。 花了一段时间，你终于学会把表单的数据插入数据库，然后显示出来了，应该说一个程序的雏形已经诞生了。 但是，你可能会看人家这个编论坛，那个开发CMS，我什么时候可以写一个呢？不要急，再巩固一下知识，熟悉了PHP和MySQL开发的要领后，再回头看你写的那个留言本，你也许会怀疑那真的是你写的吗？这个时候，你可以完善一下你写的留言本。 留言本应该加入注册以及分页的功能，可以的话，UI也可以加强

这就算学会了吗？NO，NO，NO，还早呢，你到现在还没碰过OOP呢吧？那模板和框架呢？还要继续学习呀！PHP框架提供了一个用以构建web应用的基本框架，从而简化了用PHP编写web应用程序的流程。 可以节省开发时间、、有助于建立更稳定的应用。 所以说，PHP框架是一个可以用来节省时间并强化自己代码的工具。 当你第一次选择PHP框架时，建议多尝试几个，每个框架都有自己的长处和短处，例如Zend框架由于多样的功能、、并且有一个广泛的支持系统，流行了很长时间。 而CakePHP是一个晚于Zend的PHP框架，相应的支持系统也比较少，但是更为方便和易于使用

了解了面向对象和框架后，你应该接触一下XML了，总而言之，你绝对不会发现你全部都学会了，学无止境！学东西，永远不要妄想有速成这一说，技巧再多，但是缺少努力，那也是白搭。 有一点可以保证，就是你学会了PHP，那么再学其它语言，肯定速成，反过来也一样，如果你之前学过其它的语言，那么学PHP肯定快

多借鉴别人成功的代码，绝对是有益无害，所以要多看那些经过千锤百炼凝出来的经典代码，是进步的最好方法。 另外，要强调的是，学习一项技术过程中可能会遇到困难，可能会迷茫，你也许学了一半的PHP，又开始打C#的主意，或者有人说Java很好，这个时候你绝对不能动摇，要坚持到底，彻底学会。 祝你顺利学成PHP，开发自己想要的网站

最后，分享10条PHP性能优化的小技巧，帮助你更好的用PHP开发：

1、、foreach效率更高，尽量用foreach代替while和for循环

2、、循环内部不要声明变量，尤其是对象这样的变量

3、、在多重嵌套循环中，如有可能，应当将最长的循环放在内层，最短循环放在外层，从而减少cpu跨循环层的次数，优化程序性能

4、、用单引号替代双引号引用字符串以实现PHP性能优化

5、、用i+=1代替i=i+1。 符合c/c++的习惯，效率还高

6、优化Select SQL语句，在可能的情况下尽量少的进行Insert、Update操作，达到PHP性能优化的目的

7、、尽量的少进行文件操作，虽然PHP的文件操作效率也不低的

8、、尽可能的使用PHP内部函数

9、、在可以用PHP内部字符串操作函数的情况下，不要用正则表达式

10、feof、fgets、fopen、在可以用file_get_contents替代file、系列方法的情况下，尽量用 file_get_contents，因为它的效率高得多。 但是要注意file_get_contents在打开一个URL文件时候的PHP版本问题
### 优化PHP代码的一些建议
如果一个方法可静态化，就对它做静态声明。速率可提升至4倍。
echo 比 print 快。
使用echo的多重参数（译注：指用逗号而不是句点）代替字符串连接。
在执行for循环之前确定最大循环数，不要每循环一次都计算最大值。
注销那些不用的变量尤其是大数组，以便释放内存。
尽量避免使用__get , __set , __autoload。
require_once() 代价昂贵。
在包含文件时使用完整路径，解析操作系统路径所需的时间会更少。
如果你想知道脚本开始执行（译注：即服务器端收到客户端请求）的时刻，使用$_SERVER[‘REQUEST_TIME’]要好于time()。
函数代替正则表达式完成相同功能。
str_replace函数比preg_replace函数快，但strtr函数的效率是str_replace函数的四倍。
如果一个字符串替换函数，可接受数组或字符作为参数，并且参数长度不太长，那么可以考虑额外写一段替换代码，使得每次传递参数是一个字符，而不是只写一行代码接受数组作为查询和替换的参数。
使用选择分支语句（译注：即switch case）好于使用多个if，else if语句。
用@屏蔽错误消息的做法非常低效。
打开apache的mod_deflate模块。
数据库连接当使用完毕时应关掉。
$row['id']的效率是$row[id]的7倍。
错误消息代价昂贵。
尽量不要在for循环中使用函数，比如for ($x=0; $x < count($array); $x)每循环一次都会调用count()函数。
在方法中递增局部变量，速度是最快的。几乎与在函数中调用局部变量的速度相当。
递增一个全局变量要比递增一个局部变量慢2倍。
递增一个对象属性（如：$this->prop++）要比递增一个局部变量慢3倍。
递增一个未预定义的局部变量要比递增一个预定义的局部变量慢9至10倍。
仅定义一个局部变量而没在函数中调用它，同样会减慢速度（其程度相当于递增一个局部变量）。PHP大概会检查看是否存在全局变量。
方法调用看来与类中定义的方法的数量无关，因为我（在测试方法之前和之后都）添加了10个方法，但性能上没有变化。
派生类中的方法运行起来要快于在基类中定义的同样的方法。
调用带有一个参数的空函数，其花费的时间相当于执行7至8次的局部变量递增操作。类似的方法调用所花费的时间接近于15次的局部变量递增操作。
用单引号代替双引号来包含字符串，这样做会更快一些。因为PHP会在双引号包围的字符串中搜寻变量，单引号则不会。当然，只有当你不需要在字符串中包含变量时才可以这么做。
输出多个字符串时，用逗号代替句点来分隔字符串，速度更快。注意：只有echo能这么做，它是一种可以把多个字符串当作参数的“函数”（译注：PHP手册中说echo是语言结构，不是真正的函数，故把函数加上了双引号）。
Apache解析一个PHP脚本的时间要比解析一个静态HTML页面慢2至10倍。尽量多用静态HTML页面，少用脚本。
除非脚本可以缓存，否则每次调用时都会重新编译一次。引入一套PHP缓存机制通常可以提升25%至100%的性能，以免除编译开销。
尽量做缓存，可使用memcached。memcached是一款高性能的内存对象缓存系统，可用来加速动态Web应用程序，减轻数据库负载。对运算码 (OP code)的缓存很有用，使得脚本不必为每个请求做重新编译。
当操作字符串并需要检验其长度是否满足某种要求时，你想当然地会使用strlen()函数。此函数执行起来相当快，因为它不做任何计算，只返回在zval 结构（C的内置数据结构，用于存储PHP变量）中存储的已知字符串长度。但是，由于strlen()是函数，多多少少会有些慢，因为函数调用会经过诸多步骤，如字母小写化（译注：指函数名小写化，PHP不区分函数名大小写）、哈希查找，会跟随被调用的函数一起执行。在某些情况下，你可以使用isset() 技巧加速执行你的代码。举例如下:if (strlen($foo) < 5) { echo 'Foo is too short'; }与下面的技巧做比较 if (!isset($foo)) { echo 'Foo is too short'; } 调用isset()恰巧比strlen()快，因为与后者不同的是，isset()作为一种语言结构，意味着它的执行不需要函数查找和字母小写化。也就是说，实际上在检验字符串长度的顶层代码中你没有花太多开销。
当执行变量$i的递增或递减时，$i++会比++$i慢一些。这种差异是PHP特有的，并不适用于其他语言，所以请不要修改你的C或Java代码并指望它们能立即变快，没用的。++$i更快是因为它只需要3条指令(opcodes)，$i++则需要4条指令。后置递增实际上会产生一个临时变量，这个临时变量随后被递增。而前置递增直接在原值上递增。这是最优化处理的一种，正如Zend的PHP优化器所作的那样。牢记这个优化处理不失为一个好主意，因为并不是所有的指令优化器都会做同样的优化处理，并且存在大量没有装配指令优化器的互联网服务提供商（ISPs）和服务器。
并不是事必面向对象(OOP)，面向对象往往开销很大，每个方法和对象调用都会消耗很多内存。
并非要用类实现所有的数据结构，数组也很有用。
不要把方法细分得过多，仔细想想你真正打算重用的是哪些代码？
当你需要时，你总能把代码分解成方法。
尽量采用大量的PHP内置函数。
如果在代码中存在大量耗时的函数，你可以考虑用C扩展的方式实现它们。
评估检验(profile)你的代码。检验器会告诉你，代码的哪些部分消耗了多少时间。Xdebug调试器包含了检验程序，评估检验总体上可以显示出代码的瓶颈。
mod_zip可作为Apache模块，用来即时压缩你的数据，并可让数据传输量降低80%。

### TP5性能优化建议
架构及开发过程优化建议：

路由尽量使用域名路由或者路由分组
在路由中进行验证和权限判断
合理规划数据表字段类型及索引
结合业务逻辑使用数据缓存，减少数据库压力
在应用完成部署之后，建议对应用进行相关优化，包括：
首先说明 如果是linux 或者是Mac,需要给予权限才能操作

以下方法建议，在网站稳定后再生成上传

如果开发过程中开启了调试模式的话，关闭调试模式（参考调试模式）
关闭调试模式PHP

// 应用调试模式
'app_debug' => false
// 应用调试模式
'app_debug' => false
如果使用.env 记得删除
通过命令行生成类库映射文件
php think optimize:autoload
类库映射文件可以提高自动加载的性能

成功以后会在runtime目录下生成 classmap.php 文件

通过命令行生成配置缓存文件

php think optimize:config
默认生成应用的配置缓存文件，调用后会在runtime目录下面生成 init.php 文件，生成配置缓存文件后，应用目录下面的 config.php common.php 以及 tags.php 不会被加载，被 runtime/init.php 取代。

这里要注意 在本地生成配置缓存时 需要把数据库等重要的配置替换成服务器上的配置以后 ，在生成

通过命令行生成数据表字段缓存文件

php think optimize:schema
执行完毕，会在 runtime 目录下面创建 schema 目录，然后在该目录下面按照 database.table.php 的文件命名生成数据表字段缓存文件。

通过命令行生成路由缓存文件

php think optimize:route
如果你的应用定义了大量的路由规则，那么建议在实际部署后生成路由缓存文件，可以免去路由注册的开销，从而改善路由的检测效率

开启请求缓存
开启请求缓存PHP

// 是否开启请求缓存 true自动缓存 支持设置请求缓存规则
'request_cache' => false,
1
2
// 是否开启请求缓存 true自动缓存 支持设置请求缓存规则
'request_cache' => false,
如果你的数据实时性不是很大 可以开启

### 程序猿专用代码注释:佛祖保佑，永无BUG
//
//                            _ooOoo_  
//                           o8888888o  
//                           88" . "88  
//                           (| -_- |)  
//                            O\ = /O  
//                        ____/`---'\____  
//                      .   ' \\| |// `.  
//                       / \\||| : |||// \  
//                     / _||||| -:- |||||- \  
//                       | | \\\ - /// | |  
//                     | \_| ''\---/'' | |  
//                      \ .-\__ `-` ___/-. /  
//                   ___`. .' /--.--\ `. . __  
//                ."" '< `.___\_<|>_/___.' >'"".  
//               | | : `- `.;`\ _ /`;.`/ - ` : | |  
//                 \ \ `-. \_ __\ /__ _/ .-` / /  
//         ======`-.____`-.___\_____/___.-`____.-'======  
//                            `=---='  
//  
//         .............................................  
//                  佛祖保佑             永无BUG 
//
//          佛曰:  
//
//                  写字楼里写字间，写字间里程序员； 
// 
//                  程序人员写程序，又拿程序换酒钱。  
//
//                  酒醒只在网上坐，酒醉还来网下眠；  
//
//                  酒醉酒醒日复日，网上网下年复年。  
//
//                  但愿老死电脑间，不愿鞠躬老板前；  
//
//                  奔驰宝马贵者趣，公交自行程序员。  
//
//                  别人笑我忒疯癫，我笑自己命太贱； 
// 
//                  不见满街漂亮妹，哪个归得程序员？
//

### 一组匹配中国大陆手机号码的正则表达式
正则表达式
匹配所有号码（手机卡 + 数据卡 + 上网卡）
^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7[^29\D](?(?<=4)(?:0\d|1[0-2]|9\d)|\d{2})|9[189]\d{2}|6[567]\d{2}|4(?:[14]0\d{3}|[68]\d{4}|[579]\d{2}))\d{6}$

匹配所有支持短信功能的号码（手机卡 + 上网卡）
^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7[^29\D](?(?<=4)(?:0\d|1[0-2]|9\d)|\d{2})|9[189]\d{2}|6[567]\d{2}|4[579]\d{2})\d{6}$

手机卡
匹配所有
^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7[^0129\D](?(?<=4)(?:0\d|1[0-2]|9\d)|\d{2})|9[189]\d{2}|66\d{2})\d{6}$

匹配中国移动
^(?:\+?86)?1(?:3[^0-3\D](?(?<=4)[^9\D]|\d)|5[^3-6\D]\d|8[23478]\d|(?:78|98)\d)\d{7}$

匹配中国联通
^(?:\+?86)?1(?:3[0-2]|[578][56]|66)\d{8}$

匹配中国电信
^(?:\+?86)?1(?:3[34](?(?<=4)(?:9)|\d)\d|53\d{2}|8[019]\d{2}|7[347](?(?<=4)(?:0[0-5])|\d{2})|9[19]\d{2})\d{6}$

匹配北京船舶通信导航有限公司（海事卫星通信）
^(?:\+?86)?1749\d{7}$

工业和信息化部应急通信保障中心（应急通信）
^(?:\+?86)?174(?:0[6-9]|1[0-2])\d{6}$

虚拟运营商
匹配所有
^(?:\+?86)?1(?:7[01]|6[57])\d{8}$

匹配中国移动
^(?:\+?86)?1(?:65\d|70[356])\d{7}$

匹配中国联通
^(?:\+?86)?1(?:70[4789]|71\d|67\d)\d{7}$

匹配中国电信
^(?:\+?86)?170[0-2]\d{7}$

物联网数据卡
匹配所有
^(?:\+?86)?14(?:[14]0|[68]\d)\d{9}$

匹配中国移动
^(?:\+?86)?14(?:40|8\d)\d{9}$

匹配中国联通
^(?:\+?86)?146\d{10}$

匹配中国电信
^(?:\+?86)?1410\d{9}$

上网卡
匹配所有
^(?:\+?86)?14[579]\d{8}$

匹配中国移动
^(?:\+?86)?147\d{8}$

匹配中国联通
^(?:\+?86)?145\d{8}$

匹配中国电信
^(?:\+?86)?149\d{8}$

在线测试/调试
https://regex101.com
https://regexr.com
https://www.debuggex.com（PCRE 在线视觉化）

规则
手机卡 - 基础运营商
支持语音通话 / 短信 / 数据流量
号码长度 11 位
运营商[1]	号段
中国移动	134-0~8 / 135 / 136 / 137 / 138 / 139 / 150 / 151 / 152 / 157 / 158 / 159 / 178 / 182 / 183 / 184 / 187 / 188 / 198
中国联通	130 / 131 / 132 / 155 / 156 / 166 / 175 / 176 / 185 / 186
中国电信	133 / 134-9 / 153 / 173 / 174-00~05 / 177 / 180 / 181 / 189 / 191 / 199
北京船舶通信导航有限公司（海事卫星通信）	174-9
工业和信息化部应急通信保障中心（应急通信）	174-06~12
手机卡 - 虚拟运营商
支持语音通话 / 短信 / 数据流量
号码长度 11 位
运营商[1]	号段
中国移动	165 / 1703 / 1705 / 1706
中国联通	167 / 1704 / 1707 / 1708 / 1709 / 171
中国电信	1700 / 1701 / 1702
物联网数据卡
支持数据流量
号码长度 13 位
运营商[1]	号段
中国移动	1440X / 148XX
中国联通	146XX
中国电信	1410X
上网卡
支持语音通话（部分） / 短信 / 数据流量
号码长度 11 位
运营商[1]	号段	语音通话[2]
中国移动	147	支持
中国联通	145	不支持
中国电信	149	支持
根据工信部相关文件，145 / 147 / 149 号段允许提供语音通话功能，运营商可以根据用户需要自主决定是否提供语音通话功能。目前 147 / 149 号段已经有支持语音通话的号码卡放出。

### Apache/Nginx/PHP服务器反爬虫代码大全
一、Apache

①、通过修改 .htaccess 文件

修改网站目录下的.htaccess，添加如下代码即可(2 种代码任选)：

可用代码 (1)：

 RewriteEngine On
 RewriteCond %{HTTP\_USER\_AGENT} (^$|FeedDemon|Indy Library|Alexa Toolbar|AskTbFXTV|AhrefsBot|CrawlDaddy|CoolpadWebkit|Java|Feedly|UniversalFeedParser|ApacheBench|Microsoft URL Control|Swiftbot|ZmEu|oBot|jaunty|Python–urllib|lightDeckReports Bot|YYSpider|DigExt|HttpClient|MJ12bot|heritrix|EasouSpider|Ezooms) \[NC\] 
 RewriteRule ^(.\*)$ – \[F\]
可用代码 (2)：

SetEnvIfNoCase ^User–Agent$ .\*(FeedDemon|Indy Library|Alexa Toolbar|AskTbFXTV|AhrefsBot|CrawlDaddy|CoolpadWebkit|Java|Feedly|UniversalFeedParser|ApacheBench|Microsoft URL Control|Swiftbot|ZmEu|oBot|jaunty|Python–urllib|lightDeckReports Bot|YYSpider|DigExt|HttpClient|MJ12bot|heritrix|EasouSpider|Ezooms) BADBOT 
Order Allow,Deny 
Allow fromall
Deny from env=BADBOT
②、通过修改 httpd.conf 配置文件

找到如下类似位置，根据以下代码 新增 / 修改，然后重启 Apache 即可：

 DocumentRoot /home/wwwroot/xxx 
 SetEnvIfNoCase User–Agent “.\*(FeedDemon|Indy Library|Alexa Toolbar|AskTbFXTV|AhrefsBot|CrawlDaddy|CoolpadWebkit|Java|Feedly|UniversalFeedParser|ApacheBench|Microsoft URL Control|Swiftbot|ZmEu|oBot|jaunty|Python-urllib|lightDeckReports Bot|YYSpider|DigExt|HttpClient|MJ12bot|heritrix|EasouSpider|Ezooms)” BADBOT 
          Order allow,deny 
          Allow fromall
         deny from env=BADBOT 

二、Nginx 代码

进入到 nginx 安装目录下的 conf 目录，将如下代码保存为 agent_deny.conf

cd /usr/local/nginx/conf 
 vim agent\_deny.conf
 #禁止Scrapy等工具的抓取 
 if ($http\_user\_agent ~\* (Scrapy|Curl|HttpClient)) { 
     return 403; 
  } 
  #禁止指定UA及UA为空的访问 
 if ($http\_user\_agent ~\* “FeedDemon|Indy Library|Alexa Toolbar|AskTbFXTV|AhrefsBot|CrawlDaddy|CoolpadWebkit|Java|Feedly|UniversalFeedParser|ApacheBench|Microsoft URL Control|Swiftbot|ZmEu|oBot|jaunty|Python-urllib|lightDeckReports Bot|YYSpider|DigExt|HttpClient|MJ12bot|heritrix|EasouSpider|Ezooms|^$” ) { 
    return 403;             
 } 
 #禁止非GET|HEAD|POST方式的抓取 
  if ($request\_method !~ ^(GET|HEAD|POST)$) { 
      return 403; 
  }
然后，在网站相关配置中的 location / { 之后插入如下代码：
Shell

 include agent\_deny.conf; 
如下的配置：

Shell

 \[marsge@Mars\_Server ~\]$ cat /usr/local/nginx/conf/zhangge.conf 
 location / { 
         try\_files $uri $uri/ /index.php?$args; 
         #这个位置新增1行： 
         include agent\_deny.conf; 
         rewrite ^/sitemap\_360\_sp.txt$ /sitemap\_360\_sp.php last; 
.          rewrite ^/sitemap\_baidu\_sp.xml$ /sitemap\_baidu\_sp.php last; 
.          rewrite ^/sitemap\_m.xml$ /sitemap\_m.php last; 
保存后，执行如下命令，平滑重启 nginx 即可：

Shell

 /usr/local/nginx/sbin/nginx –s reload
三、PHP 代码

将如下方法放到贴到网站入口文件 index.php 中的第一个

PHP

  //获取UA信息 
  $ua = $\_SERVER\[‘HTTP\_USER\_AGENT’\]; 
  //将恶意USER\_AGENT存入数组 
  $now\_ua = array(‘FeedDemon ‘,‘BOT/0.1 (BOT for JCE)’,‘CrawlDaddy ‘,‘Java’,‘Feedly’,‘UniversalFeedParser’,‘ApacheBench’,‘Swiftbot’,‘ZmEu’,‘Indy Library’,‘oBot’,‘jaunty’,‘YandexBot’,‘AhrefsBot’,‘MJ12bot’,‘WinHttp’,‘EasouSpider’,‘HttpClient’,‘Microsoft URL Control’,‘YYSpider’,‘jaunty’,‘Python-urllib’,‘lightDeckReports Bot’); 
 //禁止空USER\_AGENT，dedecms等主流采集程序都是空USER\_AGENT，部分sql注入工具也是空USER\_AGENT 
  if(!$ua) { 
      header(“Content-type: text/html; charset=utf-8”); 
     die(‘请勿采集本站，因为采集的站长木有小JJ！’); 

  }else{ 
     foreach($now\_ua as $value ) 
 //判断是否是数组中存在的UA 
     if(eregi($value,$ua)) { 
         header(“Content-type: text/html; charset=utf-8”); 
         die(‘请勿采集本站，因为采集的站长木有小JJ！’); 
      } 
  }
四、测试效果

模拟宜搜蜘蛛抓取：

Shell

curl –I –A ‘YisouSpider’ bizhi.bcoderss.com 
模拟 UA 为空的抓取：

Shell

 curl –I –A ” bizhi.bcoderss.com 
模拟百度蜘蛛的抓取：

Shell

 curl –I –A ‘Baiduspider’ bizhi.bcoderss.com




