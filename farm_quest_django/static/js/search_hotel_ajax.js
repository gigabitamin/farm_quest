
document.addEventListener('DOMContentLoaded', function() {
    loadTemplate('search_hotels_price_min.html'); // 페이지 로드 시 기본 템플릿 로드
});

document.getElementById('price_min_a').addEventListener('click', function() {
    loadTemplate('search_hotels_price_min.html');
});

document.getElementById('discount_rate_a').addEventListener('click', function() {
    loadTemplate('search_hotels_discount_rate.html');
});


function loadTemplate(templateName) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8000/search_hotels/<str:keyword>/?template_name=' + templateName, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // 템플릿을 로드한 후, 템플릿 컨테이너에 새로운 내용을 삽입
            document.getElementById('ordered_container').innerHTML = xhr.responseText;
        }
    };
    xhr.send();
}















// // change_template.js

// // 버튼 클릭 이벤트 처리
// document.getElementById('changeTemplateButton').addEventListener('click', function() {
//     // 원하는 템플릿 파일명을 설정
//     var newTemplateName = "search_hotels_price_min.html";

//     // Ajax 요청
//     var xhr = new XMLHttpRequest();
//     xhr.open('GET', '/path/to/template/' + newTemplateName, true);
//     xhr.onreadystatechange = function() {
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             // 서버로부터 새로운 템플릿 내용을 받음
//             var newTemplateContent = xhr.responseText;

//             // 페이지의 일부를 업데이트
//             document.getElementById('templateContainer').innerHTML = newTemplateContent;
//         }
//     };
//     xhr.send();
// });