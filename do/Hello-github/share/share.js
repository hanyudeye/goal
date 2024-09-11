function shareToWeibo() {
    // 微博分享链接
    const url = encodeURIComponent(window.location.href); // 当前页面URL
    const title = encodeURIComponent(document.title); // 当前页面标题
    const weiboShareUrl = `https://service.weibo.com/share/share.php?url=${url}&title=${title}`;
    
    // 打开分享窗口
    window.open(weiboShareUrl, '_blank', 'width=600,height=400');
}

function shareToQZone() {
    // QQ空间分享链接
    const url = encodeURIComponent(window.location.href); // 当前页面URL
    const title = encodeURIComponent(document.title); // 当前页面标题
    const desc = encodeURIComponent("这是我的网页描述"); // 网页描述
    const summary = encodeURIComponent("这是我的网页摘要"); // 网页摘要
    const qzoneShareUrl = `https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=${url}&title=${title}&desc=${desc}&summary=${summary}`;

    // 打开分享窗口
    window.open(qzoneShareUrl, '_blank', 'width=600,height=400');
}

function shareToQQFriend() {
    // QQ好友分享链接
    const url = encodeURIComponent(window.location.href); // 当前页面URL
    const title = encodeURIComponent(document.title); // 当前页面标题
    const desc = encodeURIComponent("这是我的网页描述"); // 网页描述
    const qqFriendShareUrl = `http://connect.qq.com/widget/shareqq/index.html?url=${url}&title=${title}&desc=${desc}`;

    // 打开分享窗口
    window.open(qqFriendShareUrl, '_blank', 'width=600,height=400');
}