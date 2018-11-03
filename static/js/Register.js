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
                url: '/login',     //发送请求的地址
                data:
                    {
                        username: UserName,
                        password: Password1,
                    },          //向后台传入的参数
                dataType: "json",
                success: function(data)       //如果注册成功返回true，用户名被占有则返回false
                {
                    
                    if(data.result == 'null'){
                        alert("该用户不存在！！！");
                    }
                    else if (data.result == true) {
                        alert("注册成功！！！");
						$(location).attr('href','/home');
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

});





