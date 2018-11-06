$(document).click(function (e) {
   var Title=$(e.target).html();
    $.ajax({
        type:"post",
        url:"/newpage",
        data:
            {
                title:Title,
                username:LoginName,
            },          //向后台传入的参数
        dataType: "json",
        success:function (data)
        {
            var Time=data.time;         //传入时间
            var Context=data.context;   //传入正文
             $("#newblock h1").text(Title);
             $("#newblock div .author").text(LoginName);
             $("#newblock div .time").text(Time);
             $("#newblock .paragraph").text(Context);
        }
    });
});