$(document).ready(function () {
    var LoginName=null;
    $("#bt2").click(function(){
        var UserName = $("#username").val();
        var Password=$("#password").val();
        if (UserName===""||Password==="")
        {
            alert("用户名或密码不能为空！！");
        }
        //初步判断输入是否符合规范，如果符合规范则通过ajax传输给后台由后台进行查重
        else {
            $.ajax({
                type: "post",
                url: '/login',     //发送请求的地址
                data:
                    {
                        username: UserName,
                        password: Password,
                    },          //向后台传入的参数
                dataType: "json",
                success: function(data)       //如果注册成功返回true，用户名被占有则返回false
                {
                    if(data.result == 'null'){
                        alert("该用户不存在！！！");
                    }
                    else if (data.result == true) {
                        LoginName=UserName;
                        alert("登陆成功！！！");
                        $(location).attr('href','/home');
                        $(".changeable a").remove();
                        $.cookie("username",UserName,{expires:1});
                        }
                    else if (data.result == false){
                        alert("密码错误！！！");
                    }
                    else{
                        alert("错误");
                    }
                }
            });
        }
    });
    if($.cookie("username")!==null){
         $(".changeable").text("Hi,"+LoginName);
         $(".changeable").attr("color","#3399cc");
    }

});