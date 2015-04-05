function Roc_a_Fellas() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	[Jin Fu,'',''],
[Kevin Hsieh,'',''],
[Kenny Loh,'',''],
[Malcolm Ong,'',''],
[Dynne Sung,'',''],
[Kenneth Yu,'',''],
[Julia Degeratu,Dynne Sung',''],
[Angela Guh,Kenny Loh',''],
[Frank Zhang,Jin Fu',''],
[Michael Lu,Kenneth Yu',''],
[Ji-Soo Hong,Frank Zhang',''],
[Erica Tang,Angela Guh',''],
[Kimberly Chan,Erica Tang',''],
[Joanna Hartzmark,Angela Guh',''],
[Danielle Rosenfeld,Julia Degeratu',''],
[Jason Lei,Michael Lu',''],
[Meghan Nahass,Danielle Rosenfeld',''],
[Julia Choicer,Jason Ma',''],
[Skye Kim,Erica Tang',''],
[Joanna Chen,Joanna Hartzmark',''],
[Eumie Kim,Kimberly Chan',''],
[Emily Lee,Meghan Nahass',''],
[Charles Mbaruguru,Jason Lei',''],
[Hayden Tang,Ji-Soo Hong',''],
[Brenda Lee,Hayden Tang',''],
[Johnny Bae,Charles Mbaruguru',''],
[Matt Wilson,Julia Choicer',''],
[Emily Wright,Emily Wright',''],
[Karthik Annaamalai,Joanna Chen',''],
[Sanika Natu,Eumie Kim',''],
[Chloe Chia,Brenda Lee',''],
[Danning Wang,Matt Wilson',''],
[Nikita Bokil,Sanika Natu',''],
[Yoona Seon,Karthik Annaamalai',''],
[Clare Svirsko,Julia Choicer',''],
[Jobert Sauray,Karthik Annaamalai',''],
[Emily Su,Chloe Chia',''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('roc_a_fellas_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        