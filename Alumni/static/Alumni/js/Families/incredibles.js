function Incredibles() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['Samiah Akhtar','',''],
['Arish Gupta','',''],
['Rona Song','',''],
['Brian Loo','Arish Gupta',''],
['Linda Min','Brian Loo',''],
['Salman Khoja','Salman Khoja',''],
['Eric Tang','',''],
['Alex Voo','Salman Khoja',''],
['Steven Yi','Linda Min',''],
['David Leong','David Leong',''],
['Andrew Yi','Linda Min',''],
['Billy Litner','Brian Loo',''],
['Bin Yang','Salman Khoja',''],
['Kent Yeung','David Leong',''],
['Victoria Docherty','David Leong',''],
['Hyejoo Kim','Kent Yeung',''],
['Yeonjoo Kim','',''],
['Stephanie Schneider','Billy Litner',''],
['Gina Seguiti','Bin Yang',''],
['Yinglu Yao','Victoria Docherty',''],
['Vince Ye','Andrew Yi',''],
['Arthur Hong','Billy Litner',''],
['Elise Lim','Stephanie Schneider',''],
['Dorothy Yu','Yeonjoo Kim',''],
['Christine Pak','Christine Pak',''],
['Mia Wang','Vince Ye',''],
['Andrew Gumbs','Mia Wang',''],

    ]);

    var chart = new google.visualization.OrgChart(document.getElementById('incredibles_tree'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }}
    