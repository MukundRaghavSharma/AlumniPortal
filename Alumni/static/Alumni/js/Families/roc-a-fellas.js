function Roc-a-fellas() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['Malcolm Ong','',''],
['Danielle Rosenfeld','Julia Degeratu','',''],
['Brenda Lee','Hayden Tang','',''],
['Johnny Bae','Charles Mbaruguru','',''],
['Matt Wilson','Julia Choicer','',''],
['Emily Wright','Emily Wright','',''],

    ]);

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }}
    