$(document).ready(function(){
    $('#ytbSearchFrmAjax').on('submit', function(){

        // submit 이벤트 기본 기능 : 페이지 새로고침
        // 페이지 새로고침 되지 않도록
        event.preventDefault();

        // 폼에 입력한 값들을 쿼리 스트링 방식의 데이터로 변환
        // type=youtube_name&keyword=자전거
        // serialize() 사용 : 쿼리 스트링 방식의 데이터로 변환
        let formData = $(this).serialize();

        $.ajax({
            type:"post", 
            url:"http://127.0.0.1:8000/youtube/search/ajax/",
            data:formData,
            datatype:'json',
            success:function(result){
                console.log(result)
                console.log(result.youtube_list_json)

                let youtube_list = result.youtube_list_json;

                //반환된 결과를 searchResultBox <div>에 테이블 형태로 출력 (삽입)
                // div 태그에 삽입 : append()
                // 실행할 때마다 append() 이전 결과 뒤에 계속 append 됨
                // 다 삭제한 후 append 수행
                $('#ytbSearchResultBox').empty()

                // 테이블 태그 문자열로 생성
                const str = `
                    <table id="youtube_list">
                    <tr>
                        <th>youtube_id</th>
                        <th>youtube_title</th>
                        <th>youtube_link</th>
                        <th>youtube_image</th>
                        <th>youtube_hashtag</th>
                        <th>youtube_channel_name</th>
                        <th>youtube_channel_count</th>
                        <th>youtube_content_like_count</th>
                        <th>youtube_comment_like_count</th>
                        <th>youtube_youtube_content_date</th>
                    </tr>
                `

                $('#ytbSearchResultBox').append(str);

                // 데이터 추출해서 append 
                if(youtube_list.length == 0){
                    $('#youtube_list').append('<tr align="center"><td colspan="6">조건에 해당하는 결과가 없습니다</td></tr>')
                } else {
                    for(let i=0; i<youtube_list.length; i++){
                        $('#youtube_list').append('<tr><td>' +
                            youtube_list[i].pk + '</td><td>' +
                            youtube_list[i].fields.youtube_title + '</td><td>' +
                            youtube_list[i].fields.youtube_link + '</td><td>' +
                            youtube_list[i].fields.youtube_image + '</td><td>' +
                            youtube_list[i].fields.youtube_hashtag + '</td><td>' +
                            youtube_list[i].fields.youtube_channel_name + '</td><td>' +                    
                            youtube_list[i].fields.youtube_channel_count + '</td><td>' +
                            youtube_list[i].fields.youtube_content_like_count + '</td><td>' +
                            youtube_list[i].fields.youtube_comment_like_count + '</td><td>' +
                            youtube_list[i].fields.youtube_content_date + '</td></tr>');                        
                    }
                }

                $('#youtube_list').append('</table>');
            },
            error:function(){
                // 오류 발생 시 수행되는 함수
                alert("오류 발생")
            },
            complete:function(){
                // 완료 되었을 때 수행된 함수
            }
        });

    })
});