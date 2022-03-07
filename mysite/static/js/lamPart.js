// 生成求解过程中的通用过程的函数

function GEPart(data, ele) {
    let content = '$A$';
    content += data.course.map(x => `$ \\rightarrow ${x} $`).join('');
    createDefaultPanel(ele, content);
}