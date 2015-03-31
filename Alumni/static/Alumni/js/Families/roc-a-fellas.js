
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
    ['Malcolm Ong'',''],'
['Danielle Rosenfeld'',''Danielle Rosenfeld'' ',' ',],
['Brenda Lee'',''Brenda Lee'' ',' ',],
['Johnny Bae'',''Johnny Bae'' ',' ',],
['Matt Wilson'',''Matt Wilson'' ',' ',],
['Emily Wright'',''Emily Wright'' ',' ',],

    )];

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }
    