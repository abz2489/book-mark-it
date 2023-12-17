// Update quantity on click
$('.update-link').click(function(event) {
    let form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function(event) {
    let csrfToken = "{{ csrf_token }}";
    let url = `/basket/remove/${bookId}`;
    let data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
    .done(function() {
        location.reload();
    });
})