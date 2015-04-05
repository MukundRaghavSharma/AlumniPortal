function Dynasty() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	[Imee Chan,'',''],
[Daniel Kim,'',''],
[Melanie Mui,'',''],
[Anna Ly,Ellen Lai',''],
[Lu Zhang,Melanie Mui',''],
[Jason Ma,Anna Ly',''],
[Scarlett Su,Anna Ly',''],
[Konstantin Vidensky,Lu Zhang',''],
[Hugo Zhang,Jason Ma',''],
[Alvin Poh,Scarlett Su',''],
[Stephanie Yue,Hugo Zhang',''],
[Ahmad Shamsuddin,Hugo Zhang',''],
[Zachary Rousselle,Konstantin Vidensky',''],
[Nathaniel Eliason,Zachary Rousselle',''],
[Dixon Liang,Ahmad Shamsuddin',''],
[Alvin Mathew,Nathaniel Eliason',''],
[Yvonne Yuan,Dixon Liang',''],
[Nathaniel Benzaquen-Ouakrat,Zachary Rousselle',''],
[Shreeyagya Khemka,Nathaniel Eliason',''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('dynasty_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        