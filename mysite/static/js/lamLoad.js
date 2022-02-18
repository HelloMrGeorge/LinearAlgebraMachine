function loadLinequData(data, ele) {

    createPanel(ele).text(`$AX = b，$其中$A=${data.mat}$，$b=${data.vec}$，记增广矩阵$C = (A, b)$`);

    let course = '$A$';
    for(let i = 0; i < data.elimination_course.length; i++) {
        course = course + `$\\rightarrow ${data.elimination_course[i]}$`;
    }
    createPanel(ele).text(course);;
    
    if(data.solveset.length <= 0) {
        createPanel(ele).text('无解');
    } else {
        course = '';
        for(let i = 0; i < data.solveset.length; i++) {
            course = course + `x_${i+1} = & ${data.solveset[i]} \\\\`;
        }
        course = `$\\left\\{\\begin{matrix} ${course.substring(0, course.length - 3)} \\end{matrix}\\right.$`;
        createPanel(ele).text(course);
    }
}

function loadLambdaLinData(data, ele) {

    function creatRootCourse(data, i) {
        // 每行生成每个根的解方程过程
        
    
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
    
        createPanel(ele).text(course);

        createTogglePanel(ele, `solve${i}`, '展开详细解方程过程', '')
        loadLinequData(data.LQS_list[i], $(`#solve${i}`));
    }

    createPanel(ele).text(`$AX = b$，其中$A=${data.mA}$，$b=${data.mb}$，记增广矩阵$C = (A, b)$`);

    createPanel(ele).text(`$|A| = ${data.determinat} = ${data.factorization}$`);

    let course = '解方程$|A| = 0$，';
    if(data.root.length == 0) {
        course += '得方程无解，故原方程有唯一解'
        createPanel(ele).text(course);
    } else {
        course += '存在根'
        for(let i = 0; i < data.root.length; i++) {
            course += `,$${data.lam}_{${i+1}} = ${data.root[i]}$`;
        }
        createPanel(ele).text(course);

        for(let i = 0; i < data.root.length; i++) {
            creatRootCourse(data, i)
        }
    }

    course = ''
    for(let i = 0; i < data.LQS_nozero.solveset.length; i++) {
        course += `x_${i+1} = & ${data.LQS_nozero.solveset[i]} \\\\`;
    }
    course = `当$|A|=0$时，有唯一解： $$\\left\\{\\begin{matrix} ${course.substring(0, course.length-3)} \\end{matrix}\\right.$$`;
    createPanel(ele).text(course);

    createTogglePanel(ele, `solve_nozero`, '展开详细解方程过程', '')
    loadLinequData(data.LQS_nozero, $(`#solve_nozero`));
}