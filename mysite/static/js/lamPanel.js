function createPanel(ele) {
    // 生成一个面板，用于显示一行解题过程
    // ele是面板所在的html元素

    let layer1 = $('<div class="panel panel-default"></div>');
    let layer2 = $('<div class="panel-body"></div>');
    let layer3 = $('<p></p>');

    $(ele).append(layer1);
    layer1.append(layer2);
    layer2.append(layer3);

    return layer3
}

function createButtonPanel(ele) {
    // 生成一个带按钮面板
    // ele是面板所在的html元素

    let layer1 = $('<div class="panel panel-default"></div>');
    let layer2 = $('<div class="panel-body"></div>');
    let layer3 = $('<div class="row"></div>');
    let layer4 = $('<div class="col-md-10"></div>');
    let layer5 = $('<div class="col-md-2"></div>');
    let layer6 = $('<p></p>');
    let layer7 = $('<button class="btn btn-default"></button>');

    $(ele).append(layer1);
    layer1.append(layer2);
    layer2.append(layer3);
    layer3.append(layer4);
    layer3.append(layer5);
    layer4.append(layer6);
    layer5.append(layer7);

    return [layer6, layer7];
}