function Kaleidoscope() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['Deneka Hypolite','',''],
['Ellen Lai','',''],
['Chris Lee','',''],
['Jessica Ma','',''],
['Nabila Walji','',''],
['Ran Yi','',''],
['Randall Aluwi','',''],
['Eric Tang','',''],
['Chris Chan','Ran Yi','',''],
['Christine Chang','Jessica Ma','',''],
['Margaret Sheng','',''],
['Amanda Davenport','Nabila Walji','',''],
['Song Im','Christine Chang','',''],
['Parthesh Karna','Nabila Walji','',''],
['Casey Piper','Margaret Sheng','',''],
['Min Kim','Amanda Davenport','',''],
['Michelle Berman','Casey Piper','',''],
['Umang Patel','Parthesh Karna','',''],
['Kunal Natu','',''],
['Lydia Yi','Song Im','',''],
['Alvi Hasan','Kunal Natu','',''],
['Sidharth Madan','Michelle Berman','',''],
['Jisoo Park','Min Kim','',''],
['Carol Kim','Kunal Natu','',''],

    ]);

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }}
    