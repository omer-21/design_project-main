<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>;



   $('.Design').click(function(){
   $.ajax(
   {
       type:"POST",
       url: window.location.href,
       data:{
           csrfmiddlewaretoken:'{{csrf_token}}',
           'dn':getPostData(window.location.href)
       },
       success: function( data ) 
       {
           window.location.href="/dn"
       }
       
    })
   });

$('.goToWW').click(function(){
$.ajax(
{
   type:"POST",
   url: window.location.href,
   data:{
       csrfmiddlewaretoken:'{{csrf_token}}',
       'ww':getPostData(window.location.href)
   },
   success: function( data ) 
   {
       window.location.href="/ww"
   }
   
})
});

$('.goToSW').click(function(){
$.ajax(
{
   type:"POST",
   url: window.location.href,
   data:{
       csrfmiddlewaretoken:'{{csrf_token}}',
       'sw':getPostData(window.location.href)
   },
   success: function( data ) 
   {
       window.location.href="/sw"
   }
   
})
});

$('.goToCW').click(function(){
$.ajax(
{
   type:"POST",
   url: window.location.href,
   data:{
       csrfmiddlewaretoken:'{{csrf_token}}',
       'cw':getPostData(window.location.href)
   },
   success: function( data ) 
   {
       window.location.href="/cw"
   }
   
})
});

$('.goToLD').click(function(){
$.ajax(
{
   type:"POST",
   url: window.location.href,
   data:{
       csrfmiddlewaretoken:'{{csrf_token}}',
       'ld':getPostData(window.location.href)
   },
   success: function( data ) 
   {
       window.location.href="/ld"
   }
   
})
});

$('.goToEx').click(function(){
//const url = window.location.href
var exdata=getPostData(window.location.href)
$.ajax(
{
   type:"POST",
   url: window.location.href,
   data:{
       csrfmiddlewaretoken:'{{csrf_token}}',
       'ex':exdata,
   },
   success: function( data ) 
   {
       window.location.href="/ex"
   }
   
})
});
function getdn() {return 'dn'}
function getww() {return 'ww'}
function getsw() {return 'sw'}
function getcw() {return 'cw'}
function getld() {return 'ld'}
function getex() {return  document.getElementById('exn').value}


function getPostData(url) {
    const urlList=window.location.href.split('/')
    const goal = urlList[urlList.length-2 ]
    console.log(goal)
    if (goal=='dn') {return getdn()}
    else if(goal=='ww'){return getww()}
    else if(goal=='sw'){return getsw()}
    else if(goal=='cw'){return getcw()}
    else if(goal=='ld'){return getld()}
    else if(goal=='ex'){return getex()}
    else{return 'error'}


}
