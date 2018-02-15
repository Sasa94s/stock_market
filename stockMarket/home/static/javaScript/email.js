$(document).ready(function() {
    (function() {
        var message = "{% trans 'Do you really want to remove the selected e-mail address?' %}";
        var actions = document.getElementsByName('action_remove');
        if (actions.length) {
            actions[0].addEventListener("click", function(e) {
                if (!confirm(message)) {
                    e.preventDefault();
                }
            });
        }
    })();
});