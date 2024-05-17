//load movies list evertime the page loads
document.onload = GetMovies();


function AddMovie(){
    var movie = document.getElementById('name').value;
    //??

    fetch('http://localhost:5000/movies', {
        method: "POST",
        body: JSON.stringify({
            name: movie,
            year: year,
            rating: rating
        }),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(function(response){
        return response.json();
    })
    .then((json) => {
        alert(json.status)
        ClearTable();
        GetMovies();

    })
}

function GetMovies(){
    fetch('http://localhost:5000/movies', {
        method: "GET",
        headers:{
            'Content-Type': 'application/json'
        }
        
    }).then(function(response){
        return response.json();
    })
    .then((json) => { 
        movies = json.movies;

        ClearTable();
        CreateMovieRows(movies);
    }

    );
}


function CreateMovieRows(movies){
    movies.forEach(movie => {
        //add code to create a table row for each movie
        //??
    });
}


function ClearTable(){
    var table = document.getElementById('movies');
    var rowCount = table.rows.length;
    for (var i = rowCount - 1; i > 0; i--) {
        table.deleteRow(i);
    }
}