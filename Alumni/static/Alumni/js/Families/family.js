function Family() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	       ['Julian Chun','',''],
            ['Chris Chyu','',''],
            ['Andrew Kiang','',''],
            ['Patrick Cao','',''],
            ['Jennifer Suh','',''],
            ['Jessica Wong','Jennifer Suh',''],
            ['Niharika Bandi','',''],
            ['Xiao-Lan Wong','Patrick Cao',''],
            ['Sheldon Cheung','Xiao-Lan Wong',''],
            ['Daniel Chen','Jessica Wong',''],
            ['Shi Chung','',''],
            ['William Ouyang','Jessica Wong',''],
            ['Neil Sethi','Niharika Bandi',''],
            ['Christopher Jo','Shi Chung',''],
            ['Deniz Kalaycioglu','William Ouyang',''],
            ['Vincent Liu','Christopher Jo',''],
            ['Bernard Yuan','Deniz Kalaycioglu',''],
            ['Adhip Sacheti','Daniel Chen',''],
            ['Raphael Kim','Vincent Liu',''],
        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('family_tree'));
        chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }
}
    