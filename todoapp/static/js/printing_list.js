var res;

$('#create').click(function(){
    createlist="<form id = 'form1' method='POST'><table><tr><td>Name</td><td><input type='text' id='n'></td></tr><tr><td>date</td><td><input type='date' id='d'></td></tr><tr><td><button id='submit'>Submit</button></td></tr></table></form>"
    $('#lists')[0].innerHTML="";
    $('#lists').append(createlist);

    $('body').on('click','#submit',function(){
    console.log("Enterd ")
    obj={};
    console.log($('#n').val())
    obj['name']=$('#n').val()
    console.log($('#d').val())
    obj['createdDate'] = $('#d').val()
    obj['user'] = res[0].user;

    console.log("hello");
    console.log(obj)
    $.ajax({url:'/todo/todoLists/',
        type: 'POST',
        content:'application/json',
        data: obj,
        dataType:'json',
        success:function(result){
            $('#lists').append('<h3>List Created Successfully</h3><h3>Click Show Lists to display Lists');
        }
    })

});
});




$('#btn').click(function(){
    $.ajax({ url:'http://localhost:8000/online/printtodolist_using_serializers/',
            method:'GET',
            success: function(result){
            res = result;
                var markup = "<li id='${id}' class='todolist'> ${name} (${createddate})</li><br>"
                $.template('temp',markup);
                $.tmpl('temp',result).appendTo('#lists');
            }
    });


});




$('body').on('click', '.todolist', function(){

    id=$(this).id;
    console.log("id is "+id)
    $.ajax({

        url:'http://localhost:8000/online/printtodoitem_using_serializers/'+(id),
        method : "GET",
        success : function(result){

            console.log(result)
            var markup = "<li id='${id}'><b>${description}</b>(${completed})</li>";

            $.template("item", markup);
            console.log($('#items'));
            $('#items')[0].innerHTML = ""
            $.tmpl("item", result).appendTo("#items");
        }
    });
});

