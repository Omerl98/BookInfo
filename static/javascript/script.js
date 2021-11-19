
function search_book() {
    let input = document.getElementById('searchbar').value;
    input=input.toLowerCase();
    let y = document.getElementsByClassName('media');
    for (i = 0; i < y.length; i++) {
        let title = y[i].getElementsByClassName('book-title');
        if (!title[0].innerHTML.toLowerCase().includes(input)) {
            y[i].style.display="none";
    
        }
        else {
            y[i].style.display="flex";                 
        }
    }
}

function search_by_author() {
    let input = document.getElementById('searchbar').value;
    input=input.toLowerCase();
    let y = document.getElementsByClassName('media');
    for (i = 0; i < y.length; i++) {
        let title = y[i].getElementsByClassName('authors');
        if (!title[0].innerHTML.toLowerCase().includes(input)) {
            y[i].style.display="none";
    
        }
        else {
            y[i].style.display="flex";                 
        }
    }
}

function search_by_publisher() {
    let input = document.getElementById('searchbar').value;
    input=input.toLowerCase();
    let y = document.getElementsByClassName('media');
    for (i = 0; i < y.length; i++) {
        let title = y[i].getElementsByClassName('publisher');
        if (!title[0].innerHTML.toLowerCase().includes(input)) {
            y[i].style.display="none";
    
        }
        else {
            y[i].style.display="flex";                 
        }
    }
}

function author_button() {
    document.getElementById('myDropdown').innerHTML = "Search by author";
    //document.getElementById('search-btn').onclick = function() {search_by_author()} ;
    document.getElementById('search-btn').setAttribute( "onClick", "javascript: search_by_author();" );
}

function title_button() {
    document.getElementById('myDropdown').innerHTML = "Search by title";
    document.getElementById('search-btn').setAttribute( "onClick", "javascript: search_book();" );
}

function publisher_button() {
    document.getElementById('myDropdown').innerHTML = "Search by publisher";
    document.getElementById('search-btn').setAttribute( "onClick", "javascript: search_by_publisher();" );

}
    
