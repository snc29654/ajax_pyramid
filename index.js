$(function(){
    $("button").click(function(){
        $.ajax({
            url:'./cgi-bin/sample.py',
            type:'POST',
            data:{sent:"test"}
        })
        .done(function(data){
                var smp=document.getElementById("inbox");
                smp.innerHTML = data;
        })
        .fail(function(){
        var smp=document.getElementById("inbox");
        smp.innerHTML = "failed";
});
    });
});
