$(document).ready(llamadaApi);



    function llamadaApi(){
    $.ajax({

        url: 'https://finnhub.io/api/v1/forex/symbol?exchange=oanda&token=c1do2a748v6peb0l695g',
        type: 'get',
        dataType: 'json',
        headers: { 
            //'Access-Control-Allow-Origin':'*',
            // 'X-Finnhub-Token' : 'sandbox_c1dk6ff48v6tbf1bn360'
        
        }, 

        success: function(data) {
            console.log(data)


        },
    });
}











/* 
    fetch(url,{
        method: 'get',
        headers: {
            'Content-Type' : 'application/json' ,   
            'Access-Control-Allow-Origin':'*',  
        }
    })
    .then(function(response){

        console.log(response.data);

    })
        .catch(function(error) {
                alert("Invalid user"+ error);
            });

}
callApy();
 */










