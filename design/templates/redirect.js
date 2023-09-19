<script type="text/javascript">
$('.goToWW').click(function(){
$.ajax(
{
    type:"GET",
    url: "/getValue/",
    data:{
        csrfmiddlewaretoken:'{{csrf_token}}',
        'xx':'xx3'
    },
    success: function( data ) 
    {
        alert("ben çalıştım")
        window.location.href="/ww"
        console.log(data)
        alert(data)

    }
    
 })
});
</script>