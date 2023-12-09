function optionUrl(option) {
/** 
 * SORT - function to retrieve the URL from a selected option and redirect to the url
 * URL is stored from selected option
 * Extracted URL is used to redirect the user to the selected option URL
 */
    let selectedOption = option.options[option.selectedIndex];
    let url = selectedOption.dataset.url;
    if (url) {
        window.location.href = url;
    }
}
