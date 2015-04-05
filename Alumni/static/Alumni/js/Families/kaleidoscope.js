function Kaleidoscope() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	[Deneka Hypolite,'',''],
[Ellen Lai,'',''],
[Chris Lee,'',''],
[Jessica Ma,'',''],
[Nabila Walji,'',''],
[Sophie Wong,'',''],
[Ran Yi,'',''],
[Randall Aluwi,Sophie Wong',''],
[Eric Tang-1,Sophie Wong',''],
[Chris Chan,Ran Yi',''],
[Christine Chang,Jessica Ma',''],
[Margaret Sheng,Eric Tang-1',''],
[Amanda Davenport,Nabila Walji',''],
[Song Im,Christine Chang',''],
[Parthesh Karna,Nabila Walji',''],
[Gabriella Moskowitz,Christine Chang',''],
[Casey Piper,Margaret Sheng',''],
[Min Kim,Amanda Davenport',''],
[Michelle Berman,Casey Piper',''],
[Umang Patel,Parthesh Karna',''],
[Kunal Natu,Gabriella Moskowitz',''],
[Lydia Yi,Song Im',''],
[Alvi Hasan,Kunal Natu',''],
[Sidharth Madan,Michelle Berman',''],
[Jisoo Park,Min Kim',''],
[Carol Kim,Kunal Natu',''],
[Adil Majid,Umang Patel',''],
[Anish Singh,Alvi Hasan',''],
[Cynthia Hsia,Carol Kim',''],
[Lawrence Hu,Jisoo Park',''],
[Rishi Khanna,Sidharth Madan',''],
[Donna Lee,Adil Majid',''],
[Christopher Ruland,Alvi Hasan',''],
[Roma Desai,Rishi Khanna',''],
[Vanessa Kalu,Christopher Ruland',''],
[Misha Yu,Lawrence Hu',''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('kaleidoscope_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        