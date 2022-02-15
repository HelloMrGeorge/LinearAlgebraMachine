const csrftoken = docCookies.getItem('csrftoken');
const btn = document.getElementById('submit');

btn.addEventListener('click', () => {
    $('#coures_area').empty()
    myCatch(document.getElementById('matrix').value);
})

function myCatch() {
    var myInit = { 
        method: 'POST',
        mode: 'cors',
        headers: {'X-csrftoken':csrftoken},
        body: JSON.stringify({matrix: value}),
    };

    fetch(new Request(SolverUrl, myInit))
    .then(response => response.json())
    .then(data => LinequCourse(document.getElementById('coures_area'), data));
}


function createPanel(ele) {
    // 生成一个面板，用于显示一行解题过程
    // ele是面板所在的html元素
    let layer1 = document.createElement('div');
    let layer2 = document.createElement('div');

    layer1.className = 'panel panel-default';
    layer2.className = 'panel-body';

    ele.appendChild(layer1);
    layer1.appendChild(layer2);

    return layer2
}

function LinequCourse(ele, data) {
    let start = createPanel(ele);
    start.innerHTML = `$AX = b，$其中$A=${data.mat}$，$b=${data.vec}$，记增广矩阵$C = (A, b)$`;

    let middle = createPanel(ele);
    let course = '';
    for(let i = 0; i < data.elimination_course.length; i++) {
        course = course + `$\\rightarrow ${data.elimination_course[i]}$`;
    }
    middle.innerHTML = course;

    let result = createPanel(ele);
    course = '';
    if(data.solveset.length <= 0) {
        result.innerHTML = '无解';
    } else {
        for(let i = 0; i < data.solveset.length; i++) {
        course = course + `x_${i+1} = & ${data.solveset[i]} \\\\`;
        }
        course = course.substring(0, course.length - 3)
        course = `$\\left\\{\\begin{matrix} ${course} \\end{matrix}\\right.$`;
        result.innerHTML = course;
    }

    MathJax.typeset();
}