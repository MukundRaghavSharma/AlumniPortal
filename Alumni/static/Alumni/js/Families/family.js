function Family() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['Patrick Cao','',''],
['Julian Chun','',''],
['Chris Chyu','',''],
['Andrew Kiang','',''],
['Jennifer Suh','',''],
['Jay Khil','Andrew Kiang',''],
['Jessica Wong','Jennifer Suh',''],
['Niharika Bandi','Jay Khil',''],
['Xiao-Lan Wong','Patrick Cao',''],
['Sheldon Cheung','Xiao-Lan Wong',''],
['Daniel Chen','Jessica Wong',''],
['Shi Chung','Jay Khil',''],
['William Ouyang','Jessica Wong',''],
['Neil Sethi','Niharika Bandi',''],
['Elizabeth Koh','Sheldon Cheung',''],
['Christopher Jo','Shi Chung',''],
['Deniz Kalaycioglu','William Ouyang',''],
['Issac Kwon','Neil Sethi',''],
['Vincent Liu','Christopher Jo',''],
['Bernard Yuan','Deniz Kalaycioglu',''],
['Adhip Sacheti','Daniel Chen',''],
['Miko Bautista','Deniz Kalaycioglu',''],
['Raphael Kim','Vincent Liu',''],
['Olga Zubashko','Issac Kwon',''],
['Tiffany Chen-Zeyu','Mia Wang',''],
['Willa Lu','Mia Wang',''],
['Baek Kyoum','Mia Wang',''],
['Alex Tsai','Mia Wang',''],
['Richard Lee','Mia Wang',''],
['Amy Fan','Mia Wang',''],
['Christine Kwon','Mia Wang',''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('family_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        