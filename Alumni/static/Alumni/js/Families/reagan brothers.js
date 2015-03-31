function Reagan Brothers() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['Brian Ju','',''],
['Anuj Kumar','',''],
['Abhishek Shah','',''],
['Kenneth Sim','',''],
['Peter Sukits','',''],
['Jigar Vora','',''],
['Malvika Tamhane','Jigar Vora','',''],
['Matthew Tsau','Peter Sukits','',''],
['Nicholas Yoder','Malvika Tamhane','',''],
['Raymond Liu','Anuj Kumar','',''],
['Matt Glantz','Raymond Liu','',''],
['Mark Luk','Anuj Kumar','',''],
['Victor Tam','Victor Tam','',''],
['William Chu','Nicholas Yoder','',''],
['Wangeci Ngari','Mark Luk','',''],
['Valerie Jordan','Matt Glantz','',''],
['Seungtaek Park','Raymond Liu','',''],
['Shing Yan','',''],
['Suraj Baxi','Wangeci Ngari','',''],
['Alisa Deychman','Raymond Liu','',''],
['Sean Kim','Matt Glantz','',''],
['Nicole Tseng','',''],
['Daria Wong','Raymond Liu','',''],
['Jun Lee','',''],
['Elsa Wu','Nicole Tseng','',''],
['Tricia Chiou','',''],
['Brian Groudan','Sean Kim','',''],
['Andrew Yeung','Nicole Tseng','',''],
['Kathryn Davis','Daria Wong','',''],
['Amanda Ho','Suraj Baxi','',''],
['Stefanie Chan','Elsa Wu','',''],
['Megan Kwan','Jun Lee','',''],
['David Baboolall','Daria Wong','',''],
['Kathleen Dolan','Alisa Deychman','',''],
['Vivek Sainanee','Seungtaek Park','',''],
['Heidi Yang','',''],
['Lincoln He','Alisa Deychman','',''],
['Margo Johnson','Kathryn Davis','',''],
['Barnik Saha','Brian Groudan','',''],
['Justin Lechner','',''],

    ]);

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }}
    