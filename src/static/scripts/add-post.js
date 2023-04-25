document.addEventListener("keypress", function (e) {
    if (e.keyCode === 13 || e.which === 13) {
        e.preventDefault();
        return false;
    }

})
const URL = '/add-hashtag';
//const URL = '/add-post';
let hashtagInput = document.querySelector('#hashtag-input');
let hashtagsContainer = document.querySelector('.hashtags-container');

if (hashtagInput) {
    hashtagInput.addEventListener("keypress", function (event) {
        if (event.keyCode === 13 && hashtagInput.value.length > 0) {
            let hashValue = (hashtagInput.value);
            let hashText = document.createTextNode(hashValue);
            let hashParagraph = document.createElement('p');
            hashtagsContainer.appendChild(hashParagraph);
            hashParagraph.appendChild(hashText);
            hashParagraph.classList.add('hashtagEl');
            hashParagraph.name = 'hashtagEl';
            hashtagInput.value = '';

            let request_options = {
                method: "POST",
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify({
                    hashtag: hashValue
                })
            }

            fetch(URL, request_options)
                .then(response => console.log(response.json()))
                .catch((err) => console.log(err))
        }
    });
}