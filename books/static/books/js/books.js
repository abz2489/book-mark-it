function optionUrl(option) {
/** 
 * SORT - function to retrieve the URL from a selected option and redirect to the url
 * URL is stored from selected option
 * extracted URL is used to redirect the user to the selected option URL
 */
    let selectedOption = option.options[option.selectedIndex];
    let url = selectedOption.dataset.url;
    if (url) {
        window.location.href = url;
    }
}

function handleEnableDisable(bookId) {
    let currentValue = parseInt($(`#id_qty_${bookId}`).val());
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 19;
    $(`#decrement-qty_${bookId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${bookId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
let allQtyInputs = $('.qty_input');
for(let i = 0; i < allQtyInputs.length; i++){
    let bookId = $(allQtyInputs[i]).data('book_id');
    handleEnableDisable(bookId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    let bookId = $(this).data('book_id');
    handleEnableDisable(bookId);
});

// Increment quantity
$('.increment-qty').click(function(event) {
    event.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let bookId = $(this).data('book_id');
    handleEnableDisable(bookId);
});

 // Decrement quantity
$('.decrement-qty').click(function(event) {
    event.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let bookId = $(this).data('book_id');
    handleEnableDisable(bookId);
});