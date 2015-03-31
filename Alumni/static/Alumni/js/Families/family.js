
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
    ['Patrick Cao'',''],'
['Julian Chun'',''],'
['Chris Chyu'',''],'
['Andrew Kiang'',''],'
['Jennifer Suh'',''],'
['Jessica Wong'',''Jessica Wong'' ',' ',],
['Niharika Bandi'',''],'
['Xiao-Lan Wong'',''Xiao-Lan Wong'' ',' ',],
['Sheldon Cheung'',''Sheldon Cheung'' ',' ',],
['Daniel Chen'',''Daniel Chen'' ',' ',],
['Shi Chung'',''],'
['William Ouyang'',''William Ouyang'' ',' ',],
['Neil Sethi'',''Neil Sethi'' ',' ',],
['Christopher Jo'',''Christopher Jo'' ',' ',],
['Deniz Kalaycioglu'',''Deniz Kalaycioglu'' ',' ',],
['Vincent Liu'',''Vincent Liu'' ',' ',],
['Bernard Yuan'',''Bernard Yuan'' ',' ',],
['Adhip Sacheti'',''Adhip Sacheti'' ',' ',],
['Raphael Kim'',''Raphael Kim'' ',' ',],

    )];

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }
    