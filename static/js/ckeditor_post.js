$(document).ready(function(){
    $('.edit-text').click(function () {
        var btn = $(this);
        if (btn.hasClass('edit-text')){
            btn.parent().children('.editable-text').css('opacity', '1');
            btn.parent().children('.not-editable-text').hide();
            btn.removeClass('edit-text').addClass('save-text');
        }
        else{
            var data_info = btn.attr('data-info');
            var html = btn.parent().children('.editable-text').html();


            $.ajax({
                url: '',
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': csrf,
                    'data_info': data_info,
                    'namerequest':'editable_text',
                    'text': html
                },
                dataType: 'json',
                success: function (response) {
                    if (response.status == true) {
                        console.log('Данные успешно сохранены');
                        btn.parent().children('.editable-text').css('opacity', '0');
                        btn.parent().children('.not-editable-text').show();
                        btn.parent().children('.not-editable-text').html(response.text);
                        btn.removeClass('save-text').addClass('edit-text');
                        console.log(response.text);
                    } else {
                        console.log('Не удалось сохранить текст, пожалуйста повторите попытку')
                    }
                },
                error: function (response) {
                    console.log('Не удалось сохранить текст, пожалуйста повторите попытку')
                }
            });

        }
    });
});