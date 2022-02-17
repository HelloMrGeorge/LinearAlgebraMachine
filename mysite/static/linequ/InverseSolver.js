const csrftoken = docCookies.getItem('csrftoken');
const btn = document.getElementById('submit');

function myCatch(value) {
    var myInit = { 
        method: 'POST',
        mode: 'cors',
        headers: {'X-csrftoken':csrftoken},
        body: JSON.stringify({matrix: value}),
    };
    var myRequest = new Request(SolverUrl, myInit); 
    fetch(myRequest)
    .then(response => response.json())
    .then(data => {
        console.log(data);

        document.getElementById('start').innerHTML = `$${data.mat}$`;
        document.getElementById('start_area').hidden = false;

        let course = '$A$';
        for(let i = 0; i < data.course.length; i++) {
          course = course + `$\\rightarrow ${data.course[i]}$`;
        }
        course = `${course}`
        document.getElementById('course').innerHTML = course;
        document.getElementById('course_area').hidden = false;

        document.getElementById('result').innerHTML = `所以$A^{-1} = ${data.inv}$`;
        document.getElementById('result_area').hidden = false;

        MathJax.typeset();
    });
}

btn.addEventListener('click', () => {
    var matrix = document.getElementById('matrix').value;
    myCatch(matrix);
})
