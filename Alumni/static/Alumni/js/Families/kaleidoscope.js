function Kaleidoscope() {
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
	['<a href="/profile/13"> Deneka Hypolite','',''],
['<a href="/profile/18"> Ellen Lai','',''],
['<a href="/profile/19"> Chris Lee','',''],
['<a href="/profile/23"> Jessica Ma','',''],
['<a href="/profile/33"> Nabila Walji','',''],
['<a href="/profile/35"> Sophie Wong','',''],
['<a href="/profile/37"> Ran Yi','',''],
['<a href="/profile/39"> Randall Aluwi','<a href="/profile/35"> Sophie Wong',''],
['<a href="/profile/43"> Eric Tang-1','<a href="/profile/35"> Sophie Wong',''],
['<a href="/profile/47"> Christine Chang','<a href="/profile/23"> Jessica Ma',''],
['<a href="/profile/46"> Chris Chan','<a href="/profile/37"> Ran Yi',''],
['<a href="/profile/78"> Margaret Sheng','<a href="/profile/43"> Eric Tang-1',''],
['<a href="/profile/83"> Amanda Davenport','<a href="/profile/33"> Nabila Walji',''],
['<a href="/profile/86"> Song Im','<a href="/profile/47"> Christine Chang',''],
['<a href="/profile/88"> Parthesh Karna','<a href="/profile/33"> Nabila Walji',''],
['<a href="/profile/90"> Gabriella Moskowitz','<a href="/profile/47"> Christine Chang',''],
['<a href="/profile/103"> Casey Piper','<a href="/profile/78"> Margaret Sheng',''],
['<a href="/profile/114"> Min Kim','<a href="/profile/83"> Amanda Davenport',''],
['<a href="/profile/131"> Michelle Berman','<a href="/profile/103"> Casey Piper',''],
['<a href="/profile/142"> Umang Patel','<a href="/profile/88"> Parthesh Karna',''],
['<a href="/profile/146"> Kunal Natu','<a href="/profile/90"> Gabriella Moskowitz',''],
['<a href="/profile/151"> Lydia Yi','<a href="/profile/86"> Song Im',''],
['<a href="/profile/154"> Alvi Hasan','<a href="/profile/146"> Kunal Natu',''],
['<a href="/profile/162"> Sidharth Madan','<a href="/profile/131"> Michelle Berman',''],
['<a href="/profile/164"> Jisoo Park','<a href="/profile/114"> Min Kim',''],
['<a href="/profile/174"> Carol Kim','<a href="/profile/146"> Kunal Natu',''],
['<a href="/profile/190"> Adil Majid','<a href="/profile/142"> Umang Patel',''],
['<a href="/profile/207"> Anish Singh','<a href="/profile/154"> Alvi Hasan',''],
['<a href="/profile/215"> Cynthia Hsia','<a href="/profile/174"> Carol Kim',''],
['<a href="/profile/219"> Lawrence Hu','<a href="/profile/164"> Jisoo Park',''],
['<a href="/profile/229"> Rishi Khanna','<a href="/profile/162"> Sidharth Madan',''],
['<a href="/profile/230"> Donna Lee','<a href="/profile/190"> Adil Majid',''],
['<a href="/profile/233"> Christopher Ruland','<a href="/profile/154"> Alvi Hasan',''],
['<a href="/profile/252"> Roma Desai','<a href="/profile/229"> Rishi Khanna',''],
['<a href="/profile/258"> Vanessa Kalu','<a href="/profile/233"> Christopher Ruland',''],
['<a href="/profile/265"> Misha Yu','<a href="/profile/219"> Lawrence Hu',''],

        ]);

        var chart = new google.visualization.OrgChart(document.getElementById('kaleidoscope_tree'));
        chart.draw(data, {allowHtml:true, nodeClass:"node"});
        }}
        