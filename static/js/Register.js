$(document).ready(function () {
    $("#bt1").click(function() {
        var UserName = $("#username").val();
        var Password1= $("#pw1").val();
        var Password2= $("#pw2").val();
        if (UserName.length<4||UserName.length>10) {
            alert("用户名输入不符合规范！！！");
        }
        else if(Password1.length<4||Password1.length>20)
        {
            alert("密码输入不符合规范！！！");
        }
        else if(Password1!==Password2)
        {
            alert("两次密码输入不一致！！！");
        }
        //初步判断输入是否符合规范，如果符合规范则通过ajax传输给后台由后台进行查重
        else {
            $.ajax({
                type: "post",
                url: '/register',     //后台action
                data:
                    {
                        username: UserName,
                        password: Password1
                    },          //username为要向后台传入的参数名称
                success: function(result)       //如果注册成功返回true，用户名被占有则返回false
                {
                    var logindata=JSON.parse(result);
                    if(logindata == null){
                        alert("链接超时");
                    }
                    else if (logindata == true) {
                        alert("注册成功！！！");
                        $(location).attr('href', '/home');
                    }
                    else if (logindata == false){
                        alert("用户名已被注册！！！");
                    }
                }
            });
        }
    });


});





