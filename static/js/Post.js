$(document).ready(function () {
   $("#BtForPost") .click(function () {
      var Time=new Date();
      var Title=$("#title").val();
      var Context=$("#context").val();
      if($.cookie("username")==undefined)
      {
          alert("请先登录！！！");
      }
      else if(Title.length<3&&Title.length>20)
      {
          alert("标题字数不符合规范！！！");
      }
      else if(Context.length<50)
      {
          alert("正文字数过少！！！");
      }
      else
      {
          $.ajax({
              type:"post",
              url:"/post",
              data:
                  {
                      title:Title,
                      context:Context,
                      username:$.cookie("username"),
                      time:Time,
                  },
              dataType:"json",
              success:function (data)
              {
                  if (data.result == true) {
                      alert("发帖成功！！！");
                      $(location).attr('href','/home');
                      $("#Body").append("<div class=\"block\">\n" +
                          "                    <a href=\"/newpage\"><h2>"+Title+"</h2></a>\n" +
                          "                </div>");                //将论坛标签块加到主页
                  }
                  else if (data.result == false){
                      alert("发帖失败！！！");
                  }
                  else{
                      alert("错误");
                  }
              }
              });
      }
   });
});