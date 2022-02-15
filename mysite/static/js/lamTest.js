var csrftoken = docCookies.getItem('csrftoken');
var textarea = document.getElementById('text');
const btn = document.getElementById('btn');


function mycatch() {

    let myInit = { 
        method: 'POST',
        mode: 'same-origin',
        headers: {'X-csrftoken':csrftoken},
        body: JSON.stringify({matrix: 'matrix'}),
    };

    fetch(new Request(SolverUrl, myInit))
    .then(response => response.json())
    .then(data => {
        console.log(data);
        textarea.innerHTML = '已接收';
    });
}


$("#btn").click(mycatch);
