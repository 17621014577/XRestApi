
// 通用的AJAX操作，请求URL，请求数据为data_user，成功和失败分别调用不同的函数
function normal_ajax(url , data_user , succ_callback , fail_callback){

    $.ajax({    url         : url,
                type        : "GET",
                data        : data_user ,
                dataType    : "json",
                success     : function (data) {
                                if (typeof(succ_callback) == 'function')
                                    succ_callback(data)
                              } ,
                error       : function (data) {
                                if (typeof(fail_callback) == 'function')
                                    fail_callback(data)
                              }
    });
}



$.ajaxSetup({
  	headers: {'Authorization': get_token()}
});

function get_token(){
	var storage= getCookie('jwt_token');
	return storage ? 'jwt ' + storage : "";
}


function getCookie(name)
{
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");

    if(arr=document.cookie.match(reg))

        return unescape(arr[2]);
    else
        return '';
}