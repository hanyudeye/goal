let currentPage = 1; // 当前页码
const itemsPerPage = 10; // 每页显示条数
let totalItems = 0; // 总记录数
let isMobile = /Mobi|Android/i.test(navigator.userAgent); // 检测是否是移动设备

// 加载历史数据
function loadHistoryData(page) {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", `tech_history.json`, true); // 请求 JSON 文件
    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);
            totalItems = data.length; // 更新总记录数
            displayData(data, page);
            if (!isMobile) updatePaginationButtons(); // 非移动设备更新分页按钮状态
        }
    };
    xhr.send();
}

// 显示数据
function displayData(data, page) {
    const historyList = document.getElementById("history-list");
    if (page === 1) historyList.innerHTML = ""; // 清空当前内容，仅在第一页时
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = Math.min(page * itemsPerPage, data.length);
    const items = data.slice(startIndex, endIndex);

    items.forEach(item => {
        const li = document.createElement("li");
        li.className = "history-item";
        li.textContent = `${item.year}: ${item.event}`;
        historyList.appendChild(li);
    });

    document.getElementById("loading").style.display = 'none';
}

// 更新分页按钮状态
function updatePaginationButtons() {
    document.getElementById("prevPage").disabled = currentPage === 1;
    document.getElementById("nextPage").disabled = currentPage * itemsPerPage >= totalItems;
}

// 处理“上一页”按钮点击事件
document.getElementById("prevPage").addEventListener("click", function () {
    if (currentPage > 1) {
        currentPage--;
        loadHistoryData(currentPage);
    }
});

// 处理“下一页”按钮点击事件
document.getElementById("nextPage").addEventListener("click", function () {
    if (currentPage * itemsPerPage < totalItems) {
        currentPage++;
        loadHistoryData(currentPage);
    }
});

// 移动端上拉加载功能
if (isMobile) {
    window.addEventListener('scroll', function () {
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100) {
            currentPage++;
            if (currentPage * itemsPerPage <= totalItems) {
                loadHistoryData(currentPage);
            }
        }
    });
} else {
    // 显示桌面分页按钮
    document.getElementById("pagination").style.display = 'block';
}

// 初始化页面加载
document.addEventListener("DOMContentLoaded", function () {
    loadHistoryData(currentPage);
});
