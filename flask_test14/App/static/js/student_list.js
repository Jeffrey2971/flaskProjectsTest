$getJSON('/api/students/', function (data) {
    console.log(data)
    // 获取json中的学生列表
    var student_list = data['data'];
    // 获取显示学生的元素容器
    var $ul_container = $('#student_list_container');
    // 遍历学生列表
    for (var i = 0; i < student_list.length; i++){
        //创建放单个学生的li
        var $li = $('<li></li>');
        //为学生添加链接
        //var $a('<a></a>');
        //为连接设置连接位置
        //$a.attr('href', '/api/students/' + student_list[i]['id'] + '/);
        //创建爱你 属性标签p
        var $p_name = $('<p></p>');
        $p_name.html(student_list[i]['name']);
        //追加内容
        //$a.append($p_name);
        //$li.append($a);
        //追加内容
        $li.append($p_name);
        $li.click(function () {
            window.open('/static/html/StudentDetail.html?id=', target='_self');
        })
    }
})