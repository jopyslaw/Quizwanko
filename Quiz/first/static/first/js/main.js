function send_form(form)
{
    form = document.getElementById("quiz_form");
    var user_choice = confirm("Czy na pewno chcesz zakończyć Quiz ?");
    if(user_choice)
    {
        return form.confirm();
    }
    else
    {
        return false;
    }
}