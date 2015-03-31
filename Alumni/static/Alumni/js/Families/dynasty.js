
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
    ['Imee Chan'',''],'
['Daniel Kim'',''],'
['Melanie Mui'',''],'
['Anna Ly'',''Anna Ly'' ',' ',],
['Lu Zhang'',''Lu Zhang'' ',' ',],
['Jason Ma'',''Jason Ma'' ',' ',],
['Konstantin Vidensky'',''Konstantin Vidensky'' ',' ',],
['Hugo Zhang'',''Hugo Zhang'' ',' ',],
['Alvin Poh'',''],'
['Stephanie Yue'',''Stephanie Yue'' ',' ',],
['Ahmad Shamsuddin'',''Ahmad Shamsuddin'' ',' ',],
['Zachary Rousselle'',''Zachary Rousselle'' ',' ',],

    )];

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }
    