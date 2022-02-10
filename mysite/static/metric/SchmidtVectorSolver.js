const csrftoken = docCookies.getItem('csrftoken');
const btn = document.getElementById('submit');
const course_area = document.getElementById('course_area');

function create_courese(data, i) {
  // 生成每行求正交向量的过程
  let outerdiv = document.createElement('div');
  let innerdiv = document.createElement('div');
  outerdiv.className = 'panel panel-default';
  innerdiv.className = 'panel-body';
  outerdiv.appendChild(innerdiv);

  let course = `\\varepsilon_{${i+1}} = \\alpha_{${i+1}}`;
  for(let j = 0; j < i; j++) {
    course = course + `- \\frac{(\\alpha_{${i+1}}, \\varepsilon_{${j+1}})}{(\\varepsilon_{${i+1}}, \\varepsilon_{${j+1}})} \\varepsilon_{${j+1}}`;
  }
  course = course + `= \\alpha_{${i+1}}`;
  for(let j = 0; j < i; j++) {
    if (data.coef[i][j].charAt(0) == '-') {
      // 防止出现连续的两个负号
      course = course + `+ ${data.coef[i][j].substring(1)}\\varepsilon_{${j+1}}`;
    } else {
      course = course + `- ${data.coef[i][j]}\\varepsilon_{${j+1}}`;
    }
    
  }
  course = course + `= ${data.vecs[i]}`;
  innerdiv.innerHTML = `$$${course}$$`;

  course_area.appendChild(outerdiv);
}

function myCatch(value) {
  var myInit = { 
    method: 'POST',
    mode: 'cors',
    headers: {'X-csrftoken':csrftoken},
    body: JSON.stringify({matrix: value}),
  };
  // 外部js中引用链接要么直接用地址，要么提前在html文件中把链接赋值给一个变量
  var myRequest = new Request("/metric/SchmidtVectorSolver", myInit); 
  fetch(myRequest)
  .then(response => response.json())
  .then(data => {
    console.log(data);

    let course = '';
    for(let i = 0; i < data.mat.length; i++) {
      course = course + `\\alpha_{${i+1}} = ${data.mat[i]},`;
    }
    document.getElementById('start_vector').innerHTML = `初始向量：$${course.substring(0, course.length - 1)}$`;
    document.getElementById('start_area').hidden = false;

    for(let i = 0; i < data.vecs.length; i++) {
      create_courese(data, i)
    }

    course = '';
    for(let i = 0; i < data.norm_vecs.length; i++) {
      course = course + `\\varepsilon_{${i+1}}' = ${data.norm_vecs[i]},`;
    }
    document.getElementById('norm_vector').innerHTML = `单位化后得：$${course.substring(0, course.length - 1)}$`;
    document.getElementById('norm_area').hidden = false;

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
