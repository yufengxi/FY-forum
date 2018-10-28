$(document).ready(function () {
    $("#pw2").click(function(){
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
                url: "check",     //发送请求的地址
                data:
                    {
                        username: UserName,
                        password: Password
                    },          //向后台传入的参数
                dataType: "text",
                success: function(result)       //如果注册成功返回true，用户名被占有则返回false
                {
                    var logindata=JSON.parse(result);
                    if(logindata.checkResult == null){
                        alert("该用户不存在！！！");
                    }
                    else if (logindata.checkResult === true) {
                        alert("登陆成功！！！");
                        $(location).attr('href', '/home');
                    }
                    else if (logindata.checkResult === false){
                        alert("密码错误！！！");
                    }
                }
            });
        }
    });

});