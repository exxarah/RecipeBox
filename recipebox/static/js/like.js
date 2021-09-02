var like_button = document.getElementsByClassName('like-button-request')[0]
var like_label = document.getElementsByClassName('like-button-label')[0]
like_button.addEventListener('click', likeRequest)
var httpRequest;

function likeRequest() {
    httpRequest = new XMLHttpRequest();

    if(!httpRequest) {
        alert('Cannot create an XMLHTTP instance T_T')
        return false;
    }
    httpRequest.onreadystatechange = alertContents;
    httpRequest.open('GET', 'liked_by')
    httpRequest.send();
}

function alertContents(){
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
            // Do Something With the Response
            var jsonResponse = JSON.parse(httpRequest.responseText)
            if (!jsonResponse["liked"])
                like_button.getElementsByTagName('i')[0].classList.remove('selected')
            else
                like_button.getElementsByTagName('i')[0].classList.add('selected')

            // Update label text
            like_label.textContent = jsonResponse["num_likes"]
        } else {
            alert('There was a problem with the request')
        }
    }
}