$(document).ready(function () {

    $("#bt1").click(function (){
        var UserName = $("#username").val();
        var Password1 = $("#pw1").val();
        var Password2 = $("#pw2").val();
        if (UserName.length < 4 || UserName.length > 10) {
            alert("用户名输入不符合规范");
        }
        else if (Password1.length < 4 || Password1.length > 20) {
            alert("密码输入不符合规范");
        }
        else if (Password1 !== Password2) {
            alert("两次密码输入不一致");
        }
    });
});





