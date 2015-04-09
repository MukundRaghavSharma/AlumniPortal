function Boss() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['<a href="/profile/14444"> Mukund Sharma','',''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('boss_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        