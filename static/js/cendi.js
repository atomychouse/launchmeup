

params = localStorage.getItem('idea');
params = JSON.parse(params);

(function($) {

$('.fa-plus-circle').click(function(e){
    e.preventDefault();
    var hereis = $(this).parents('div:first');
    $(this).siblings('textarea:first').clone().appendTo(hereis);
});
    
$('.saver').click(function(){
    idea = {
        name:$("[name='idea_name']").val()
    };
    ideaval = JSON.stringify(idea);
    localStorage.setItem('idea', ideaval);
});


try{
    $('.tit').html(params.name);
    $('[name="idea_name"]').val(params.name);
}
catch(err){
    var pas = null;
}

$('.carousel').carousel()


}(jQuery));