const csrftoken = docCookies.getItem('csrftoken');
const btn = document.getElementById('submit');
const course_area = document.getElementById('course_area');

function create_courese(data, i) {
    // 生成每行验证线性相关的过程
    let outerdiv = document.createElement('div');
    let innerdiv = document.createElement('div');
    outerdiv.className = 'panel panel-default';
    innerdiv.className = 'panel-body';
    outerdiv.appendChild(innerdiv);

    let course = '';
    for(let j = 0; j < i; j++) {
        if(data.position.indexOf(j) != -1) {
            course = course + `\\alpha_{${j+1}}, `;
        }
    }
    course = course + `\\alpha_{${i+1}}`;

    if(data.position.indexOf(i) != -1) {
        course = `向量组$(${course})$线性无关；`;
    } else {
        course = `向量组$(${course})$线性相关，因为`;
        
        let equ = `${data.coef[i-1][0]}\\alpha_{${1}}`;
        let n = 1; //给系数的位置计数
        for(let j = 1; j < i; j++) {
            if(data.position.indexOf(j) != -1) {
                if(data.coef[i-1][n].charAt(0) == '-') {
                    // 防止出现连续的两个正负号
                    equ = equ + `${data.coef[i-1][n]}\\alpha_{${j+1}}`;
                } else {
                    equ = equ + `+ ${data.coef[i-1][n]}\\alpha_{${j+1}}`;
                }
                n++;
            }
        }
        equ = `$${equ}= \\alpha_{${i+1}}$`;
        course = course + equ;
    }

    innerdiv.innerHTML = course;
    course_area.appendChild(outerdiv);
}

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

        let course = '';
        for(let i = 0; i < data.group.length; i++) {
            course = course + `\\alpha_{${i+1}} = ${data.group[i]},`;
        }
        document.getElementById('start_vector').innerHTML = `初始向量：$${course.substring(0, course.length - 1)}$`;
        document.getElementById('start_area').hidden = false;

        for(let i = 1; i < data.group.length; i++) {
            create_courese(data, i)
        }

        course = '';
        for(let i = 0; i < data.group.length; i++) {
            if(data.position.indexOf(i) != -1) {
                course = course + `\\alpha_{${i+1}} = ${data.group[i]},`;
            }
        }
        document.getElementById('result_vector').innerHTML = `综上，极大线性无关组：$${course.substring(0, course.length - 1)}$`;
        document.getElementById('result_area').hidden = false;

        MathJax.typeset();
    });
}

btn.addEventListener('click', () => {
  // 先删除先前js生成的元素
    var childs = course_area.childNodes; 
    for(var i = childs.length - 1; i >= 0; i--) { 
        course_area.removeChild(childs[i]); 
    }

    var matrix = document.getElementById('matrix').value;
    myCatch(matrix);
})
