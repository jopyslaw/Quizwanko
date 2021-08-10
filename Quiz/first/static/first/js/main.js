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

function login_validate()
{
    var username = document.getElementById("register_username").value;
    var password = document.getElementById("register_password").value;
    var reg = new RegExp("[^A-Za-z0-9]")
    if(username.search(reg))
    {
        console.log("It's working");
    }
    else
    {
        console.log("It's not working properly");
    }

}
