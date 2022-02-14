const csrftoken = docCookies.getItem('csrftoken');
const btn = document.getElementById('submit');
const root_course_area = document.getElementById('root_course_area');

function creatRootCourse(data, i) {
    // 每行生成每个根的解方程过程

    let ls = creatButtonPanel(root_course_area);
    let content = ls[0];
    let btn = ls[1];

    let course = `当$ ${data.lam} = ${data.root[i]}$时，`;
    if(data.LQS_list[i].solveset.length == 0) {
        course += `$Rank(A)=${data.rank[i][0]}, Rank(C)=${data.rank[i][1]}$，所以无解`
    } else {
        course += `$Rank(A)=Rank(C)=${data.rank[i][0]}$，`
        let solveset = ''
        for(let j = 0; j < data.LQS_list[i].solveset.length; j++) {
            solveset += `x_${j+1} = & ${data.LQS_list[i].solveset[j]} \\\\`;
        }
        course += `解得$\\left\\{\\begin{matrix} ${solveset.substring(0, solveset.length-3)} \\end{matrix}\\right.$`;
    }

    content.innerHTML = course;
    btn.innerHTML = '详解';
}

function creatButtonPanel(ele) {
    // 生成一个带按钮的面板，用于显示一行解题过程
    // ele是面板所在的html元素
    let layer1 = document.createElement('div');
    let layer2 = document.createElement('div');
    let layer3 = document.createElement('div');
    let layer4 = document.createElement('div');
    let layer5 = document.createElement('div'); //layer1-3从外到内，4,5并列

    layer1.className = 'panel panel-default';
    layer2.className = 'panel-body';
    layer3.className = 'row';
    layer4.className = 'col-md-10';
    layer5.className = 'col-md-2';

    ele.appendChild(layer1);
    layer1.appendChild(layer2);
    layer2.appendChild(layer3);
    layer3.appendChild(layer4);
    layer3.appendChild(layer5);

    let btn = document.createElement('button');
    btn.className = 'btn btn-default';
    layer5.appendChild(btn);

    return [layer4, btn]
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

        document.getElementById('start').innerHTML = `$AX = b$，其中$A=${data.mA}$，$b=${data.mb}$，记增广矩阵$C = (A, b)$`;
        document.getElementById('start_area').hidden = false;

        document.getElementById('deter').innerHTML = `$|A| = ${data.determinat} = ${data.factorization}$`;
        document.getElementById('deter_area').hidden = false;

        let course = '解方程$|A| = 0$，';
        if(data.root.length == 0) {
            course += '得方程无解，故原方程有唯一解'
            document.getElementById('root').innerHTML = course;
            document.getElementById('root_area').hidden = false;
        } else {
            course += '存在根'
            for(let i = 0; i < data.root.length; i++) {
                course += `,$${data.lam}_{${i+1}} = ${data.root[i]}$`;
            }
            document.getElementById('root').innerHTML = course;
            document.getElementById('root_area').hidden = false;

            for(let i = 0; i < data.root.length; i++) {
                creatRootCourse(data, i)
            }
            
        }

        course = ''
        for(let i = 0; i < data.LQS_nozero.solveset.length; i++) {
            course += `x_${i+1} = & ${data.LQS_nozero.solveset[i]} \\\\`;
        }
        course = `当$|A|=0$时，有唯一解： $$\\left\\{\\begin{matrix} ${course.substring(0, course.length-3)} \\end{matrix}\\right.$$`;
        document.getElementById('nozero').innerHTML = course;
        document.getElementById('nozero_area').hidden = false;

        MathJax.typeset();
    });
}

btn.addEventListener('click', () => {
    // 先删除先前js生成的元素
    var childs = root_course_area.childNodes; 
    for(var i = childs.length - 1; i >= 0; i--) { 
        root_course_area.removeChild(childs[i]); 
    }

    var matrix = document.getElementById('matrix').value;
    myCatch(matrix);
})
