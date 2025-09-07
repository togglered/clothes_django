function open_link_with_params(params, values) {
	if (window.history && history.pushState) {
		history.pushState({foo: 'bar'}, 'Title', location.href.replace(location.hash,''));
	}
	const currentUrl = new URL(window.location.href);
	for (let i = 0; i < params.length; i++) {
		currentUrl.searchParams.set(params[i], values[i]);
	}
	window.location.href = currentUrl;
}

const urlString = window.location.href;
const url = new URL(urlString);

const selectElement = document.querySelector('#sort-select');
if (selectElement) {
  const options = selectElement.options;
  const showed = url.searchParams.get('sorted');
  if (showed) {
    for (let i = 0; i < selectElement.length; i++) {
      options[i].removeAttribute('selected');
      if (options[i].value == showed) {
        options[i].setAttribute('selected', 'selected')
      }
    }
  }
}